# LATEX
from cycler import cycler

available =['jotagray', 'jotagrey', 'jotawhite', 'jotaglass', 'jotadark', 'jotablack', 'academic']

jotagray = {

    # errorbar props
    'errorbar.capsize': 0.0,

     # Patches
    'patch.linewidth': 0.5,
    'patch.edgecolor': '#ebecf0',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,

    # Fonts
    'font.family': ['sans-serif'],
    'font.sans-serif': ['Roboto', 'Arial', 'DejaVu Sans'],
    'font.fantasy': ['xkcd', 'Humor Sans', 'Comic Sans MS'],  
    'font.monospace': ['DejaVu Sans Mono', 'Computer Modern Typewriter', 'Courier'],
    'font.serif': ['DejaVu Serif', 'Computer Modern Roman'], 
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 15.0,
    'text.color': '#222222',
    'mathtext.fontset': 'dejavuserif',
    'mathtext.default': 'rm',

    # Lines
    'lines.linewidth': 2.0,
    'lines.antialiased': True,
    'lines.marker': 'none', 
    'lines.markersize': 8.0,
    'lines.solid_capstyle': 'butt',
    'lines.dashed_pattern': [6.0, 6.0],
    'lines.dashdot_pattern': [3.0, 5.0, 1.0, 5.0],
    'lines.dotted_pattern': [1.0, 3.0],
    'lines.markeredgewidth': 2.0,
    'lines.markerfacecolor': 'auto',
    'lines.markeredgecolor': 'auto',

    # scatter props
    'scatter.marker': 'o',
    'markers.fillstyle': 'full', #'full' , ʼleft', 'right', 'bottom', 'top' , 'none' 

     # hist props
     'hist.bins': 10,

    # AXES
    # Documentation for cycler (https://matplotlib.org/cycler/),
    'axes.facecolor': '#ebecf0',
    'axes.edgecolor': '#ebecf0',
    'axes.linewidth': 4.0,
    'axes.titlesize': 26.0, # fontsize of the axes title
    'axes.titlepad': 20.0, # pad between axes and title in points
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'center',
    'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 18.0, # fontsize of the x any y labels
    'axes.labelpad': 5.0, # space between label and axis
    'axes.labelweight': 'normal',
    'axes.labelcolor': '#222222',
    'axes.axisbelow': True,
    'axes.autolimit_mode': 'round_numbers',
    'axes.unicode_minus': True,
    'axes.spines.left': False,
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.spines.bottom': False,
    # Use scientific notation
    'axes.formatter.min_exponent': 0,  # minimum exponent to format in scientific notation
    'axes.formatter.use_locale': True, 
    'axes.formatter.useoffset': True, # If True, the tick label formatter
                                      # will default to labeling ticks relative
                                      # to an offset when the data range is
                                      # small compared to the minimum absolute
                                      # value of the data.
    'axes.formatter.offset_threshold': 4, # When useoffset is True, the offset
                                          # will be used when it can remove
                                          # at least this number of significant
                                          # digits from tick labels.

    'axes.prop_cycle': cycler(
        color=[
            'tab:red',
            'tab:blue',
            'tab:green',
            'tab:orange',
            'tab:purple',
            'tab:brown',
            'tab:pink',
            'tab:gray',
            'tab:olive',
            'tab:cyan',
            'k',
        ]
    ),
     # Grid
    'axes.grid': True, # display grid or not
    'axes3d.grid': True, 
    'grid.color': 'k',
    'grid.alpha': 0.5,
    'grid.linewidth': 0.9,
    'grid.linestyle': ':',
    
     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 10.0, # major tick length in points
    'xtick.minor.size': 0.2, # minor tick length in points
    'xtick.major.width': 1.5,  # major tick width in points
    'xtick.minor.width': 0.5,  # minor tick width in points
    'xtick.major.pad': 6.0, # distance to major tick label in points
    'xtick.minor.pad': 3.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 20.0, # fontsize of the tick labels
    'xtick.direction': 'in',  # direction: in, out, or inout
    'xtick.color': '#333333',

    # Ticks Y
    'ytick.alignment': 'bottom',
    'ytick.major.size': 0.0,
    'ytick.minor.size': 0.0,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.5,
    'ytick.major.pad': 3.0,
    'ytick.minor.pad': 1.5,
    'ytick.minor.visible': False,
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 20.0,
    'ytick.color': '#333333',
    'ytick.direction': 'out',  # direction: in, out, or inout

    # Images
    'image.aspect': 'equal',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    'figure.figsize': [11.72, 9.72],
    'figure.facecolor': '#ebecf0',
    'figure.edgecolor': '#ebecf0',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.subplot.left': 0.177,
    'figure.subplot.right': 0.946,
    'figure.subplot.bottom': 0.156,
    'figure.subplot.top': 0.965,
    'figure.titlesize': 28.0, # size of the figure title (Figure.suptitle())
    'figure.titleweight': 'bold',  # weight of the figure title


    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': '#ebecf0',
    'savefig.edgecolor': '#ebecf0',
    'figure.constrained_layout.use': True,
    'pdf.fonttype': 3,  # Output Type 3 (Type3) or Type 42 (TrueType)
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': True,
    'legend.frameon': True,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 1,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,   # border whitespace in fontsize units
    'legend.markerscale': 1.5,  # the relative size of legend markers vs. original
    'legend.labelspacing': 0.3,  # the vertical space between the legend entries in fraction of fontsize
    'legend.columnspacing': 1.0, # the border between the axes and legend edge in fraction of fontsize
    'legend.borderaxespad': 0.5, # the border between the axes and legend edge in fraction of fontsize
    'legend.handlelength': 1.0,  # the length of the legend lines in fraction of fontsize
    'legend.handleheight': 0.7,  # the height of the legend handle in fraction of fontsize
    'legend.handletextpad': 0.5, # the space between the legend line and legend text in fraction of fontsize
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

     # Date
    'date.autoformatter.year': "%Y",
    'date.autoformatter.month': "%b",
    'date.autoformatter.day': "%d",
    'date.autoformatter.hour': "%H:%M",
    'date.autoformatter.minute': "%H:%M"
}


