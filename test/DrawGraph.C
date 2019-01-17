



void DrawGraph()
{
    gStyle->SetOptStat(0);
    TString Filenamesig = "output/muon/signal/rsg_3000.root";
    TString Filenamebkg = "output/muon/background/ttbar_ALL.root";
    TString Filenamedat = "output/muon/data/singleMuon_ALL.root";
    //TString Filenamesig = "output/electron/signal/rsg_3000.root";
    //TString Filenamebkg = "output/electron/background/ttbar_ALL.root";
    //TString Filemamedat = "output/electron/data/SingleElectron_2016_All.root";
    TFile *f_sig = new TFile(Filenamesig);
    TFile *f_bkg = new TFile(Filenamebkg);
    TFile *f_dat = new TFile(Filenamedat);
    TH1F *h_sig = (TH1F*) f_sig->Get("h_FatJetEff");
    TH1F *h_bkg = (TH1F*) f_bkg->Get("h_FatJetEff");
    TH1F *h_dat = (TH1F*) f_dat->Get("h_FatJetEff");

    Double_t N1 = h_sig->GetEntries();
    Double_t N2 = h_bkg->GetEntries();
    Double_t N3 = h_dat->GetEntries();
    //h_sig->Scale(1/N1);
    //h_bkg->Scale(1/N2);
    //h_dat->Scale(1/N3);
    h_sig->SetLineColor(1);
    h_bkg->SetLineColor(2);
    h_dat->SetLineColor(3);
    h_sig->SetMarkerStyle(20);
    h_bkg->SetMarkerStyle(22);
    h_dat->SetMarkerStyle(21);
    h_sig->SetMarkerColor(1);
    h_bkg->SetMarkerColor(2);
    h_dat->SetMarkerColor(3);
    h_sig->GetXaxis()->SetTitle("p_{T} [GeV]");
    h_sig->GetYaxis()->SetTitle("Efficiency");
    h_sig->Draw("e");
    h_dat->Draw("esame");
    h_bkg->Draw("e same");

    TLegend* leg = new TLegend(0.15,0.65,0.55,0.85,"Toptag Efficiency");
    leg->AddEntry(h_sig,"Signal");
    leg->AddEntry(h_bkg,"Background");
    leg->AddEntry(h_dat,"Data");

    leg->DrawClone("Same p");
 
    TLatex latex;
    latex.SetTextSize(0.05);
    latex.SetTextFont(61);
    latex.DrawLatex(1350,0.65,"CMSDAS");  

    latex.SetTextSize(0.035);
    latex.SetTextFont(52);
    latex.DrawLatex(1400,0.60,"2019");
}
