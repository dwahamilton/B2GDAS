void background_plotter(double lumi=36000.0){

	TFile* output = new TFile("background_plots.root","RECREATE");

	vector<pair<TString,double> > backgrounds;
	vector<TString> datas;
	vector<TString> histos;
	vector<TString> leptontype;

	backgrounds.push_back(make_pair("WJetsToLNu_Wpt-0To50.root",(1.0*57280.0)/(99983076.0*0.34)));
	backgrounds.push_back(make_pair("WJetsToLNu_Wpt-50To100.root",(1.0*3258.0)/(67082709.0*0.36)));
	backgrounds.push_back(make_pair("WJetsToLNu_Pt-100To250.root",(0.41*676.3)/(120124110.0*0.361348)));
	backgrounds.push_back(make_pair("WJetsToLNu_Pt-250To400.root",(0.43*23.94)/(12022587.0*0.368953)));
	backgrounds.push_back(make_pair("WJetsToLNu_Pt-400To600.root",(0.44*3.031)/(1939947.0*0.382909)));
	backgrounds.push_back(make_pair("WJetsToLNu_Pt-600ToInf.root",(0.44*0.4524)/(1974609.0*0.400576)));
	backgrounds.push_back(make_pair("singletop_schan.root",3.36/9651642.0));
	backgrounds.push_back(make_pair("singletop_tchan_top.root",136.02/5993676.0));
	backgrounds.push_back(make_pair("singletop_tchan_antitop.root",80.95/3928063.0));
	backgrounds.push_back(make_pair("singletop_tWchan_antitop.root",35.6/6952830.0));
	backgrounds.push_back(make_pair("singletop_tWchan_top.root",35.6/6933094.0));

	// backgrounds.push_back(make_pair("QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8.root","background"))
	// backgrounds.push_back(make_pair("QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8.root","background"))
	// backgrounds.push_back(make_pair("QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8.root","background"))
	// backgrounds.push_back(make_pair("QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8.root","background"))
	// backgrounds.push_back(make_pair("QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8.root","background"))
	// backgrounds.push_back(make_pair("QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8.root","background"))

	backgrounds.push_back(make_pair("QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8.root",7823.0/4150588.0));
	backgrounds.push_back(make_pair("QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8.root",648.2/3959986.0));
	backgrounds.push_back(make_pair("QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8.root",186.9/3896412.0));
	backgrounds.push_back(make_pair("QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8.root",32.29/3992112.0));
	backgrounds.push_back(make_pair("QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8.root",9.418/2999069.0));
	backgrounds.push_back(make_pair("QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8.root",0.84265/396409.0));
	backgrounds.push_back(make_pair("QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8.root",0.114943/397660.0));
	backgrounds.push_back(make_pair("QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8.root",0.0068291/399226.0));
	backgrounds.push_back(make_pair("QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8.root",0.0001654/391735.0));

	datas.push_back("SingleElectron_2016_All.root");
	datas.push_back("singleMuon_ALL.root");

	leptontype.push_back("electron");
	leptontype.push_back("muon");

	histos.push_back("h_mttbar");


	for (unsigned l=0; l<leptontype.size(); l++){
	//Get ttbar and background hists
	TFile* f_ttbar = TFile::Open("output/" + leptontype[l] + "/background/ttbar_ALL.root");
		for (unsigned h=0; h<histos.size(); h++){
			TFile* f_back = TFile::Open("output/" + leptontype[l] + "/background/" + backgrounds[0].first);
			TH1D* h_ttbar = (TH1D*) f_ttbar->Get(histos[h]); h_ttbar->Scale(lumi*831.76/77081156.0);
			cout<<"output/" + leptontype[l] + "/background/ttbar_ALL.root"<<" "<<h_ttbar->GetEntries()<<endl;
			TH1D* h_back = (TH1D*) f_back->Get(histos[h]); h_back->Scale(lumi*backgrounds[0].second);
			cout<<"output/" + leptontype[l] + "/background/" + backgrounds[0].first<<" "<<h_back->GetEntries()<<endl;

			for (unsigned b=1; b<backgrounds.size(); b++){
			TFile* f_back = TFile::Open("output/" + leptontype[l] + "/background/" + backgrounds[b].first);
			TH1D* temp = (TH1D*) f_back->Get(histos[h]); 
			cout<<"output/" + leptontype[l] + "/background/" + backgrounds[b].first<<" "<<temp->GetEntries()<<endl;
			temp->Scale(lumi*backgrounds[b].second);
			// new TCanvas(); temp->Draw();
			h_back->Add(temp);

			}

			//Make stack
			THStack* stack = new THStack(histos[h] + "_stack", histos[h] + ";" + h_ttbar->GetXaxis()->GetTitle() + ";" + h_ttbar->GetYaxis()->GetTitle());
			// stack->GetXaxis()->SetTitle(h_ttbar->GetXaxis()->GetTitle());
			// stack->GetYaxis()->SetTitle(h_ttbar->GetYaxis()->GetTitle());

			h_ttbar->SetFillColor(kRed);
			stack->Add(h_ttbar);
			h_back->SetFillColor(kGreen);
			stack->Add(h_back);

			output->cd();
			h_ttbar->Write();
			// stack->Write();

			//Get data hist
			TFile* f_data = TFile::Open("output/" + leptontype[l] + "/data/" + datas[0]);

			TH1D* h_data = (TH1D*) f_data->Get(histos[h]);

			for (unsigned d=1; d<datas.size(); d++){
			f_data = TFile::Open("output/" + leptontype[l] + "/data/" + datas[d]);

			h_data->Add((TH1D*) f_data->Get(histos[h]));

			}

			TCanvas* c = new TCanvas("c_" + leptontype[l] + "_" + histos[h], "c_" + leptontype[l] + "_" + histos[h], 800,600);
			stack->Draw("hist");
			h_data->Draw("same");
			TLegend* leg = new TLegend(0.7,0.7,0.9,0.9);
			leg->AddEntry(h_ttbar,"TTbar","f");
			leg->AddEntry(h_back,"Other backgrounds","f");
			leg->AddEntry(h_data,"Data","l");
			leg->Draw();
			output->cd();
			c->Write();
		}
	}

	output->Write();

}