jotagrey = jotagray


jotawhite = {

    # errorbar props
    'errorbar.capsize': 0.0,

     # Patches
    'patch.linewidth': 0.5,
    'patch.edgecolor': 'white',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,

     # Fonts
    'font.family': ['sans-serif'],
    'font.sans-serif': ['Roboto', 'Arial', 'DejaVu Sans'],
    'font.fantasy': ['xkcd', 'Humor Sans', 'Comic Sans MS'],  
    'font.monospace': ['DejaVu Sans Mono', 'Computer Modern Typewriter', 'Courier'],
    'font.serif': ['DejaVu Serif', 'Computer Modern Roman'], 
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 15.0,
    'text.color': '#222222',
    'mathtext.fontset': 'dejavuserif',
    'mathtext.default': 'rm',

    # Lines
    'lines.linewidth': 2.0,
    'lines.antialiased': True,
    'lines.marker': 'none', 
    'lines.markersize': 8.0,
    'lines.solid_capstyle': 'butt',
    'lines.dashed_pattern': [6.0, 6.0],
    'lines.dashdot_pattern': [3.0, 5.0, 1.0, 5.0],
    'lines.dotted_pattern': [1.0, 3.0],
    'lines.markeredgewidth': 2.0,
    'lines.markerfacecolor': 'auto',
    'lines.markeredgecolor': 'auto',

    # scatter props
    'scatter.marker': 'o',
    'markers.fillstyle': 'full', #'full' , ʼleft', 'right', 'bottom', 'top' , 'none' 

     # hist props
     'hist.bins': 10,

    # Documentation for cycler (https://matplotlib.org/cycler/),
    # Axes
    'axes.facecolor': 'white',
    'axes.edgecolor': 'white',
    'axes.linewidth': 4.0,
    'axes.labelpad': 5.0,
    'axes.titlesize': 26.0,
    'axes.titlepad': 20.0,
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'center',
    'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 18.0,
    'axes.labelweight': 'normal',
    'axes.labelcolor': '#222222',
    'axes.axisbelow': True,
    'axes.autolimit_mode': 'round_numbers',
    'axes.unicode_minus': True,
    'axes.spines.left': False,
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.spines.bottom': False,
    # Use scientific notation
    'axes.formatter.min_exponent': 0,  # minimum exponent to format in scientific notation
    'axes.formatter.use_locale': True, 
    'axes.formatter.useoffset': True, # If True, the tick label formatter
                                      # will default to labeling ticks relative
                                      # to an offset when the data range is
                                      # small compared to the minimum absolute
                                      # value of the data.
    'axes.formatter.offset_threshold': 4, # When useoffset is True, the offset
                                          # will be used when it can remove
                                          # at least this number of significant
                                          # digits from tick labels.


    'axes.prop_cycle': cycler(
        color=[
            'tab:red',
            'tab:blue',
            'tab:green',
            'tab:orange',
            'tab:purple',
            'tab:brown',
            'tab:pink',
            'tab:gray',
            'tab:olive',
            'tab:cyan',
            'k',
        ]
    ),
    # Grid
    'axes.grid': True,
    'axes3d.grid': True,
    'grid.color': 'k',
    'grid.alpha': 0.5,
    'grid.linewidth': 0.7,
    'grid.linestyle': ':',

     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 10.0, # major tick length in points
    'xtick.minor.size': 0.2, # minor tick length in points
    'xtick.major.width': 1.5,  # major tick width in points
    'xtick.minor.width': 0.5,  # minor tick width in points
    'xtick.major.pad': 6.0, # distance to major tick label in points
    'xtick.minor.pad': 3.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 20.0, # fontsize of the tick labels
    'xtick.direction': 'in',  # direction: in, out, or inout
    'xtick.color': '#333333',

    # Ticks Y
    'ytick.alignment': 'center',
    'ytick.major.size': 0.0,
    'ytick.minor.size': 0.0,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.5,
    'ytick.major.pad': 3.0,
    'ytick.minor.pad': 1.5,
    'ytick.minor.visible': False,
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 20.0,
    'ytick.color': '#333333',
    'ytick.direction': 'out',  # direction: in, out, or inout

    # Images
    'image.aspect': 'equal',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    'figure.figsize': [11.72, 9.72],
    'figure.facecolor': 'white',
    'figure.edgecolor': 'white',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.subplot.left': 0.177,
    'figure.subplot.right': 0.946,
    'figure.subplot.bottom': 0.156,
    'figure.subplot.top': 0.965,
    'figure.titlesize': 28.0,
    'figure.titleweight': 'bold',

    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': 'white',
    'savefig.edgecolor': 'white',
    'figure.constrained_layout.use': True,
    'pdf.fonttype': 3,  # Output Type 3 (Type3) or Type 42 (TrueType)
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': True,
    'legend.frameon': True,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 1,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,   # border whitespace in fontsize units
    'legend.markerscale': 1.0,  # the relative size of legend markers vs. original
    'legend.labelspacing': 0.3,  # the vertical space between the legend entries in fraction of fontsize
    'legend.columnspacing': 0.5, # the border between the axes and legend edge in fraction of fontsize
    'legend.borderaxespad': 0.5, # the border between the axes and legend edge in fraction of fontsize
    'legend.handlelength': 0.5,  # the length of the legend lines in fraction of fontsize
    'legend.handleheight': 0.5,  # the height of the legend handle in fraction of fontsize
    'legend.handletextpad': 0.5, # the space between the legend line and legend text in fraction of fontsize
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

    'boxplot.boxprops.color': '#555555',
    'boxplot.capprops.color': '#555555',
    'boxplot.flierprops.color': '#555555',
    'boxplot.flierprops.markeredgecolor': '#555555',
    'boxplot.whiskerprops.color': '#555555',

    # Date
    'date.autoformatter.year': "%Y",
    'date.autoformatter.month': "%b",
    'date.autoformatter.day': "%d",
    'date.autoformatter.hour': "%H:%M",
    'date.autoformatter.minute': "%H:%M"
}





