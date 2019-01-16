import ROOT 
import sys
import math
from optparse import OptionParser

parser = OptionParser()
parser.add_option('--signal_in', type='string', action='store',
                  dest='signal_in',
                  help='Input signal file')

parser.add_option('--background_in', type='string', action='store',
                  dest='background_in',
                  help='Input background file')

parser.add_option('--file_out', type='string', action='store',
                  dest='file_out',
                  help='Output file')

parser.add_option('--histo', type='string', action='store',
                  dest='histo',
                  help='Variable for S/B')
    
(options, args) = parser.parse_args()
argv = []

outfile = ROOT.TFile(options.file_out, "RECREATE")
fsig = ROOT.TFile.Open(options.signal_in)
fbkgd = ROOT.TFile.Open(options.background_in)

fsigHist = fsig.Get(options.histo)
fbkgdHist = fbkgd.Get(options.histo)

xmin = fbkgdHist.GetXaxis().GetXmin()
xmax = fbkgdHist.GetXaxis().GetXmax()
nbins = fbkgdHist.GetNbinsX()

xaxisTitle = fbkgdHist.GetXaxis().GetTitle()

outfile.cd()
soverb = ROOT.TH1D("Signal over Background", ";%s;S/#sqrt{B}"%(xaxisTitle),nbins,xmin,xmax) 

runningSig = 0
runningBkgd = 0
for abin in xrange(nbins):
    runningSig += fsigHist.GetBinContent(abin)
    runningBkgd += fbkgdHist.GetBinContent(abin)

    if runningBkgd == 0:
        continue 
    else: 
        soverb.SetBinContent(abin, runningSig/math.sqrt(runningBkgd))

outfile.Write()
