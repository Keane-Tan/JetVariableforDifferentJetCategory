from collections import OrderedDict

allVars = {
        'jPtAK8':                  [r"$p_{T}$ [GeV]",         40,    0.0,    3500.0],
        'jEtaAK8':                 [r"$\eta$",                20,   -6.0,    6.0   ],
        'jPhiAK8':                 [r"$\phi$",                20,   -4.0,    4.0   ],
        'jAxismajorAK8':           [r"$\sigma_{major}(J)$",   40,     0.0,    0.5   ],
        'jAxisminorAK8':           [r"$\sigma_{minor}(J)$",   40,     0.0,    0.3   ],
        'jChEMEFractAK8':          ["fChEM(J)",               50,     0.0,    1.0   ],
        'jChHadEFractAK8':         ["fChHad(J)",              50,     0.0,    1.0   ],
        'jChHadMultAK8':           ["nChHad(J)",              145,    0.0,    145.0 ],
        'jChMultAK8':              ["nCh(J)",                 145,    0.0,    145.0 ],
        'jecfN2b1AK8':             ["ecfN2b1(J)",             50,     0.0,    0.6   ],
        'jecfN2b2AK8':             ["ecfN2b2(J)",             50,     0.0,    0.4   ],
        'jecfN3b1AK8':             ["ecfN3b1(J)",             50,     0.0,    6.0   ],
        'jecfN3b2AK8':             ["ecfN3b2(J)",             50,     0.0,    5.0   ],
        'jEleEFractAK8':           ["fEle(J)",                50,     0.0,    1.0   ],
        'jEleMultAK8':             ["nEle(J)",                8,      0.0,    8.0   ],
        'jGirthAK8':               ["girth(J)",               40,     0.0,    0.5   ],
        'jHfEMEFractAK8':          ["fHFEM(J)",               50,     0.0,    1.0   ],
        'jHfHadEFractAK8':         ["fHFHad(J)",              50,     0.0,    1.0   ],
        'jMultAK8':                ["mult(J)",                50,    0.0,    250.0 ],
        'jMuEFractAK8':            ["fMu(J)",                 50,     0.0,    1.0   ],
        'jMuMultAK8':              ["nMu(J)",                 8,      0.0,    10.0  ],
        'jNeuEmEFractAK8':         ["fNeuEM(J)",              50,     0.0,    1.0   ],
        'jNeuHadEFractAK8':        ["fNeuHad(J)",             50,     0.0,    1.0   ],
        'jNeuHadMultAK8':          ["nNeuHad(J)",             25,     0.0,    25.0  ],
        'jNeuMultAK8':             ["nNeu(J)",                120,    0.0,    120.0 ],
        'jTau1AK8':                [r"$\tau_{1}(J)$",         40,     0.0,    0.8   ],
        'jTau2AK8':                [r"$\tau_{2}(J)$",         40,     0.0,    0.65  ],
        'jTau3AK8':                [r"$\tau_{3}(J)$",         40,     0.0,    0.35  ],
        'jTau21AK8':               [r"$\tau_{21}(J)$",        40,     0.0,    1.3   ],
        'jTau32AK8':               [r"$\tau_{32}(J)$",        40,     0.0,    1.3   ],
        'jPhoEFractAK8':           ["fPho(J)",                50,     0.0,    1.0   ],
        'jPhoMultAK8':             ["nPho(J)",                110,    0.0,    110.0 ],
        'jPtDAK8':                 ["ptD",                    40,     0.0,    1.2   ],
        'jSoftDropMassAK8':        [r"$m_{SD}(J)$",           40,    0.0,    250.   ],
        'dPhijMETAK8':             [r"$\Delta\phi(J,MET)$",   30,    0.0,    4.0   ]
}

# the colors below are the default colors in matplotlib. I only added black at the end.
colorDict = {
                'Q_lD':'#ff7f0e', 
                'QM_lD':'#2ca02c', 
                'QM_Q_lD':'#bcbd22', 
                'QM_G_lD':'#17becf',
                'G_Q_lD':'#7f7f7f', 
                'G_lD':'#8c564b',  
                'lD':'#1f77b4', 
                'SMM_lD':'#d62728', 
                'SM':'#9467bd', 
                'SMM':'#e377c2',                 
                'SMM_G_lD':'#000000'
            }
            
            
inputFiles = OrderedDict()
inputFiles["mMed-600"] = "2018_mMed-600_mDark-20_rinv-0p3_alpha-peak_yukawa-1.root"
inputFiles["mMed-800"] = "2018_mMed-800_mDark-20_rinv-0p3_alpha-peak_yukawa-1.root"
inputFiles["mMed-1000"] = "2018_mMed-1000_mDark-20_rinv-0p3_alpha-peak_yukawa-1.root"
inputFiles["mMed-1500"] = "2018_mMed-1500_mDark-20_rinv-0p3_alpha-peak_yukawa-1.root"
inputFiles["baseline"] = "2018_mMed-2000_mDark-20_rinv-0p3_alpha-peak_yukawa-1.root"
inputFiles["mMed-3000"] = "2018_mMed-3000_mDark-20_rinv-0p3_alpha-peak_yukawa-1.root"
inputFiles["mMed-4000"] = "2018_mMed-4000_mDark-20_rinv-0p3_alpha-peak_yukawa-1.root"
inputFiles["mDark-1"] = "2018_mMed-2000_mDark-1_rinv-0p3_alpha-peak_yukawa-1.root"
inputFiles["mDark-100"] = "2018_mMed-2000_mDark-100_rinv-0p3_alpha-peak_yukawa-1.root"
inputFiles["rinv-0p1"] = "2018_mMed-2000_mDark-20_rinv-0p1_alpha-peak_yukawa-1.root"
inputFiles["rinv-0p7"] = "2018_mMed-2000_mDark-20_rinv-0p7_alpha-peak_yukawa-1.root"
