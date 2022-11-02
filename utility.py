import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.gridspec as gridspec

def decode(hvCat,nlabel,clabel,catList):
    if hvCat >= nlabel:
        hvCat -= nlabel
        catList.append(clabel)
    return hvCat

def hvCat_decode(hvCat):
    catList = []
    hvCat = decode(hvCat,16,"SMM",catList)
    hvCat = decode(hvCat,8,"QM",catList)
    hvCat = decode(hvCat,4,"G",catList)
    hvCat = decode(hvCat,2,"Q",catList)
    hvCat = decode(hvCat,1,"lD",catList)
    return catList

def hvCat_encode(string):
    catList = string.split("_")
    code = 0
    if "lD" in catList: code += 1
    if "Q" in catList: code += 2
    if "G" in catList: code += 4
    if "QM" in catList: code += 8
    if "SMM" in catList: code += 16
    return code
    
def getBin(variables,varName):
    varDetail = variables[varName]
    return np.linspace(varDetail[2],varDetail[3]*1.001,varDetail[1])