jotaglass = {

    # errorbar props
    'errorbar.capsize': 0.0,

     # Patches
    'patch.linewidth': 0.5,
    'patch.edgecolor': 'none',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,

     # Fonts
    'font.family': ['sans-serif'],
    'font.sans-serif': ['Roboto', 'Arial', 'DejaVu Sans'],
    'font.fantasy': ['xkcd', 'Humor Sans', 'Comic Sans MS'],  
    'font.monospace': ['DejaVu Sans Mono', 'Computer Modern Typewriter', 'Courier'],
    'font.serif': ['DejaVu Serif', 'Computer Modern Roman'], 
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 15.0,
    'text.color': '#222222',
    'mathtext.fontset': 'dejavuserif',
    'mathtext.default': 'rm',
 
    # Lines
    'lines.linewidth': 2.0,
    'lines.antialiased': True,
    'lines.marker': 'none', 
    'lines.markersize': 8.0,
    'lines.solid_capstyle': 'butt',
    'lines.dashed_pattern': [6.0, 6.0],
    'lines.dashdot_pattern': [3.0, 5.0, 1.0, 5.0],
    'lines.dotted_pattern': [1.0, 3.0],
    'lines.markeredgewidth': 2.0,
    'lines.markerfacecolor': 'auto',
    'lines.markeredgecolor': 'auto',

    # scatter props
    'scatter.marker': 'o',
    'markers.fillstyle': 'full', #'full' , ʼleft', 'right', 'bottom', 'top' , 'none' 

     # hist props
     'hist.bins': 10,

    # Documentation for cycler (https://matplotlib.org/cycler/),
    # Axes
    'axes.facecolor': 'white',
    'axes.edgecolor': 'white',
    'axes.linewidth': 4.0,
    'axes.labelpad': 5.0,
    'axes.titlesize': 26.0,
    'axes.titlepad': 20.0,
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'center',
    'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 18.0,
    'axes.labelweight': 'normal',
    'axes.labelcolor': '#222222',
    'axes.axisbelow': True,
    'axes.autolimit_mode': 'round_numbers',
    'axes.unicode_minus': True,
    'axes.spines.left': False,
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.spines.bottom': False,
    # Use scientific notation
    'axes.formatter.min_exponent': 0,  # minimum exponent to format in scientific notation
    'axes.formatter.use_locale': True, 
    'axes.formatter.useoffset': True, # If True, the tick label formatter
                                      # will default to labeling ticks relative
                                      # to an offset when the data range is
                                      # small compared to the minimum absolute
                                      # value of the data.
    'axes.formatter.offset_threshold': 4, # When useoffset is True, the offset
                                          # will be used when it can remove
                                          # at least this number of significant
                                          # digits from tick labels.


    'axes.prop_cycle': cycler(
        color=[
            'tab:red',
            'tab:blue',
            'tab:green',
            'tab:orange',
            'tab:purple',
            'tab:brown',
            'tab:pink',
            'tab:gray',
            'tab:olive',
            'tab:cyan',
            'k',
        ]
    ),
    # Grid
    'axes.grid': True,
    'axes3d.grid': True,
    'grid.color': 'k',
    'grid.alpha': 0.5,
    'grid.linewidth': 0.7,
    'grid.linestyle': ':',

     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 10.0, # major tick length in points
    'xtick.minor.size': 0.2, # minor tick length in points
    'xtick.major.width': 1.5,  # major tick width in points
    'xtick.minor.width': 0.5,  # minor tick width in points
    'xtick.major.pad': 6.0, # distance to major tick label in points
    'xtick.minor.pad': 3.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 20.0, # fontsize of the tick labels
    'xtick.direction': 'in',  # direction: in, out, or inout
    'xtick.color': '#333333',

    # Ticks Y
    'ytick.alignment': 'center',
    'ytick.major.size': 0.0,
    'ytick.minor.size': 0.0,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.5,
    'ytick.major.pad': 3.0,
    'ytick.minor.pad': 1.5,
    'ytick.minor.visible': False,
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 20.0,
    'ytick.color': '#333333',
    'ytick.direction': 'out',  # direction: in, out, or inout

     # Images
    'image.aspect': 'equal',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    'figure.figsize': [11.72, 9.72],
    'figure.facecolor': 'white',
    'figure.edgecolor': 'white',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.subplot.left': 0.177,
    'figure.subplot.right': 0.946,
    'figure.subplot.bottom': 0.156,
    'figure.subplot.top': 0.965,
    'figure.titlesize': 28.0,
    'figure.titleweight': 'bold',

    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': 'none',
    'savefig.edgecolor': 'none',
    'savefig.transparent': True,
    'figure.constrained_layout.use': True,
    'pdf.fonttype': 3,  # Output Type 3 (Type3) or Type 42 (TrueType)
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': True,
    'legend.frameon': True,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 1,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,  
    'legend.markerscale': 1.0,  
    'legend.labelspacing': 0.3, 
    'legend.columnspacing': 0.5, 
    'legend.borderaxespad': 0.5,
    'legend.handlelength': 0.5, 
    'legend.handleheight': 0.5, 
    'legend.handletextpad': 0.5,
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

    'boxplot.boxprops.color': '#555555',
    'boxplot.capprops.color': '#555555',
    'boxplot.flierprops.color': '#555555',
    'boxplot.flierprops.markeredgecolor': '#555555',
    'boxplot.whiskerprops.color': '#555555',

    # Date
    'date.autoformatter.year': "%Y",
    'date.autoformatter.month': "%b",
    'date.autoformatter.day': "%d",
    'date.autoformatter.hour': "%H:%M",
    'date.autoformatter.minute': "%H:%M"
}




