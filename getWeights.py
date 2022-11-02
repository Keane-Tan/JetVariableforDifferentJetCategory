# use the t-channel environment to run this script
# we want to normalize the distributions by the pT distribution of the Q jets
import uproot as up
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.gridspec as gridspec
import mplhep as hep
import pandas as pd
import os
# importing custom libraries
import variables as var
import utility as ut

mpl.rc("font", family="serif", size=20)

def getBin(variables,varName):
    varDetail = variables[varName]
    return np.linspace(varDetail[2],varDetail[3]*1.001,varDetail[1])

def getWeights(JetsAK8_hvCategory,catLabel,QPtHist):
    catBranches = branches[JetsAK8_hvCategory == ut.hvCat_encode(catLabel)]
    hist,bin_edges = np.histogram(catBranches['jPtAK8'],bins=getBin(var.allVars,'jPtAK8'))
    return np.nan_to_num(np.array(QPtHist)/np.array(hist), nan=0.0, posinf=0.0, neginf=0.0)
    
fileName = "tree_SVJ_mMed-1000_mDark-20_rinv-0p3_alpha-peak_yukawa-1_NN.root"
f = up.open(fileName)
ftree = f['tree']
branches = ftree.arrays(list(var.allVars.keys()) + ['JetsAK8_hvCategory'],library="pd")
JetsAK8_hvCategory = branches['JetsAK8_hvCategory']
Qbranches = branches[JetsAK8_hvCategory == ut.hvCat_encode("Q_lD")]
QPtHist,bin_edges = np.histogram(Qbranches['jPtAK8'],bins=getBin(var.allVars,'jPtAK8'))

weightDict = {}
weightDict["bin_edges"] = bin_edges
for catLabel in var.colorDict.keys():
    weightDict[catLabel] = getWeights(JetsAK8_hvCategory,catLabel,QPtHist)
np.savez_compressed("weights.npz",**weightDict)
