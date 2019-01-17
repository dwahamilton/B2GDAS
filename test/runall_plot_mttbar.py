#! /usr/bin/env python


## _________                _____.__                            __  .__               
## \_   ___ \  ____   _____/ ____\__| ____  __ ______________ _/  |_|__| ____   ____  
## /    \  \/ /  _ \ /    \   __\|  |/ ___\|  |  \_  __ \__  \\   __\  |/  _ \ /    \ 
## \     \___(  <_> )   |  \  |  |  / /_/  >  |  /|  | \// __ \|  | |  (  <_> )   |  \
##  \______  /\____/|___|  /__|  |__\___  /|____/ |__|  (____  /__| |__|\____/|___|  /
##         \/            \/        /_____/                   \/                    \/ 
import sys
import array as array
from plot_mttbar import plot_mttbar
import os

file_list = []
# file_list.append(["ttbar_ALL.root","background"])
# file_list.append(["SingleElectron_2016_All.root","data"])
# file_list.append(["singleMuon_ALL.root","data"])
# file_list.append(["WJetsToLNu_Wpt-0To50.root","background"])
# file_list.append(["WJetsToLNu_Wpt-50To100.root","background"])
# file_list.append(["WJetsToLNu_Pt-100To250.root","background"])
# file_list.append(["WJetsToLNu_Pt-250To400.root","background"])
# file_list.append(["WJetsToLNu_Pt-400To600.root","background"])
# file_list.append(["WJetsToLNu_Pt-600ToInf.root","background"])

# file_list.append(["QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8.root","background"])

# file_list.append(["QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8.root","background"])
# file_list.append(["QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8.root","background"])

# file_list.append(["rsg_500.root","signal"])
# file_list.append(["rsg_750.root","signal"])
# file_list.append(["rsg_1000.root","signal"])
# file_list.append(["rsg_1250.root","signal"])
# file_list.append(["rsg_1500.root","signal"])
# file_list.append(["rsg_2000.root","signal"])
# file_list.append(["rsg_2500.root","signal"])
file_list.append(["rsg_3000.root","signal"])
# file_list.append(["rsg_3500.root","signal"])
# file_list.append(["rsg_4000.root","signal"])
# file_list.append(["rsg_4500.root","signal"])
# file_list.append(["rsg_5000.root","signal"])
# file_list.append(["singletop_schan.root","background"])
# file_list.append(["singletop_tWchan_antitop.root","background"])
# file_list.append(["singletop_tWchan_top.root","background"])
# file_list.append(["singletop_tchan_antitop.root","background"])
# file_list.append(["singletop_tchan_top.root","background"])

outputs = ["./output","./output/electron","./output/muon",
"./output/electron/data","./output/electron/background","./output/electron/signal",
"./output/muon/data","./output/muon/background","./output/muon/signal"]

for output in outputs:
	if (not os.path.isdir(output)):
		os.mkdir(output)

for file,file_type in file_list:
	plot_mttbar(["--file_in", "root://cmseos.fnal.gov//store/user/cmsdas/2019/long_exercises/B2GTTbar/" + file, "--file_out", "output/electron/" + file_type + "/" + file, "--leptontype",str(0)])
	plot_mttbar(["--file_in", "root://cmseos.fnal.gov//store/user/cmsdas/2019/long_exercises/B2GTTbar/" + file, "--file_out", "output/muon/" + file_type + "/" + file, "--leptontype",str(1)])