jotablack = {

    # errorbar props
    'errorbar.capsize': 0.0,

     # Patches
    'patch.linewidth': 0.0,
    'patch.edgecolor': 'black',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,

     # Fonts
    'font.family': ['sans-serif'],
    'font.sans-serif': ['Roboto', 'Arial', 'DejaVu Sans'],
    'font.fantasy': ['xkcd', 'Humor Sans', 'Comic Sans MS'],  
    'font.monospace': ['DejaVu Sans Mono', 'Computer Modern Typewriter', 'Courier'],
    'font.serif': ['DejaVu Serif', 'Computer Modern Roman'], 
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 15.0,
    'text.color': 'white',
    'mathtext.fontset': 'dejavuserif',
    'mathtext.default': 'rm',
 
    # Lines
    'lines.color': 'white',
    'lines.linewidth': 2.0,
    'lines.antialiased': True,
    'lines.marker': 'none', 
    'lines.markersize': 8.0,
    'lines.solid_capstyle': 'butt',
    'lines.dashed_pattern': [6.0, 6.0],
    'lines.dashdot_pattern': [3.0, 5.0, 1.0, 5.0],
    'lines.dotted_pattern': [1.0, 3.0],
    'lines.markeredgewidth': 0.8,
    'lines.markerfacecolor': 'none',
    'lines.markeredgecolor': 'auto',

    # scatter props
    'scatter.marker': 'o',
    'markers.fillstyle': 'full', #'full' , ʼleft', 'right', 'bottom', 'top' , 'none' 

     # hist props
     'hist.bins': 10,

    # Documentation for cycler (https://matplotlib.org/cycler/),
    # Axes
    'axes.facecolor': 'black',
    'axes.edgecolor': 'white',
    'axes.linewidth': 4.0,
    'axes.labelpad': 5.0,
    'axes.titlesize': 26.0,
    'axes.titlepad': 20.0,
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'center',
    'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 18.0,
    'axes.labelweight': 'normal',
    'axes.labelcolor': 'white',
    'axes.axisbelow': True,
    'axes.autolimit_mode': 'round_numbers',
    'axes.unicode_minus': True,
    'axes.spines.left': False,
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.spines.bottom': False,
    # Use scientific notation
    'axes.formatter.min_exponent': 0,  # minimum exponent to format in scientific notation
    'axes.formatter.use_locale': True, 
    'axes.formatter.useoffset': True, # If True, the tick label formatter
                                      # will default to labeling ticks relative
                                      # to an offset when the data range is
                                      # small compared to the minimum absolute
                                      # value of the data.
    'axes.formatter.offset_threshold': 4, # When useoffset is True, the offset
                                          # will be used when it can remove
                                          # at least this number of significant
                                          # digits from tick labels.


    'axes.prop_cycle': cycler(
        color=[
            'tab:red',
            'tab:blue',
            'tab:green',
            'tab:orange',
            'tab:purple',
            'tab:brown',
            'tab:pink',
            'tab:gray',
            'tab:olive',
            'tab:cyan',
            'k',
        ]
    ),
    # Grid
    'axes.grid': True,
    'axes3d.grid': True,
    'grid.color': 'white',
    'grid.alpha': 0.5,
    'grid.linewidth': 0.8,
    'grid.linestyle': ':',

     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 10.0, # major tick length in points
    'xtick.minor.size': 0.2, # minor tick length in points
    'xtick.major.width': 1.5,  # major tick width in points
    'xtick.minor.width': 0.5,  # minor tick width in points
    'xtick.major.pad': 6.0, # distance to major tick label in points
    'xtick.minor.pad': 3.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 20.0, # fontsize of the tick labels
    'xtick.direction': 'in',  # direction: in, out, or inout
    'xtick.color': 'white',

    # Ticks Y
    'ytick.alignment': 'center',
    'ytick.major.size': 0.0,
    'ytick.minor.size': 0.0,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.5,
    'ytick.major.pad': 3.0,
    'ytick.minor.pad': 1.5,
    'ytick.minor.visible': False,
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 20.0,
    'ytick.color': 'white',
    'ytick.direction': 'out',  # direction: in, out, or inout

     # Images
    'image.aspect': 'equal',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    'figure.figsize': [11.72, 9.72],
    'figure.facecolor': 'black',
    'figure.edgecolor': 'black',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.subplot.left': 0.177,
    'figure.subplot.right': 0.946,
    'figure.subplot.bottom': 0.156,
    'figure.subplot.top': 0.965,
    'figure.titlesize': 28.0,
    'figure.titleweight': 'bold',

    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': 'black',
    'savefig.edgecolor': 'black',
    'figure.constrained_layout.use': True,
    'pdf.fonttype': 3,  # Output Type 3 (Type3) or Type 42 (TrueType)
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': True,
    'legend.frameon': True,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 1,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,  
    'legend.markerscale': 1.0,  
    'legend.labelspacing': 0.3, 
    'legend.columnspacing': 0.5, 
    'legend.borderaxespad': 0.5,
    'legend.handlelength': 0.5, 
    'legend.handleheight': 0.5, 
    'legend.handletextpad': 0.5,
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

    'boxplot.boxprops.color': 'white',
    'boxplot.capprops.color': 'white',
    'boxplot.flierprops.color': 'white',
    'boxplot.flierprops.markeredgecolor': 'white',
    'boxplot.whiskerprops.color': 'white',

    # Date
    'date.autoformatter.year': "%Y",
    'date.autoformatter.month': "%b",
    'date.autoformatter.day': "%d",
    'date.autoformatter.hour': "%H:%M",
    'date.autoformatter.minute': "%H:%M"
}




