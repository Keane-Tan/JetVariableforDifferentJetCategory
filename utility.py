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
    
def histMake(data,binEdge,weights=None,norm=True):
    data,bins = np.histogram(data, bins=binEdge, weights=weights, density=norm)
    bins = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
    binwidth = bins[1] - bins[0]
    pbins = np.append(bins,bins[-1]+binwidth)
    pdata = np.append(data,data[-1])
    return np.array(pbins),np.array(pdata)

def histplot(pdata,pbins,color,label,alpha=1.0,hatch=None,points=False,facecolorOn=True,ax=plt):
    if points:
        ax.plot(pbins[:-1],pdata[:-1],color=color,label=label,marker=".",linestyle="None")
    else:
        ax.step(pbins,pdata,where="post",color=color)
        if facecolorOn:
            facecolor=color
        else:
            facecolor="none"
        ax.fill_between(pbins,pdata, step="post", edgecolor=color, facecolor=facecolor, label=label, alpha=alpha, hatch=hatch)

def histMakePlot(data,binEdge,color,label,weights=None,alpha=1.0,hatch=None,points=False,facecolorOn=True,norm=True,ax=plt):
    pbins,pdata = histMake(data,binEdge,weights=weights,norm=norm)
    histplot(pdata,pbins,color,label,alpha=alpha,hatch=hatch,points=points,facecolorOn=facecolorOn,ax=ax)
    return pdata,pbins
