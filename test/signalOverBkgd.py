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

parser.add_option('--histo', type='string', action='store',
                  dest='histo',
                  help='Variable for S/B')

parser.add_option('--backward', type='int', action='store',
                  dest='backward',
                  default=0,
                  help='Backward direction of integration')
    
(options, args) = parser.parse_args()
argv = []

sigName = options.signal_in.split("/")[-1].split(".")[0]
bkgdName = options.background_in.split("/")[-1].split(".")[0]

outfile = ROOT.TFile("%s_Over_%s_%s.root"%(sigName,bkgdName,options.histo), "RECREATE")
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
for abin in xrange(nbins+2):
    if options.backward:
        abin = nbins+1 - abin
    runningSig += fsigHist.GetBinContent(abin)
    runningBkgd += fbkgdHist.GetBinContent(abin)

    if runningBkgd == 0:
        continue 
    else: 
        soverb.SetBinContent(abin, runningSig/(1+math.sqrt(runningBkgd)))

outfile.Write()
if options.backward:
    soverb.SaveAs("%s_Over_%s_%s_Backward.C"%(sigName, bkgdName, options.histo))
else:
    soverb.SaveAs("%s_Over_%s_%s_Upward.C"%(sigName, bkgdName, options.histo))
