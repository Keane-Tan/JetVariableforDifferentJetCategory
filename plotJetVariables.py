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

weightDict = np.load("weights.npz")
print(weightDict.files)
for stuff in weightDict.files:
    print(stuff)
    print(len(weightDict[stuff]))
    print(weightDict[stuff])
    print()
    
fileName = "tree_SVJ_mMed-1000_mDark-20_rinv-0p3_alpha-peak_yukawa-1_NN.root"
f = up.open(fileName)
ftree = f['tree']
branches = ftree.arrays(list(vr.allVars.keys()) + ['JetsAK8_hvCategory'],library="pd")
JetsAK8_hvCategory = branches['JetsAK8_hvCategory']

allCats = list(vr.colorDict.keys())

pTBinEdges = weightDict["bin_edges"]

for var in vr.allVars.keys():
    histogramList = []
    histogramLabels = []
    histogramColors = []
    binEdges = ut.getBin(vr.allVars,var)
    for catLabel in allCats[:5]:
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
    plt.legend()
    plt.yscale("log")
    plt.savefig("{}.png".format(var))
    
        
