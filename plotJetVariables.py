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
import variables as var
import utility as ut

weights = np.load("weights.npz")
print(weights.files)
for stuff in weights.files:
    print(stuff)
    print(len(weights[stuff]))
    print(weights[stuff])
    print()
