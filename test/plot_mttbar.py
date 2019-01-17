#! /usr/bin/env python


## _________                _____.__                            __  .__
## \_   ___ \  ____   _____/ ____\__| ____  __ ______________ _/  |_|__| ____   ____
## /    \  \/ /  _ \ /    \   __\|  |/ ___\|  |  \_  __ \__  \\   __\  |/  _ \ /    \
## \     \___(  <_> )   |  \  |  |  / /_/  >  |  /|  | \// __ \|  | |  (  <_> )   |  \
##  \______  /\____/|___|  /__|  |__\___  /|____/ |__|  (____  /__| |__|\____/|___|  /
##         \/            \/        /_____/                   \/                    \/
import sys
import array as array
from optparse import OptionParser

def plot_mttbar(argv) :
    parser = OptionParser()

    parser.add_option('--file_in', type='string', action='store',
                      dest='file_in',
                      help='Input file')

    parser.add_option('--file_out', type='string', action='store',
                      dest='file_out',
                      help='Output file')
    parser.add_option('--leptontype', type='int', action='store',
                      dest='leptontype',
                      help='0 is electron 1 is muon')
    parser.add_option('--elec_unc', type='int', action='store',
                      dest='elec_unc',
                      help='0 for no lepid uncertainty, 1 for up, 2 for down')
    parser.add_option('--muon_unc', type='int', action='store',
                      dest='muon_unc',
                      help='0 for no lepid uncertainty, 1 for up, 2 for down')
    parser.add_option('--jer', type='int', action='store',
                      dest='jer',
                      help='0 for no jer uncertainty, 1 for up, 2 for down')
    parser.add_option('--jes', type='int', action='store',
                      dest='jes',
                      help='0 for no jes uncertainty, 1 for up, 2 for down')
    #parser.add_option('--isData', action='store_true',
    #                  dest='isData',
    #                  default = False,
    #                  help='Is this Data?')
    parser.add_option('--category', type='string',action = 'store',
		      dest='category',
	              default = 'All',
		      help = 'btag is for 0 top tags, 1 b tag and  toptag is for 1 top tag 0 b tags')
    (options, args) = parser.parse_args(argv)
    argv = []

    print '===== Command line options ====='
    print options
    print '================================'

    import ROOT

    from leptonic_nu_z_component import solve_nu_tmass, solve_nu

    fout= ROOT.TFile(options.file_out, "RECREATE")
    h_mttbar = ROOT.TH1F("h_mttbar", ";m_{t#bar{t}} (GeV);Number", 100, 0, 5000)
    #h_mtopHad = ROOT.TH1F("h_mtopHad", ";m_{jet} (GeV);Number", 100, 0, 400)
    #h_mtopHadGroomed = ROOT.TH1F("h_mtopHadGroomed", ";Groomed m_{jet} (GeV);Number", 100, 0, 400)
    #Pt, Eta, Phi Spectra
    h_FatJetPt = ROOT.TH1F("h_FatJetPt", ";p_{T} (GeV);Entries", 250, 0, 5000)
    h_FatJetEta = ROOT.TH1F("h_FatJetEta", ";Fat Jet #eta;Entries", 200, -2.5, 2.5)
    h_FatJetPhi = ROOT.TH1F("h_FatJetPhi", ";Fat Jet #phi;Entries", 200, -3.14, 3.14)
    h_GenWeight = ROOT.TH1F("h_GenWeight", ";blah;blah", 200, 0, 50)
    #h_SemiLeptTrig          = ROOT.TH1F("h_SemiLeptTrig", ";blah;blah", 200, 0, 500)
    h_SemiLeptWeight        = ROOT.TH1F("h_SemiLeptWeight", ";blah;blah", 200, 0, 50)
    h_PUWeight              = ROOT.TH1F("h_PUWeight", ";blah;blah", 200, 0, 50)
    h_FatJetRap             = ROOT.TH1F("h_FatJetRap", ";blah;blah", 200, 0, 500)
    h_FatJetEnergy          = ROOT.TH1F("h_FatJetEnergy", ";Fat Jet Energy [GeV];Entries", 250, 0, 5000)
    h_FatJetBDisc           = ROOT.TH1F("h_FatJetBDisc", ";B Discriminant;Entries", 200, 0, 1)
    h_FatJetMass            = ROOT.TH1F("h_FatJetMass", ";Fat Jet Mass [GeV];Entries", 200, 0, 500)
    h_FatJetMassSoftDrop    = ROOT.TH1F("h_FatJetMassSoftDrop", ";Fat Jet SD Mass [GeV];Entries", 200, 0, 500)
    h_FatJetTau32           = ROOT.TH1F("h_FatJetTau32", ";Fat Jet #tau_{32};Entries", 200, 0, 1)
    #h_FatJetTau21           = ROOT.TH1F("h_FatJetTau21", ";blah;Entries", 200, 0, 500)
    #h_FatJetSDBDiscW        = ROOT.TH1F("h_FatJetSDBDiscW", ";blah;Entries", 200, 0, 500)
    h_FatJetSDBDiscB        = ROOT.TH1F("h_FatJetSDBDiscB", ";Fat SD Jet B Discriminant;Entries", 200, 0, 1)
    h_FatJetSDsubjetWpt     = ROOT.TH1F("h_FatJetSDsubjetWpt", ";Fat SD Jet W Pt [GeV];Entries", 200, 0, 500)
    h_FatJetSDsubjetWmass   = ROOT.TH1F("h_FatJetSDsubjetWmass", ";Fat SD Jet W mass [GeV];Entries", 200, 0, 500)
    h_FatJetSDsubjetBpt     = ROOT.TH1F("h_FatJetSDsubjetBpt", ";Fat SD Jet B Pt [GeV];Entries", 200, 0, 500)
    h_FatJetSDsubjetBmass   = ROOT.TH1F("h_FatJetSDsubjetBmass", ";Fat SD Jet B Mass [GeV];Entries", 200, 0, 500)
    #h_FatJetJECUpSys        = ROOT.TH1F("h_FatJetJECUpSys", ";blah;Entries", 200, 0, 500)
    #h_FatJetJECDnSys        = ROOT.TH1F("h_FatJetJECDnSys", ";blah;Entries", 200, 0, 500)
    #h_FatJetJERUpSys        = ROOT.TH1F("h_FatJetJERUpSys", ";blah;Entries", 200, 0, 500)
    #h_FatJetJERDnSys        = ROOT.TH1F("h_FatJetJERDnSys", ";blah;Entries", 200, 0, 500)
    #h_LeptonType            = ROOT.TH1F("h_LeptonType", ";blah;Entries", 200, 0, 500)
    h_LeptonPt              = ROOT.TH1F("h_LeptonPt", ";Lepton Pt [GeV];Entries", 200, 0, 500)
    h_LeptonEta             = ROOT.TH1F("h_LeptonEta", ";Lepton #eta;Entries", 200, -2.5, 2.5)
    h_LeptonPhi             = ROOT.TH1F("h_LeptonPhi", ";Lepton #phi;Entries", 200, -3.14, 3.14)
    h_LeptonEnergy          = ROOT.TH1F("h_LeptonEnergy", ";Lepton Energy [GeV];Entries", 200, 0, 500)
    h_LeptonIso             = ROOT.TH1F("h_LeptonIso", ";Lepton Iso;Entries", 200, 0, 500)
    h_LeptonPtRel           = ROOT.TH1F("h_LeptonPtRel", ";Lepton PtRel [GeV];Entries", 200, 0, 500)
    h_LeptonDRMin           = ROOT.TH1F("h_LeptonDRMin", ";LeptonDRMin;Entries", 200, 0, 5)
    h_SemiLepMETpt          = ROOT.TH1F("h_SemiLepMETpt", ";MET Pt [GeV];Entries", 200, 0, 500)
    h_SemiLepMETphi         = ROOT.TH1F("h_SemiLepMETphi", ";MET #phi;Entries", 200, -3.14, 3.14)
    h_SemiLepNvtx           = ROOT.TH1F("h_SemiLepNvtx", ";N Vertex;Entries", 25, -0.5, 19.5)
    h_FatJetDeltaPhiLep     = ROOT.TH1F("h_FatJetDeltaPhiLep", ";#Delta#Phi;Entries", 200, -3.14, 3.14)
    h_NearestAK4JetBDisc    = ROOT.TH1F("h_NearestAK4JetBDisc", ";AK4 B Discriminant;Entries", 200, 0, 1)
    h_NearestAK4JetPt       = ROOT.TH1F("h_NearestAK4JetPt", ";AK4 Jet Pt [GeV];Entries", 200, 0, 500)
    h_NearestAK4JetEta      = ROOT.TH1F("h_NearestAK4JetEta", ";AK4 Jet #eta;Entries", 200, -2.5, 2.5)
    h_NearestAK4JetPhi      = ROOT.TH1F("h_NearestAK4JetPhi", ";AK4 Jet #phi;Entries", 200, -3.14, 3.14)
    h_NearestAK4JetMass     = ROOT.TH1F("h_NearestAK4JetMass", ";AK4 Jet Mass [GeV];Entries", 200, 0, 500)
    #h_NearestAK4JetJECUpSys = ROOT.TH1F("h_NearestAK4JetJECUpSys", ";blah;Entries", 200, 0, 500)
    #h_NearestAK4JetJECDnSys = ROOT.TH1F("h_NearestAK4JetJECDnSys", ";blah;Entries", 200, 0, 500)
    #h_NearestAK4JetJERUpSys = ROOT.TH1F("h_NearestAK4JetJERUpSys", ";blah;Entries", 200, 0, 500)
    #h_NearestAK4JetJERDnSys = ROOT.TH1F("h_NearestAK4JetJERDnSys", ";blah;Entries", 200, 0, 500)
    #h_SemiLeptRunNum        = ROOT.TH1F("h_SemiLeptRunNum", ";blah;Entries", 200, 0, 500)
    #h_SemiLeptLumiNum       = ROOT.TH1F("h_SemiLeptLumiNum", ";blah;Entries", 200, 0, 500)
    #h_SemiLeptEventNum      = ROOT.TH1F("h_SemiLeptEventNum", ";blah;Entries", 200, 0, 500)

    fin = ROOT.TFile.Open(options.file_in)

    trees = [ fin.Get("TreeSemiLept") ]

    purw = ROOT.TFile.Open("purw.root")
    h_purw = purw.Get("pileup")

    for itree,t in enumerate(trees) :

        #if options.isData :
        SemiLeptTrig        =  ROOT.vector('int')()
        SemiLeptWeight      = array.array('f', [0.] )
        PUWeight            = array.array('f', [0.] )
        GenWeight           = array.array('f', [0.] )
        LeptonIDWeight      = array.array('f', [0.] )
        LeptonIDWeightUnc   = array.array('f', [0.] )
        MuonTrkWeight       = array.array('f', [0.] )
        MuonTrkWeightUnc    = array.array('f', [0.] )
        FatJetPt            = array.array('f', [-1.])
        FatJetEta           = array.array('f', [-1.])
        FatJetPhi           = array.array('f', [-1.])
        FatJetRap           = array.array('f', [-1.])
        FatJetEnergy        = array.array('f', [-1.])
        FatJetBDisc         = array.array('f', [-1.])
        FatJetMass          = array.array('f', [-1.])
        FatJetMassSoftDrop  = array.array('f', [-1.])
        FatJetTau32         = array.array('f', [-1.])
        FatJetTau21         = array.array('f', [-1.])
        FatJetSDBDiscW      = array.array('f', [-1.])
        FatJetSDBDiscB      = array.array('f', [-1.])
        FatJetSDsubjetWpt   = array.array('f', [-1.])
        FatJetSDsubjetWmass = array.array('f', [-1.])
        FatJetSDsubjetBpt   = array.array('f', [-1.])
        FatJetSDsubjetBmass = array.array('f', [-1.])
        FatJetJECUpSys      = array.array('f', [-1.])
        FatJetJECDnSys      = array.array('f', [-1.])
        FatJetJERUpSys      = array.array('f', [-1.])
        FatJetJERDnSys      = array.array('f', [-1.])
        LeptonType          = array.array('i', [-1])
        LeptonPt            = array.array('f', [-1.])
        LeptonEta           = array.array('f', [-1.])
        LeptonPhi           = array.array('f', [-1.])
        LeptonEnergy        = array.array('f', [-1.])
        LeptonIso           = array.array('f', [-1.])
        LeptonPtRel         = array.array('f', [-1.])
        LeptonDRMin         = array.array('f', [-1.])
        SemiLepMETpt        = array.array('f', [-1.])
        SemiLepMETphi       = array.array('f', [-1.])
        SemiLepNvtx         = array.array('i', [0])
        FatJetDeltaPhiLep      = array.array('f', [-1.])
        NearestAK4JetBDisc            = array.array('f', [-1.])
        NearestAK4JetPt     = array.array('f', [-1.])
        NearestAK4JetEta    = array.array('f', [-1.])
        NearestAK4JetPhi    = array.array('f', [-1.])
        NearestAK4JetMass   = array.array('f', [-1.])
        NearestAK4JetJECUpSys = array.array('f', [-1.])
        NearestAK4JetJECDnSys = array.array('f', [-1.])
        NearestAK4JetJERUpSys = array.array('f', [-1.])
        NearestAK4JetJERDnSys = array.array('f', [-1.])
        SemiLeptRunNum        = array.array('f', [-1.])
        SemiLeptLumiNum     = array.array('f', [-1.])
        SemiLeptEventNum      = array.array('f', [-1.])


        #if options.isData :
        t.SetBranchAddress('SemiLeptTrig'        , SemiLeptTrig )
        t.SetBranchAddress('SemiLeptWeight'      , SemiLeptWeight      ) #Combined weight of all scale factors (lepton, PU, generator) relevant for the smeileptonic event selection
        t.SetBranchAddress('PUWeight'            , PUWeight            )
        t.SetBranchAddress('GenWeight'           , GenWeight               )
        t.SetBranchAddress('FatJetPt'            , FatJetPt            )
        t.SetBranchAddress('FatJetEta'           , FatJetEta           )
        t.SetBranchAddress('FatJetPhi'           , FatJetPhi           )
        t.SetBranchAddress('FatJetRap'           , FatJetRap           )
        t.SetBranchAddress('FatJetEnergy'        , FatJetEnergy        )
        t.SetBranchAddress('FatJetBDisc'         , FatJetBDisc         )
        t.SetBranchAddress('FatJetMass'          , FatJetMass           )
        t.SetBranchAddress('FatJetMassSoftDrop'  , FatJetMassSoftDrop  )
        t.SetBranchAddress('FatJetTau32'         , FatJetTau32         )
        t.SetBranchAddress('FatJetTau21'         , FatJetTau21         )
        t.SetBranchAddress('FatJetSDBDiscW'      , FatJetSDBDiscW      )
        t.SetBranchAddress('FatJetSDBDiscB'      , FatJetSDBDiscB              )
        t.SetBranchAddress('FatJetSDsubjetWpt'   , FatJetSDsubjetWpt   )
        t.SetBranchAddress('FatJetSDsubjetWmass' , FatJetSDsubjetWmass )
        t.SetBranchAddress('FatJetSDsubjetBpt'   , FatJetSDsubjetBpt   )
        t.SetBranchAddress('FatJetSDsubjetBmass' , FatJetSDsubjetBmass )
        t.SetBranchAddress('FatJetJECUpSys'      , FatJetJECUpSys      )
        t.SetBranchAddress('FatJetJECDnSys'      , FatJetJECDnSys      )
        t.SetBranchAddress('FatJetJERUpSys'      , FatJetJERUpSys      )
        t.SetBranchAddress('FatJetJERDnSys'      , FatJetJERDnSys      )
        t.SetBranchAddress('LeptonType'          , LeptonType          )
        t.SetBranchAddress('LeptonPt'            , LeptonPt            )
        t.SetBranchAddress('LeptonEta'           , LeptonEta           )
        t.SetBranchAddress('LeptonPhi'           , LeptonPhi           )
        t.SetBranchAddress('LeptonEnergy'        , LeptonEnergy        )
        t.SetBranchAddress('LeptonIso'           , LeptonIso           )
        t.SetBranchAddress('LeptonPtRel'         , LeptonPtRel         )
        t.SetBranchAddress('LeptonDRMin'         , LeptonDRMin         )
        t.SetBranchAddress('SemiLepMETpt'        , SemiLepMETpt        )
        t.SetBranchAddress('SemiLepMETphi'       , SemiLepMETphi       )
        t.SetBranchAddress('SemiLepNvtx'         , SemiLepNvtx         )
        t.SetBranchAddress('FatJetDeltaPhiLep'      , FatJetDeltaPhiLep      )
        t.SetBranchAddress('NearestAK4JetBDisc'            ,NearestAK4JetBDisc             )
        t.SetBranchAddress('NearestAK4JetPt'     ,NearestAK4JetPt      )
        t.SetBranchAddress('NearestAK4JetEta'    ,NearestAK4JetEta     )
        t.SetBranchAddress('NearestAK4JetPhi'    ,NearestAK4JetPhi     )
        t.SetBranchAddress('NearestAK4JetMass'   ,NearestAK4JetMass    )
        t.SetBranchAddress('NearestAK4JetJECUpSys'      , NearestAK4JetJECUpSys)
        t.SetBranchAddress('NearestAK4JetJECDnSys'      , NearestAK4JetJECDnSys)
        t.SetBranchAddress('NearestAK4JetJERUpSys'      , NearestAK4JetJERUpSys)
        t.SetBranchAddress('NearestAK4JetJERDnSys'      , NearestAK4JetJERDnSys)
        t.SetBranchAddress('SemiLeptRunNum'         ,  SemiLeptRunNum       )
        t.SetBranchAddress('SemiLeptLumiNum'      ,  SemiLeptLumiNum    )
        t.SetBranchAddress('SemiLeptEventNum'       ,  SemiLeptEventNum     )
        t.SetBranchAddress('LeptonIDWeight'       ,  LeptonIDWeight     )
        t.SetBranchAddress('LeptonIDWeightUnc'       ,  LeptonIDWeightUnc     )
        t.SetBranchAddress('MuonTrkWeight'       ,  MuonTrkWeight     )
        t.SetBranchAddress('MuonTrkWeightUnc'       ,  MuonTrkWeightUnc     )


        t.SetBranchStatus ('*', 0)
        t.SetBranchStatus ('SemiLeptWeight', 1)
        t.SetBranchStatus ('PUWeight', 1)
        t.SetBranchStatus ('GenWeight', 1)
        t.SetBranchStatus ('FatJetPt', 1)
        t.SetBranchStatus ('FatJetEta', 1)
        t.SetBranchStatus ('FatJetPhi', 1)
        t.SetBranchStatus ('FatJetMass', 1)
        t.SetBranchStatus ('FatJetMassSoftDrop', 1)
        t.SetBranchStatus ('FatJetTau32', 1)
        t.SetBranchStatus ('SemiLeptTrig', 1)
        t.SetBranchStatus ('NearestAK4JetBDisc', 1)
        t.SetBranchStatus ('NearestAK4JetPt'   ,1 )
        t.SetBranchStatus ('NearestAK4JetEta'  ,1 )
        t.SetBranchStatus ('NearestAK4JetPhi'  ,1 )
        t.SetBranchStatus ('NearestAK4JetMass' ,1 )
        t.SetBranchStatus ('SemiLepMETpt' , 1 )
        t.SetBranchStatus ('SemiLepMETphi' , 1 )
        t.SetBranchStatus ('LeptonType'          , 1 )
        t.SetBranchStatus ('LeptonPt'            , 1)
        t.SetBranchStatus ('LeptonEta'           , 1)
        t.SetBranchStatus ('LeptonPhi'           , 1)
        t.SetBranchStatus ('LeptonEnergy'        , 1)
        t.SetBranchStatus ('LeptonIso'           , 1)
        t.SetBranchStatus ('LeptonPtRel'         , 1)
        t.SetBranchStatus ('LeptonDRMin'         , 1)
        t.SetBranchStatus ('LeptonIDWeight'      , 1)
        t.SetBranchStatus ('LeptonIDWeightUnc'      , 1)
        t.SetBranchStatus ('MuonTrkWeight'      , 1)
        t.SetBranchStatus ('MuonTrkWeightUnc'      , 1)
        t.SetBranchStatus ('SemiLepNvtx'         ,1)


        entries = t.GetEntriesFast()
        print 'Processing tree ' + str(itree)
        data_message = False    

        eventsToRun = entries
        for jentry in xrange( eventsToRun ):
            if jentry % 100000 == 0 :
                print 'processing ' + str(jentry) + '/' + str(eventsToRun)
            # get the next tree in the chain and verify
            ientry = t.GetEntry( jentry )
            if ientry < 0:
                break

            lepweight = LeptonIDWeight[0]

            new_pileup = h_purw.GetBinContent(SemiLepNvtx[0]+1)
            # print SemiLepNvtx[0]
            # print new_pileup

            new_weight = new_pileup*GenWeight[0]/abs(GenWeight[0])
            # Muons only for now
            if options.leptontype == 1:
                if LeptonType[0] != 13 :
                    continue
                if SemiLeptTrig[0] != 1  :
                    continue
                new_weight*=MuonTrkWeight[0]
                if (options.muon_unc==1):
                    lepweight -= LeptonIDWeightUnc[0]
                elif (options.muon_unc==2):
                    lepweight += LeptonIDWeightUnc[0]    


            if options.leptontype == 0:
                if LeptonType[0] != 11 :
                    continue
                if SemiLeptTrig[1] != 1  :
                    continue    
                if (options.elec_unc==1):
                    lepweight -= LeptonIDWeightUnc[0]
                elif (options.elec_unc==2):
                    lepweight += LeptonIDWeightUnc[0]    

            new_weight*=lepweight


            if options.file_out.find("data") != -1:
                if data_message==False:
                    print "Sample is data. Setting weights to 1"
                    data_message=True
                new_weight=1.0

            hadTopCandP4 = ROOT.TLorentzVector()
            hadTopCandP4.SetPtEtaPhiM( FatJetPt[0], FatJetEta[0], FatJetPhi[0], FatJetMass[0])
            bJetCandP4 = ROOT.TLorentzVector()
            bJetCandP4.SetPtEtaPhiM( NearestAK4JetPt[0], NearestAK4JetEta[0], NearestAK4JetPhi[0], NearestAK4JetMass[0])
            nuCandP4 = ROOT.TLorentzVector()
            nuCandP4.SetPtEtaPhiM( SemiLepMETpt[0], 0, SemiLepMETphi[0], SemiLepMETpt[0] )
            theLepton = ROOT.TLorentzVector()
            theLepton.SetPtEtaPhiE( LeptonPt[0], LeptonEta[0], LeptonPhi[0], LeptonEnergy[0] ) # Assume massless

            if (options.jes==1):
                bJetCandP4*=NearestAK4JetJECUpSys[0]
                hadTopCandP4*=NearestAK4JetJECUpSys[0]
            elif (options.jes==2):
                bJetCandP4*=NearestAK4JetJECDnSys[0]
                hadTopCandP4*=NearestAK4JetJECDnSys[0]

            FatJetPt[0]=hadTopCandP4.Pt()
            FatJetMass[0]=hadTopCandP4.M()
            NearestAK4JetPt[0]=bJetCandP4.Pt()
            NearestAK4JetMass[0]=bJetCandP4.M()


            tau32 = FatJetTau32[0]
            mass_sd = FatJetMassSoftDrop[0]
            bdisc = NearestAK4JetBDisc[0]

            passKin = hadTopCandP4.Perp() > 400.
            passTopTag = mass_sd > 75 and tau32 < 0.7

            pass2DCut = LeptonPtRel[0] > 55. or LeptonDRMin[0] > 0.4
            passBtag = bdisc > 0.8484

	    if options.category == 'All':
            	if not passKin or not pass2DCut or not passBtag or not passTopTag :
                    continue

	    if options.category == 'btag':
		if not passKin or not pass2DCut or not passBtag:
	 	    continue
		if passTopTag:
		    continue

	    if options.category == 'toptag':
		if not passKin or not pass2DCut or not passTopTag:
		    continue 
		if passBtag:
		    continue


            ##  ____  __.__                              __  .__         __________
            ## |    |/ _|__| ____   ____   _____ _____ _/  |_|__| ____   \______   \ ____   ____  ____
            ## |      < |  |/    \_/ __ \ /     \\__  \\   __\  |/ ___\   |       _// __ \_/ ___\/  _ \
            ## |    |  \|  |   |  \  ___/|  Y Y  \/ __ \|  | |  \  \___   |    |   \  ___/\  \__(  <_> )
            ## |____|__ \__|___|  /\___  >__|_|  (____  /__| |__|\___  >  |____|_  /\___  >\___  >____/
            ##         \/       \/     \/      \/     \/             \/          \/     \/     \/

            # Now we do our kinematic calculation based on the categories of the
            # number of top and bottom tags
            mttbar = -1.0


            lepTopCandP4 = None
            # Get the z-component of the lepton from the W mass constraint
            solution, nuz1, nuz2 = solve_nu( vlep=theLepton, vnu=nuCandP4 )
            # If there is at least one real solution, pick it up
            if solution :
                nuCandP4.SetPz( nuz1 )
            else :
                nuCandP4.SetPz( nuz1.real )

            lepTopCandP4 = nuCandP4 + theLepton + bJetCandP4

            ttbarCand = hadTopCandP4 + lepTopCandP4
            mttbar = ttbarCand.M()

            h_mttbar.Fill( mttbar, new_weight )
            #h_mtopHadGroomed.Fill( mass_sd, new_weight )
            #h_mtopHad.Fill( hadTopCandP4.M(), new_weight )
            #h_SemiLeptTrig.Fill( SemiLeptTrig[0], new_weight )
            h_SemiLeptWeight.Fill( SemiLeptWeight[0])
            h_PUWeight.Fill( PUWeight[0])
            h_GenWeight.Fill( abs(GenWeight[0]))
            h_FatJetPt.Fill( FatJetPt[0], new_weight )
            h_FatJetEta.Fill( FatJetEta[0], new_weight )
            h_FatJetPhi.Fill( FatJetPhi[0], new_weight )
            h_FatJetRap.Fill( FatJetRap[0], new_weight )
            h_FatJetEnergy.Fill( FatJetEnergy[0], new_weight )
            h_FatJetBDisc.Fill( FatJetBDisc[0], new_weight )
            h_FatJetMass.Fill( FatJetMass[0], new_weight )
            h_FatJetMassSoftDrop.Fill( FatJetMassSoftDrop[0], new_weight )
            h_FatJetTau32.Fill( FatJetTau32[0], new_weight )
            #h_FatJetTau21.Fill( FatJetTau21[0], new_weight )
            #h_FatJetSDBDiscW.Fill( FatJetSDBDiscW[0], new_weight )
            h_FatJetSDBDiscB.Fill( FatJetSDBDiscB[0], new_weight )
            h_FatJetSDsubjetWpt.Fill( FatJetSDsubjetWpt[0], new_weight )
            h_FatJetSDsubjetWmass.Fill( FatJetSDsubjetWmass[0], new_weight )
            h_FatJetSDsubjetBpt.Fill( FatJetSDsubjetBpt[0], new_weight )
            h_FatJetSDsubjetBmass.Fill( FatJetSDsubjetBmass[0], new_weight )
            #h_FatJetJECUpSys.Fill( FatJetJECUpSys[0], new_weight )
            #h_FatJetJECDnSys.Fill( FatJetJECDnSys[0], new_weight )
            #h_FatJetJERUpSys.Fill( FatJetJERUpSys[0], new_weight )
            #h_FatJetJERDnSys.Fill( FatJetJERDnSys[0], new_weight )
            #h_LeptonType.Fill( LeptonType[0], new_weight )
            h_LeptonPt.Fill( LeptonPt[0], new_weight )
            h_LeptonEta.Fill( LeptonEta[0], new_weight )
            h_LeptonPhi.Fill( LeptonPhi[0], new_weight )
            h_LeptonEnergy.Fill( LeptonEnergy[0], new_weight )
            h_LeptonIso.Fill( LeptonIso[0], new_weight )
            h_LeptonPtRel.Fill( LeptonPtRel[0], new_weight )
            h_LeptonDRMin.Fill( LeptonDRMin[0], new_weight )
            h_SemiLepMETpt.Fill( SemiLepMETpt[0], new_weight )
            h_SemiLepMETphi.Fill( SemiLepMETphi[0], new_weight )
            h_SemiLepNvtx.Fill( SemiLepNvtx[0], new_weight )
            h_FatJetDeltaPhiLep.Fill( FatJetDeltaPhiLep[0], new_weight )
            h_NearestAK4JetBDisc.Fill( NearestAK4JetBDisc[0], new_weight )
            h_NearestAK4JetPt.Fill( NearestAK4JetPt[0], new_weight )
            h_NearestAK4JetEta.Fill( NearestAK4JetEta[0], new_weight )
            h_NearestAK4JetPhi.Fill( NearestAK4JetPhi[0], new_weight )
            h_NearestAK4JetMass.Fill( NearestAK4JetMass[0], new_weight )
            #h_NearestAK4JetJECUpSys.Fill( NearestAK4JetJECUpSys[0], new_weight )
            #h_NearestAK4JetJECDnSys.Fill( NearestAK4JetJECDnSys[0], new_weight )
            #h_NearestAK4JetJERUpSys.Fill( NearestAK4JetJERUpSys[0], new_weight )
            #h_NearestAK4JetJERDnSys.Fill( NearestAK4JetJERDnSys[0], new_weight )
            #h_SemiLeptRunNum.Fill( SemiLeptRunNum[0], new_weight )
            #h_SemiLeptLumiNum.Fill( SemiLeptLumiNum[0], new_weight )
            #h_SemiLeptEventNum.Fill( SemiLeptEventNum[0], new_weight )

    fout.cd()
    fout.Write()
    fout.Close()

if __name__ == "__main__" :
    plot_mttbar(sys.argv)
