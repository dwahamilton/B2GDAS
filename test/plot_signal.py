from ROOT import *
 
f1 = TFile.Open("root://cmsxrootd.fnal.gov//store/user/cmsdas/2019/long_exercises/B2GTTbar/rsg_1250.root")  
f2 = TFile.Open("root://cmsxrootd.fnal.gov//store/user/cmsdas/2019/long_exercises/B2GTTbar/rsg_1500.root") 
f3 = TFile.Open("root://cmsxrootd.fnal.gov//store/user/cmsdas/2019/long_exercises/B2GTTbar/rsg_2000.root") 
f4 = TFile.Open("root://cmsxrootd.fnal.gov//store/user/cmsdas/2019/long_exercises/B2GTTbar/rsg_3000.root")  
f5 = TFile.Open("root://cmsxrootd.fnal.gov//store/user/cmsdas/2019/long_exercises/B2GTTbar/rsg_4000.root")  

gStyle.SetOptStat(0)

h1 = f1.Get("h_mttbar_true") 
h1.SetLineWidth(3)
h1.SetLineColor(kBlue)
h1.SetTitle("Mass ttbar for Different Signals")
h1.GetXaxis().SetTitle("Mass ttbar (GeV)")
h1.Draw()

h2 = f2.Get("h_mttbar_true") 
h2.SetLineWidth(3)
h2.SetLineColor(kGreen)
h2.Draw("SAME")

h3 = f3.Get("h_mttbar_true") 
h3.SetLineWidth(3)
h3.SetLineColor(kRed)
h3.Draw("SAME")

h4 = f4.Get("h_mttbar_true") 
h4.SetLineWidth(3)
h4.SetLineColor(kOrange)
h4.Draw("SAME")

h5 = f5.Get("h_mttbar_true") 
h5.SetLineWidth(3)
h5.SetLineColor(kViolet)
h5.Draw("SAME")

legend = TLegend(0.5,0.41,0.9,0.74)
legend.AddEntry(h1,"1250 GeV","L")
legend.AddEntry(h2,"1500 GeV","L")
legend.AddEntry(h3,"2000 GeV","L")
legend.AddEntry(h4,"3000 GeV","L")
legend.AddEntry(h5,"4000 GeV","L")
legend.Draw()
