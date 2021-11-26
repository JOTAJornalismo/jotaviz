import matplotlib as mpl


def plotconfig():
    figwidth = 6
    figheight =5
    fontsize0=14

    labelsize = fontsize0*1.1
    titlesize = fontsize0*1.1

    mpl.style.use('classic')
    mpl.rcParams.update({'font.size':fontsize0 })
    mpl.rcParams.update({'legend.fontsize':fontsize0 })# legend
    mpl.rcParams.update({'axes.titlesize':titlesize})       # Title
    mpl.rcParams.update({'axes.labelsize':labelsize})    # x,y,cbar labels
    mpl.rcParams.update({'figure.titlesize' :titlesize})
    mpl.rcParams.update({'xtick.labelsize':fontsize0 , 'ytick.labelsize':fontsize0,
                         'xtick.direction':'in',      'ytick.direction':'in',
                         'xtick.major.size':6,        'ytick.major.size':6})
    mpl.rcParams.update({'xtick.top':True,  'ytick.right':True})

    mpl.rcParams.update({'axes.formatter.use_mathtext':True})
    mpl.rcParams.update({'axes.formatter.limits':[-3,3]})
    mpl.rcParams.update({'axes.formatter.useoffset':False})   # no offset of axis

    mpl.rcParams.update({'figure.figsize':[figwidth,figheight]})
    mpl.rcParams.update({'savefig.bbox':'tight'})
    mpl.rcParams.update({'image.cmap':'jet'})

    mpl.rcParams.update({'lines.markeredgewidth':2,
                         'lines.markersize':6})

    #Legend
    mpl.rcParams.update({'legend.handletextpad':0.3,'legend.borderaxespad':0.1,
                         'legend.handlelength':1,'legend.labelspacing':0.2,'legend.borderpad':0.3})

    # To get sans-serif
    mpl.rcParams.update({'font.style':'normal'})
    mpl.rcParams.update({'font.family':'serif'})
    mpl.rcParams.update({'mathtext.fontset':'dejavuserif'})

if __name__ =="__main__":
    plotconfig()
