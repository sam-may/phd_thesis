import sys, os

pho_kin_had = [20, 29, 14, 23, 51, 52, 41, 42]
#pho_kin_had = [22, 31, 16, 25, 70, 71, 45, 46]
jet_kin_had = [9, 10, 11, 12, 34, 35, 36, 37, 53, 54, 55, 56, 32, 33, 38, 5]
#jet_kin_had = [11,12,13,14,36,37,38,39,72,73,74,75,34,35,40,7]
dipho_kin_had = [50, 2, 4, 49, 46]
#dipho_kin_had = [69,2,4,68,56]
evt_kin_had = [39]
#evt_kin_had = [41]
all_had = pho_kin_had + jet_kin_had + dipho_kin_had + evt_kin_had
print(len(all_had))


pho_kin_lep = [20, 29, 14, 23, 62, 63, 43, 44]
#pho_kin_lep = [22,31,16,25,88,89,47,48]
jet_kin_lep = [9, 10, 11, 34, 35, 36, 64, 65, 66, 50, 51, 38, 5]
#jet_kin_lep = [11,12,13,36,37,38,90,91,92,65,66,40,7]
dipho_kin_lep = [61, 2, 4, 60, 57]
#dipho_kin_lep = [87,2,4,86,75]
lep_kin_lep = [45, 46, 56]
#lep_kin_lep = [51,52,71]
evt_kin_lep = [39]
#evt_kin_lep = [41]
all_lep = pho_kin_lep + jet_kin_lep + dipho_kin_lep + lep_kin_lep + evt_kin_lep
print(len(all_lep))


files = { "Hadronic" : "ttHHadronic_RunII_MVA_Presel_v4.11_7Apr2020_impute_histogramsRunIIstd", "Leptonic" : "ttHLeptonic_RunII_MVA_Presel_v4.11_7Apr2020_histogramsRunIIstd" }

info = { 
        "Hadronic" : 
        { 
            "pho_kin" : { "label" : "Photon Kinematics", "numbers" : pho_kin_had},
            "jet_kin" : { "label" : "Jet Kinematics", "numbers" : jet_kin_had},
            "dipho_kin" : { "label" : "DiPhoton Kinematics", "numbers" : dipho_kin_had},
            "evt_kin" : { "label" : "Event-level Kinematics", "numbers" : evt_kin_had},
            "all" : { "label" : "", "numbers" : all_had},
        },
        "Leptonic" :
	{ 
            "pho_kin" : { "label" : "Photon Kinematics", "numbers" : pho_kin_lep},
            "jet_kin" : { "label" : "Jet Kinematics", "numbers" : jet_kin_lep},
            "dipho_kin" : { "label" : "DiPhoton Kinematics", "numbers" : dipho_kin_lep},
            "evt_kin" : { "label" : "Event-level Kinematics", "numbers" : evt_kin_lep},
            "lep_kin" : { "label" : "Lepton Kinematics", "numbers" : lep_kin_lep},
            "all" : { "label" : "", "numbers" : all_lep},
        },
    }


counter = -1
set_counter = 0
width = 2
with open("hlf_plots_auto.tex", "w") as f_out:
    for channel in info.keys():
        for style in [""]:
            for title, group in info[channel].items():
                if title == "all":
                    continue
                for i in group["numbers"]:
                    counter += 1
                    if counter % (width*2) == 0:
                        f_out.write("\\clearpage\n")
                    if counter % width == 0:
                        #if set_counter % 3 == 0:
                        #    f_out.write("\\clearpage\n")
                        f_out.write("\\begin{figure} [htbp!] \n")
                        f_out.write("   \\centering\n")
                        #f_out.write("   \\hspace*{-0.25cm}\n")
                        f_out.write("   \\begin{tabular}{c c}\n")
                    suffix = "&" if (counter + 1) % width != 0 else ""
                    f_out.write("       \includegraphics[width=0.43\linewidth,page=%d]{{figures/tth/%s%s}.pdf} %s\n" % (i, files[channel], style, suffix))
                    if (counter + 1) % width == 0:
                        f_out.write("   \\end{tabular}\n")
                        caption = "Agreement between data and simulation" if style == "" else "Comparison of signal and background shapes"
                        f_out.write("   \\caption{%s for the %s input features to the BDT-bkg algorithm in the t$\\bar{\\text{t}}$H %s channel.}\n" % (caption, group["label"].lower(), channel.lower()))
                        f_out.write("   \\label{fig:appA_%s_%s_%d}\n" % (channel, style, i))
                        f_out.write("\\end{figure}\n\n")
                        set_counter += 1
