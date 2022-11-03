# use the t-channel environment to run this script
# we want to normalize the distributions by the pT distribution of the Q jets
import uproot as up
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.gridspec as gridspec
import mplhep as hep
from collections import OrderedDict
import pandas as pd
import os
# importing custom libraries
import variables as vr
import utility as ut
import mplhep as hep
mpl.use('Agg')
mpl.rc("font", family="serif", size=20)

weightDict = np.load("weights.npz")
    
fileName = "tree_SVJ_mMed-1000_mDark-20_rinv-0p3_alpha-peak_yukawa-1_NN.root"
f = up.open(fileName)
ftree = f['tree']
branches = ftree.arrays(list(vr.allVars.keys()) + ['JetsAK8_hvCategory'],library="pd")
JetsAK8_hvCategory = branches['JetsAK8_hvCategory']

allCats = list(vr.colorDict.keys())

pTBinEdges = weightDict["bin_edges"]

twoCats = [
            [['Q_lD','QM_lD','QM_Q_lD','QM_G_lD'],"highDark"],
            [['G_Q_lD','G_lD','lD'],"midDark"], 
            [['SMM_lD','SM','SMM','SMM_G_lD'],"lowDark"]
]

for cats,catsLab in twoCats:
    for var in vr.allVars.keys():
        histogramList = []
        histogramLabels = []
        histogramColors = []
        binEdges = ut.getBin(vr.allVars,var)
        for catLabel in cats:
            cBranches = branches[JetsAK8_hvCategory == ut.hvCat_encode(catLabel)]
            pTAK8 = cBranches['jPtAK8']
            cWeights = weightDict[catLabel]
            cWeightInds = np.digitize(pTAK8,pTBinEdges) - 1
            histWeights = np.take(cWeights,cWeightInds)
            varBranch = cBranches[var]
            hc,bins = np.histogram(varBranch,binEdges,weights=histWeights)
            histogramList.append(hc)
            histogramLabels.append(catLabel)
            histogramColors.append(vr.colorDict[catLabel])
        plt.figure(figsize=(12,8))
        hep.histplot(histogramList,binEdges,color=histogramColors,label=histogramLabels)
        plt.legend(fontsize=13)
        plt.ylim(10)
        plt.ylabel("pT Weighted Events")
        plt.xlabel(vr.allVars[var][0])
        plt.yscale("log")
        plt.savefig("plots/{}_{}.png".format(var,catsLab))
    
        
