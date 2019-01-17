import ROOT 
import sys
import math
import pdb
from optparse import OptionParser
from os import listdir
from os.path import isfile, join

# Get file list
sigDir=["output/electron/signal/","output/muon/signal/"]
bkgDir=["output/electron/background/","output/muon/background/"]
sigElec=[]
sigMuon=[]
bkgElec=[]
bkgMuon=[]

for lep in xrange(0,2):
    for fName in listdir(sigDir[lep]):
	if lep==0 and (".root" in fName):
            sigElec.append(sigDir[lep]+fName)
	if lep==1 and (".root" in fName):
	    sigMuon.append(sigDir[lep]+fName)
    for fName in listdir(bkgDir[lep]):
	if lep==0 and (".root" in fName):
	    bkgElec.append(bkgDir[lep]+fName)
	if lep==1 and (".root" in fName):
	    bkgMuon.append(bkgDir[lep]+fName)

sigFiles=[sigElec,sigMuon]
bkgFiles=[bkgElec,bkgMuon]
lepLabel=["electron/","muon/"]

# Loop over all files to get histograms for signal and background
for lep in xrange(0,2):
    for sigFileName in sigFiles[lep]:
        outfileName="sigout/"+lepLabel[lep]+sigFileName.replace(sigDir[lep],"").replace(".root","_out.root")
        outfile=ROOT.TFile(outfileName,"RECREATE")
	for bkgFileName in bkgFiles[lep]:
	    fsig=ROOT.TFile.Open(sigFileName)
	    fbkgd=ROOT.TFile.Open(bkgFileName)
	    bkgDirecName=bkgFileName.replace(bkgDir[lep],"").replace(".root","")
	    outfile.mkdir(bkgDirecName)
	    outfile.cd(bkgDirecName)
            for dirKey in fsig.GetListOfKeys():
                histName=dirKey.GetName()
                histSame=0
                for dirKeyBkg in fbkgd.GetListOfKeys():
	            histBkgName=dirKeyBkg.GetName()
	            if histName==histBkgName:
	                histSame=1
	                break
                if histSame==1:

	            fsigHist = fsig.Get(histName)
	            fbkgdHist = fbkgd.Get(histName)

	    	    xmin = fbkgdHist.GetXaxis().GetXmin()
	            xmax = fbkgdHist.GetXaxis().GetXmax()
	            nbins = fbkgdHist.GetNbinsX()

	            xaxisTitle = fbkgdHist.GetXaxis().GetTitle()

		    
	            soverbName=histName+" S/B"
	            soverb = ROOT.TH1D(soverbName, ";%s;S/#sqrt{B}"%(xaxisTitle),nbins,xmin,xmax) 

	            runningSig = 0
	            runningBkgd = 0
	            for abin in xrange(nbins):
    	                runningSig += fsigHist.GetBinContent(abin)
    	                runningBkgd += fbkgdHist.GetBinContent(abin)

    	                if runningBkgd == 0:
                            continue 
    	                else: 
                    	    soverb.SetBinContent(abin, runningSig/math.sqrt(abs(runningBkgd)))
		    soverb.Write()