jotadark = {

    # errorbar props
    'errorbar.capsize': 0.0,

     # Patches
    'patch.linewidth': 0.0,
    'patch.edgecolor': '#212946',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,

     # Fonts
     # font color: very light grey
    'font.family': ['sans-serif'],
    'font.sans-serif': ['Roboto', 'Arial', 'DejaVu Sans'],
    'font.fantasy': ['xkcd', 'Humor Sans', 'Comic Sans MS'],  
    'font.monospace': ['DejaVu Sans Mono', 'Computer Modern Typewriter', 'Courier'],
    'font.serif': ['DejaVu Serif', 'Computer Modern Roman'], 
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 15.0,
    'text.color': '#f1f1f1',
    'mathtext.fontset': 'dejavuserif',
    'mathtext.default': 'rm',
 
    # Lines
    'lines.color': '#f1f1f1',
    'lines.linewidth': 2.0,
    'lines.antialiased': True,
    'lines.marker': 'none', 
    'lines.markersize': 8.0,
    'lines.solid_capstyle': 'butt',
    'lines.dashed_pattern': [6.0, 6.0],
    'lines.dashdot_pattern': [3.0, 5.0, 1.0, 5.0],
    'lines.dotted_pattern': [1.0, 3.0],
    'lines.markeredgewidth': 0.8,
    'lines.markerfacecolor': 'none',
    'lines.markeredgecolor': 'auto',

    # scatter props
    'scatter.marker': 'o',
    'markers.fillstyle': 'full', #'full' , ʼleft', 'right', 'bottom', 'top' , 'none' 

     # hist props
     'hist.bins': 10,

    # Documentation for cycler (https://matplotlib.org/cycler/),
    # Axes
    'axes.facecolor': '#212946',
    'axes.edgecolor': '#f1f1f1',
    'axes.linewidth': 4.0,
    'axes.labelpad': 5.0,
    'axes.titlesize': 26.0,
    'axes.titlepad': 20.0,
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'center',
    'axes3d.grid': True,
    'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 18.0,
    'axes.labelweight': 'normal',
    'axes.labelcolor': '#f1f1f1',
    'axes.axisbelow': True,
    'axes.autolimit_mode': 'round_numbers',
    'axes.unicode_minus': True,
    'axes.spines.left': False,
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.spines.bottom': False,    
    # Use scientific notation
    'axes.formatter.min_exponent': 0,  # minimum exponent to format in scientific notation
    'axes.formatter.use_locale': True, 
    'axes.formatter.useoffset': True, # If True, the tick label formatter
                                      # will default to labeling ticks relative
                                      # to an offset when the data range is
                                      # small compared to the minimum absolute
                                      # value of the data.
    'axes.formatter.offset_threshold': 4, # When useoffset is True, the offset
                                          # will be used when it can remove
                                          # at least this number of significant
                                          # digits from tick labels.


    'axes.prop_cycle': cycler(
        color=[
            'tab:red',
            'tab:blue',
            'tab:green',
            'tab:orange',
            'tab:purple',
            'tab:brown',
            'tab:pink',
            'tab:gray',
            'tab:olive',
            'tab:cyan',
            'k',
        ]
    ),
    # Grid
    # grid: bluish dark grey, slightly lighter than background
    'axes.grid': True,
    'grid.color': '#f1f1f1',
    'grid.alpha': 0.5,
    'grid.linewidth': 0.8,
    'grid.linestyle': ':',

     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 10.0, # major tick length in points
    'xtick.minor.size': 0.2, # minor tick length in points
    'xtick.major.width': 1.5,  # major tick width in points
    'xtick.minor.width': 0.5,  # minor tick width in points
    'xtick.major.pad': 6.0, # distance to major tick label in points
    'xtick.minor.pad': 3.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 20.0, # fontsize of the tick labels
    'xtick.direction': 'in',  # direction: in, out, or inout
    'xtick.color': '#f1f1f1',

    # Ticks Y
    'ytick.alignment': 'center',
    'ytick.major.size': 0.0,
    'ytick.minor.size': 0.0,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.5,
    'ytick.major.pad': 3.0,
    'ytick.minor.pad': 1.5,
    'ytick.minor.visible': False,
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 20.0,
    'ytick.color': '#f1f1f1',
    'ytick.direction': 'out',  # direction: in, out, or inout

     # Images
    'image.aspect': 'equal',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    # background: bluish dark grey
    'figure.figsize': [11.72, 9.72],
    'figure.facecolor': '#212946',
    'figure.edgecolor': '#212946',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.subplot.left': 0.177,
    'figure.subplot.right': 0.946,
    'figure.subplot.bottom': 0.156,
    'figure.subplot.top': 0.965,
    'figure.titlesize': 28.0,
    'figure.titleweight': 'bold',

    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': '#212946',
    'savefig.edgecolor': '#212946',
    'figure.constrained_layout.use': True,
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': True,
    'legend.frameon': True,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 1,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,  
    'legend.markerscale': 1.0,  
    'legend.labelspacing': 0.3, 
    'legend.columnspacing': 0.5, 
    'legend.borderaxespad': 0.5,
    'legend.handlelength': 0.5, 
    'legend.handleheight': 0.5, 
    'legend.handletextpad': 0.5,
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

    'boxplot.boxprops.color': 'white',
    'boxplot.capprops.color': 'white',
    'boxplot.flierprops.color': 'white',
    'boxplot.flierprops.markeredgecolor': 'white',
    'boxplot.whiskerprops.color': 'white',

    # Date
    'date.autoformatter.year': "%Y",
    'date.autoformatter.month': "%b",
    'date.autoformatter.day': "%d",
    'date.autoformatter.hour': "%H:%M",
    'date.autoformatter.minute': "%H:%M"
}


academic = {
    "text.usetex": True,
    # "text.latex.preamble": "\usepackage\{amsmath\}",
    "mathtext.fontset": "dejavusans",
    "mathtext.fallback": "cm",
    "mathtext.default": "regular",
    # FONT
    "font.size": 15,
    "font.family": "cm",
    # AXES
    # Documentation for cycler (https://matplotlib.org/cycler/),
    "axes.axisbelow": "line",
    "axes.prop_cycle": cycler(
        color=[
            "tab:red",
            "tab:blue",
            "tab:green",
            "tab:orange",
            "tab:purple",
            "tab:brown",
            "tab:pink",
            "tab:gray",
            "tab:olive",
            "tab:cyan",
            "k",
        ]
    ),
    # GRID
    "axes.grid": False,
    "grid.linewidth": 0.6,
    "grid.alpha": 0.5,
    "grid.linestyle": "--",
    # TICKS,
    "xtick.top": False,
    "xtick.direction": "in",
    "xtick.minor.visible": False,
    "xtick.major.size": 6.0,
    "xtick.minor.size": 4.0,
    "ytick.right": False,
    "ytick.direction": "in",
    "ytick.minor.visible": False,
    "ytick.major.size": 6.0,
    "ytick.minor.size": 4.0,
    # FIGURE,
    "figure.constrained_layout.use": True,
}