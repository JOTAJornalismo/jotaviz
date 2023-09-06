# LATEX
from cycler import cycler

available =['jotagray', 'jotagrey', 'jotawhite', 'jotaglass', 'jotadark', 'jotablack', 'jotavoid', 'jotaneon']

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
    'font.family': 'sans-serif',
    'font.sans-serif': [
        'Roboto',
        'Helvetica',
        'Computer Modern Sans Serif',
        'DejaVu Sans'
        ],
    'font.fantasy': [
        'xkcd',
        'Humor Sans',
        'Comic Sans MS'
        ],  
    'font.monospace': [
        'DejaVu Sans Mono',
        'Computer Modern Typewriter',
        'Courier'
        ],
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 13.0,
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
    'axes.titlesize': 18.0, # fontsize of the axes title
    'axes.titlepad': 10.0, # pad between axes and title in points
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'left',
    #'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    #'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 14.0, # fontsize of the x any y labels
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
    'grid.color': '#888888',
    'grid.alpha': 0.85, 
    'grid.linewidth': 0.85,
    'grid.linestyle': '-',
    
     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 3.0, # major tick length in points
    'xtick.minor.size': 0.5, # minor tick length in points
    'xtick.major.width': 1.0,  # major tick width in points
    'xtick.minor.width': 0.75,  # minor tick width in points
    'xtick.major.pad': 2.0, # distance to major tick label in points
    'xtick.minor.pad': 2.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 14.0, # fontsize of the tick labels
    'xtick.direction': 'inout',  # direction: in, out, or inout
    'xtick.color': '#555555',

    # Ticks Y
    'ytick.alignment': 'bottom',
    'ytick.major.size': 3.0,
    'ytick.minor.size': 0.5,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.75,
    'ytick.major.pad': 2.0,
    'ytick.minor.pad': 2.0,
    'ytick.minor.visible': False, 
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 14.0,
    'ytick.color': '#555555',
    'ytick.direction': 'inout',  # direction: in, out, or inout

    # Images
    'image.aspect': 'auto',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    # figure(figsize=(1,1)) would create an inch-by-inch image, which would be 100-by-100 pixels unless you also give a different dpi argument.
    # figsize = [6.4 4.8] PNG 640x480
    'figure.figsize': [6.4, 6.4],
    'figure.facecolor': '#ebecf0',
    'figure.edgecolor': '#ebecf0',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.titlesize': 20.0, # size of the figure title (Figure.suptitle())
    'figure.titleweight': 'bold',  # weight of the figure title


    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': '#ebecf0',
    'savefig.edgecolor': '#ebecf0',
    'figure.constrained_layout.use': True,
    'pdf.fonttype': 42,  # Output Type 3 (Type3) or Type 42 (TrueType)
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': True,
    'legend.frameon': False,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 3,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,   # border whitespace in fontsize units
    'legend.markerscale': 1.5,  # the relative size of legend markers vs. original
    'legend.labelspacing': 0.3,  # the vertical space between the legend entries in fraction of fontsize
    'legend.columnspacing': 1.0, # the border between the axes and legend edge in fraction of fontsize
    'legend.borderaxespad': 0.5, # the border between the axes and legend edge in fraction of fontsize
    'legend.handlelength': 1.4,  # the length of the legend lines in fraction of fontsize
    'legend.handleheight': 0.85,  # the height of the legend handle in fraction of fontsize
    'legend.handletextpad': 0.5, # the space between the legend line and legend text in fraction of fontsize
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

     # Boxplot parans
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

jotagrey = jotagray



jotawhite = {
    # errorbar props
    'errorbar.capsize': 0.0,

     # Patches
    'patch.linewidth': 0.5,
    'patch.edgecolor': '#ffffff',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,

    # Fonts
    'font.family': 'sans-serif',
    'font.sans-serif': [
        'Roboto',
        'Helvetica',
        'Computer Modern Sans Serif',
        'DejaVu Sans'
        ],
    'font.fantasy': [
        'xkcd',
        'Humor Sans',
        'Comic Sans MS'
        ],  
    'font.monospace': [
        'DejaVu Sans Mono',
        'Computer Modern Typewriter',
        'Courier'
        ],
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 13.0,
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
    'axes.facecolor': '#ffffff',
    'axes.edgecolor': '#ffffff',
    'axes.linewidth': 4.0,
    'axes.titlesize': 18.0, # fontsize of the axes title
    'axes.titlepad': 10.0, # pad between axes and title in points
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'left',
    #'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    #'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 14.0, # fontsize of the x any y labels
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
    'grid.color': '#888888',
    'grid.alpha': 0.85,
    'grid.linewidth': 0.85,
    'grid.linestyle': '-',
    
     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 3.0, # major tick length in points
    'xtick.minor.size': 0.5, # minor tick length in points
    'xtick.major.width': 1.0,  # major tick width in points
    'xtick.minor.width': 0.75,  # minor tick width in points
    'xtick.major.pad': 2.0, # distance to major tick label in points
    'xtick.minor.pad': 2.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 14.0, # fontsize of the tick labels
    'xtick.direction': 'inout',  # direction: in, out, or inout
    'xtick.color': '#555555',

    # Ticks Y
    'ytick.alignment': 'bottom',
    'ytick.major.size': 3.0,
    'ytick.minor.size': 0.5,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.75,
    'ytick.major.pad': 2.0,
    'ytick.minor.pad': 2.0,
    'ytick.minor.visible': False, 
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 14.0,
    'ytick.color': '#555555',
    'ytick.direction': 'out',  # direction: in, out, or inout

    # Images
    'image.aspect': 'auto',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    # figure(figsize=(1,1)) would create an inch-by-inch image, which would be 100-by-100 pixels unless you also give a different dpi argument.
    # figsize = [6.4 4.8] PNG 640x480
    'figure.figsize': [6.4, 6.4],
    'figure.facecolor': '#ffffff',
    'figure.edgecolor': '#ffffff',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.titlesize': 20.0, # size of the figure title (Figure.suptitle())
    'figure.titleweight': 'bold',  # weight of the figure title


    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': '#ffffff',
    'savefig.edgecolor': '#ffffff',
    'figure.constrained_layout.use': True,
    'pdf.fonttype': 42,  # Output Type 3 (Type3) or Type 42 (TrueType)
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': True,
    'legend.frameon': False,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 3,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,   # border whitespace in fontsize units
    'legend.markerscale': 1.5,  # the relative size of legend markers vs. original
    'legend.labelspacing': 0.3,  # the vertical space between the legend entries in fraction of fontsize
    'legend.columnspacing': 1.0, # the border between the axes and legend edge in fraction of fontsize
    'legend.borderaxespad': 0.5, # the border between the axes and legend edge in fraction of fontsize
    'legend.handlelength': 1.4,  # the length of the legend lines in fraction of fontsize
    'legend.handleheight': 0.85,  # the height of the legend handle in fraction of fontsize
    'legend.handletextpad': 0.5, # the space between the legend line and legend text in fraction of fontsize
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

     # Boxplot parans
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
    'font.family': 'sans-serif',
    'font.sans-serif': [
        'Roboto',
        'Helvetica',
        'Computer Modern Sans Serif',
        'DejaVu Sans'
        ],
    'font.fantasy': [
        'xkcd',
        'Humor Sans',
        'Comic Sans MS'
        ],  
    'font.monospace': [
        'DejaVu Sans Mono',
        'Computer Modern Typewriter',
        'Courier'
        ],
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 13.0,
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
    'axes.facecolor': '#ffffff',
    'axes.edgecolor': '#ffffff',
    'axes.linewidth': 4.0,
    'axes.titlesize': 18.0, # fontsize of the axes title
    'axes.titlepad': 10.0, # pad between axes and title in points
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'left',
    #'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    #'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 14.0, # fontsize of the x any y labels
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
    'grid.color': '#888888',
    'grid.alpha': 0.85,
    'grid.linewidth': 0.85,
    'grid.linestyle': '-',
    
     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 3.0, # major tick length in points
    'xtick.minor.size': 0.5, # minor tick length in points
    'xtick.major.width': 1.0,  # major tick width in points
    'xtick.minor.width': 0.75,  # minor tick width in points
    'xtick.major.pad': 2.0, # distance to major tick label in points
    'xtick.minor.pad': 2.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 14.0, # fontsize of the tick labels
    'xtick.direction': 'inout',  # direction: in, out, or inout
    'xtick.color': '#555555',

    # Ticks Y
    'ytick.alignment': 'bottom',
    'ytick.major.size': 3.0,
    'ytick.minor.size': 0.5,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.75,
    'ytick.major.pad': 2.0,
    'ytick.minor.pad': 2.0,
    'ytick.minor.visible': False, 
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 14.0,
    'ytick.color': '#555555',
    'ytick.direction': 'inout',  # direction: in, out, or inout

    # Images
    'image.aspect': 'auto',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    # figure(figsize=(1,1)) would create an inch-by-inch image, which would be 100-by-100 pixels unless you also give a different dpi argument.
    # figsize = [6.4 4.8] PNG 640x480
    'figure.figsize': [6.4, 6.4],
    'figure.facecolor': '#ffffff',
    'figure.edgecolor': '#ffffff',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.titlesize': 20.0, # size of the figure title (Figure.suptitle())
    'figure.titleweight': 'bold',  # weight of the figure title


    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': 'none',
    'savefig.edgecolor': 'none',
    'figure.constrained_layout.use': True,
    'pdf.fonttype': 42,  # Output Type 3 (Type3) or Type 42 (TrueType)
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': True,
    'legend.frameon': False,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 3,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,   # border whitespace in fontsize units
    'legend.markerscale': 1.5,  # the relative size of legend markers vs. original
    'legend.labelspacing': 0.3,  # the vertical space between the legend entries in fraction of fontsize
    'legend.columnspacing': 1.0, # the border between the axes and legend edge in fraction of fontsize
    'legend.borderaxespad': 0.5, # the border between the axes and legend edge in fraction of fontsize
    'legend.handlelength': 1.4,  # the length of the legend lines in fraction of fontsize
    'legend.handleheight': 0.85,  # the height of the legend handle in fraction of fontsize
    'legend.handletextpad': 0.5, # the space between the legend line and legend text in fraction of fontsize
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

     # Boxplot parans
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
    'patch.linewidth': 0.5,
    'patch.edgecolor': '#333333',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,

    # Fonts
    'font.family': 'sans-serif',
    'font.sans-serif': [
        'Roboto',
        'Helvetica',
        'Computer Modern Sans Serif',
        'DejaVu Sans'
        ],
    'font.fantasy': [
        'xkcd',
        'Humor Sans',
        'Comic Sans MS'
        ],  
    'font.monospace': [
        'DejaVu Sans Mono',
        'Computer Modern Typewriter',
        'Courier'
        ],
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 13.0,
    'text.color': '#d9d9d9',
    'mathtext.fontset': 'dejavuserif',
    'mathtext.default': 'rm',

    # Lines
    'lines.linewidth': 2.0,
    'lines.antialiased': True,
    'lines.marker': 'none',
    'lines.color': '#d9d9d9', 
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
    'axes.facecolor': '#333333',
    'axes.edgecolor': '#d9d9d9',
    'axes.linewidth': 4.0,
    'axes.titlesize': 18.0, # fontsize of the axes title
    'axes.titlepad': 10.0, # pad between axes and title in points
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'left',
    #'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    #'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 14.0, # fontsize of the x any y labels
    'axes.labelpad': 5.0, # space between label and axis
    'axes.labelweight': 'normal',
    'axes.labelcolor': '#d9d9d9',
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
    'grid.color': '#d9d9d9',
    'grid.alpha': 0.85,
    'grid.linewidth': 0.85,
    'grid.linestyle': '-',
    
     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 3.0, # major tick length in points
    'xtick.minor.size': 0.5, # minor tick length in points
    'xtick.major.width': 1.0,  # major tick width in points
    'xtick.minor.width': 0.75,  # minor tick width in points
    'xtick.major.pad': 2.0, # distance to major tick label in points
    'xtick.minor.pad': 2.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 14.0, # fontsize of the tick labels
    'xtick.direction': 'inout',  # direction: in, out, or inout
    'xtick.color': '#d9d9d9',

    # Ticks Y
    'ytick.alignment': 'bottom',
    'ytick.major.size': 3.0,
    'ytick.minor.size': 0.5,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.75,
    'ytick.major.pad': 2.0,
    'ytick.minor.pad': 2.0,
    'ytick.minor.visible': False, 
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 14.0,
    'ytick.color': '#d9d9d9',
    'ytick.direction': 'inout',  # direction: in, out, or inout

    # Images
    'image.aspect': 'auto',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    # figure(figsize=(1,1)) would create an inch-by-inch image, which would be 100-by-100 pixels unless you also give a different dpi argument.
    # figsize = [6.4 4.8] PNG 640x480
    'figure.figsize': [6.4, 6.4],
    'figure.facecolor': '#333333',
    'figure.edgecolor': '#333333',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.titlesize': 20.0, # size of the figure title (Figure.suptitle())
    'figure.titleweight': 'bold',  # weight of the figure title


    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': '#333333',
    'savefig.edgecolor': '#333333',
    'figure.constrained_layout.use': True,
    'pdf.fonttype': 42,  # Output Type 3 (Type3) or Type 42 (TrueType)
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': False,
    'legend.frameon': False,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 3,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,   # border whitespace in fontsize units
    'legend.markerscale': 1.5,  # the relative size of legend markers vs. original
    'legend.labelspacing': 0.3,  # the vertical space between the legend entries in fraction of fontsize
    'legend.columnspacing': 1.0, # the border between the axes and legend edge in fraction of fontsize
    'legend.borderaxespad': 0.5, # the border between the axes and legend edge in fraction of fontsize
    'legend.handlelength': 1.4,  # the length of the legend lines in fraction of fontsize
    'legend.handleheight': 0.85,  # the height of the legend handle in fraction of fontsize
    'legend.handletextpad': 0.5, # the space between the legend line and legend text in fraction of fontsize
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

     # Boxplot parans
    'boxplot.boxprops.color': '#d9d9d9',
    'boxplot.capprops.color': '#d9d9d9',
    'boxplot.flierprops.color': '#d9d9d9',
    'boxplot.flierprops.markeredgecolor': '#d9d9d9',
    'boxplot.whiskerprops.color': '#d9d9d9',

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
    'patch.linewidth': 0.5,
    'patch.edgecolor': '#212946',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,

    # Fonts
    'font.family': 'sans-serif',
    'font.sans-serif': [
        'Roboto',
        'Helvetica',
        'Computer Modern Sans Serif',
        'DejaVu Sans'
        ],
    'font.fantasy': [
        'xkcd',
        'Humor Sans',
        'Comic Sans MS'
        ],  
    'font.monospace': [
        'DejaVu Sans Mono',
        'Computer Modern Typewriter',
        'Courier'
        ],
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 13.0,
    'text.color': '#ebecf0',
    'mathtext.fontset': 'dejavuserif',
    'mathtext.default': 'rm',

    # Lines
    'lines.linewidth': 2.0,
    'lines.antialiased': True,
    'lines.marker': 'none',
    'lines.color': '#f1f1f1', 
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
    'axes.facecolor': '#212946',
    'axes.edgecolor': '#f1f1f1',
    'axes.linewidth': 4.0,
    'axes.titlesize': 18.0, # fontsize of the axes title
    'axes.titlepad': 10.0, # pad between axes and title in points
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'left',
    #'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    #'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 14.0, # fontsize of the x any y labels
    'axes.labelpad': 5.0, # space between label and axis
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
    'axes.grid': True, # display grid or not
    'axes3d.grid': True, 
    'grid.color': '#f1f1f1',
    'grid.alpha': 0.85,
    'grid.linewidth': 0.85,
    'grid.linestyle': '-',
    
     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 3.0, # major tick length in points
    'xtick.minor.size': 0.5, # minor tick length in points
    'xtick.major.width': 1.0,  # major tick width in points
    'xtick.minor.width': 0.75,  # minor tick width in points
    'xtick.major.pad': 2.0, # distance to major tick label in points
    'xtick.minor.pad': 2.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 14.0, # fontsize of the tick labels
    'xtick.direction': 'inout',  # direction: in, out, or inout
    'xtick.color': '#f1f1f1',

    # Ticks Y
    'ytick.alignment': 'bottom',
    'ytick.major.size': 3.0,
    'ytick.minor.size': 0.5,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.75,
    'ytick.major.pad': 2.0,
    'ytick.minor.pad': 2.0,
    'ytick.minor.visible': False, 
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 14.0,
    'ytick.color': '#f1f1f1',
    'ytick.direction': 'inout',  # direction: in, out, or inout

    # Images
    'image.aspect': 'auto',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    # figure(figsize=(1,1)) would create an inch-by-inch image, which would be 100-by-100 pixels unless you also give a different dpi argument.
    # figsize = [6.4 4.8] PNG 640x480
    'figure.figsize': [6.4, 6.4],
    'figure.facecolor': '#212946',
    'figure.edgecolor': '#212946',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.titlesize': 20.0, # size of the figure title (Figure.suptitle())
    'figure.titleweight': 'bold',  # weight of the figure title


    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': '#212946',
    'savefig.edgecolor': '#212946',
    'figure.constrained_layout.use': True,
    'pdf.fonttype': 42,  # Output Type 3 (Type3) or Type 42 (TrueType)
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': True,
    'legend.frameon': False,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 3,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,   # border whitespace in fontsize units
    'legend.markerscale': 1.5,  # the relative size of legend markers vs. original
    'legend.labelspacing': 0.3,  # the vertical space between the legend entries in fraction of fontsize
    'legend.columnspacing': 1.0, # the border between the axes and legend edge in fraction of fontsize
    'legend.borderaxespad': 0.5, # the border between the axes and legend edge in fraction of fontsize
    'legend.handlelength': 1.4,  # the length of the legend lines in fraction of fontsize
    'legend.handleheight': 0.85,  # the height of the legend handle in fraction of fontsize
    'legend.handletextpad': 0.5, # the space between the legend line and legend text in fraction of fontsize
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

     # Boxplot parans
    'boxplot.boxprops.color': '#ffffff',
    'boxplot.capprops.color': '#ffffff',
    'boxplot.flierprops.color': '#ffffff',
    'boxplot.flierprops.markeredgecolor': '#ffffff',
    'boxplot.whiskerprops.color': '#ffffff',

     # Date
    'date.autoformatter.year': "%Y",
    'date.autoformatter.month': "%b",
    'date.autoformatter.day': "%d",
    'date.autoformatter.hour': "%H:%M",
    'date.autoformatter.minute': "%H:%M"
}



jotavoid = {

    # errorbar props
    'errorbar.capsize': 0.0,

     # Patches
    'patch.linewidth': 0.5,
    'patch.edgecolor': 'none',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,

    # Fonts
    'font.family': 'sans-serif',
    'font.sans-serif': [
        'Roboto',
        'Helvetica',
        'Computer Modern Sans Serif',
        'DejaVu Sans'
        ],
    'font.fantasy': [
        'xkcd',
        'Humor Sans',
        'Comic Sans MS'
        ],  
    'font.monospace': [
        'DejaVu Sans Mono',
        'Computer Modern Typewriter',
        'Courier'
        ],
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 13.0,
    'text.color': '#222222',
    'mathtext.fontset': 'dejavuserif',
    'mathtext.default': 'rm',

    # Lines
    'lines.linewidth': 2.0,
    'lines.antialiased': True,
    'lines.marker': 'none',
    'lines.color': '#f1f1f1', 
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
    'axes.facecolor': '#ffffff',
    'axes.edgecolor': '#ffffff',
    'axes.linewidth': 0.0,
    'axes.titlesize': 0.0, # fontsize of the axes title
    'axes.titlepad': 0.0, # pad between axes and title in points
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'left',
    #'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    #'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 14.0, # fontsize of the x any y labels
    'axes.labelpad': 5.0, # space between label and axis
    'axes.labelweight': 'normal',
    'axes.labelcolor': 'none',
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
    'grid.color': '#ffffff',
    'grid.alpha': 0.85,
    'grid.linewidth': 0.85,
    'grid.linestyle': '-',
    
     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 0.0, # major tick length in points
    'xtick.minor.size': 0.0, # minor tick length in points
    'xtick.major.width': 0.0,  # major tick width in points
    'xtick.minor.width': 0.0,  # minor tick width in points
    'xtick.major.pad': 0.0, # distance to major tick label in points
    'xtick.minor.pad': 0.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 0.0, # fontsize of the tick labels
    'xtick.direction': 'in',  # direction: in, out, or inout
    'xtick.color': 'none',

    # Ticks Y
    'ytick.alignment': 'bottom',
    'ytick.major.size': 0.0,
    'ytick.minor.size': 0.0,
    'ytick.major.width': 0.0,
    'ytick.minor.width': 0.0,
    'ytick.major.pad': 0.0,
    'ytick.minor.pad': 0.0,
    'ytick.minor.visible': False, 
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 0.0,
    'ytick.color': 'none',
    'ytick.direction': 'in',  # direction: in, out, or inout

    # Images
    'image.aspect': 'auto',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    # figure(figsize=(1,1)) would create an inch-by-inch image, which would be 100-by-100 pixels unless you also give a different dpi argument.
    # figsize = [6.4 4.8] PNG 640x480
    'figure.figsize': [6.4, 6.4],
    'figure.facecolor': '#ffffff',
    'figure.edgecolor': '#ffffff',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.titlesize': 20.0, # size of the figure title (Figure.suptitle())
    'figure.titleweight': 'bold',  # weight of the figure title


    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': 'none',
    'savefig.edgecolor': 'none',
    'figure.constrained_layout.use': True,
    'pdf.fonttype': 42,  # Output Type 3 (Type3) or Type 42 (TrueType)
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': True,
    'legend.frameon': False,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 3,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,   # border whitespace in fontsize units
    'legend.markerscale': 1.5,  # the relative size of legend markers vs. original
    'legend.labelspacing': 0.3,  # the vertical space between the legend entries in fraction of fontsize
    'legend.columnspacing': 1.0, # the border between the axes and legend edge in fraction of fontsize
    'legend.borderaxespad': 0.5, # the border between the axes and legend edge in fraction of fontsize
    'legend.handlelength': 1.4,  # the length of the legend lines in fraction of fontsize
    'legend.handleheight': 0.85,  # the height of the legend handle in fraction of fontsize
    'legend.handletextpad': 0.5, # the space between the legend line and legend text in fraction of fontsize
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

     # Boxplot parans
    'boxplot.boxprops.color': '#222222',
    'boxplot.capprops.color': '#222222',
    'boxplot.flierprops.color': '#222222',
    'boxplot.flierprops.markeredgecolor': '#222222',
    'boxplot.whiskerprops.color': '#222222',

     # Date
    'date.autoformatter.year': "%Y",
    'date.autoformatter.month': "%b",
    'date.autoformatter.day': "%d",
    'date.autoformatter.hour': "%H:%M",
    'date.autoformatter.minute': "%H:%M"
}





jotaneon = {


    # errorbar props
    'errorbar.capsize': 0.0,

     # Patches
    'patch.linewidth': 0.5,
    'patch.edgecolor': '#333333',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,

    # Fonts
    'font.family': 'sans-serif',
    'font.sans-serif': [
        'Roboto',
        'Helvetica',
        'Computer Modern Sans Serif',
        'DejaVu Sans'
        ],
    'font.fantasy': [
        'xkcd',
        'Humor Sans',
        'Comic Sans MS'
        ],  
    'font.monospace': [
        'DejaVu Sans Mono',
        'Computer Modern Typewriter',
        'Courier'
        ],
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 13.0,
    'text.color': '#d9d9d9',
    'mathtext.fontset': 'dejavuserif',
    'mathtext.default': 'rm',

    # Lines
    'lines.linewidth': 2.0,
    'lines.antialiased': True,
    'lines.marker': 'none',
    'lines.color': '#d9d9d9', 
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
    'axes.facecolor': '#333333',
    'axes.edgecolor': '#d9d9d9',
    'axes.linewidth': 4.0,
    'axes.titlesize': 18.0, # fontsize of the axes title
    'axes.titlepad': 10.0, # pad between axes and title in points
    'axes.titleweight': 'bold',
    'axes.titlelocation': 'left',
    #'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    #'axes.ymargin': 0.05, # change the y axis so there is no white space at the end
    'axes.labelsize': 14.0, # fontsize of the x any y labels
    'axes.labelpad': 5.0, # space between label and axis
    'axes.labelweight': 'normal',
    'axes.labelcolor': '#d9d9d9',
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
            '#04D9D9',
            '#F241A3',
            '#FA851E',
            '#BFD91A',
            '#D9D9D9',
            '#1AA0D9',
            '#E62F53',
            '#FEED00',
        ]
    ),
     # Grid
    'axes.grid': True, # display grid or not
    'axes3d.grid': True, 
    'grid.color': '#d9d9d9',
    'grid.alpha': 0.85,
    'grid.linewidth': 0.85,
    'grid.linestyle': '-',
    
     # Ticks X
    'xtick.alignment': 'center',
    'xtick.major.size': 3.0, # major tick length in points
    'xtick.minor.size': 0.5, # minor tick length in points
    'xtick.major.width': 1.0,  # major tick width in points
    'xtick.minor.width': 0.75,  # minor tick width in points
    'xtick.major.pad': 2.0, # distance to major tick label in points
    'xtick.minor.pad': 2.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 14.0, # fontsize of the tick labels
    'xtick.direction': 'inout',  # direction: in, out, or inout
    'xtick.color': '#d9d9d9',

    # Ticks Y
    'ytick.alignment': 'bottom',
    'ytick.major.size': 3.0,
    'ytick.minor.size': 0.5,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.75,
    'ytick.major.pad': 2.0,
    'ytick.minor.pad': 2.0,
    'ytick.minor.visible': False, 
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 14.0,
    'ytick.color': '#d9d9d9',
    'ytick.direction': 'inout',  # direction: in, out, or inout

    # Images
    'image.aspect': 'auto',
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    # figure(figsize=(1,1)) would create an inch-by-inch image, which would be 100-by-100 pixels unless you also give a different dpi argument.
    # figsize = [6.4 4.8] PNG 640x480
    'figure.figsize': [6.4, 6.4],
    'figure.facecolor': '#333333',
    'figure.edgecolor': '#333333',
    'figure.subplot.hspace': 0.156,
    'figure.subplot.wspace': 0.156,
    'figure.titlesize': 20.0, # size of the figure title (Figure.suptitle())
    'figure.titleweight': 'bold',  # weight of the figure title


    # set savefig
    'savefig.dpi': 100.0,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': '#333333',
    'savefig.edgecolor': '#333333',
    'figure.constrained_layout.use': True,
    'pdf.fonttype': 42,  # Output Type 3 (Type3) or Type 42 (TrueType)
    'svg.fonttype': 'none',
    'svg.fonttype': 'path',
    'svg.hashsalt': None,
    'svg.image_inline': True,

    # Legend
    'legend.loc': 'best',
    'legend.fancybox': False,
    'legend.frameon': False,
    'legend.framealpha': 0.7,
    'legend.numpoints': 1,
    'legend.scatterpoints': 3,
    'legend.title_fontsize': 'medium',
    'legend.fontsize': 'medium',
    'legend.borderpad': 0.5,   # border whitespace in fontsize units
    'legend.markerscale': 1.5,  # the relative size of legend markers vs. original
    'legend.labelspacing': 0.3,  # the vertical space between the legend entries in fraction of fontsize
    'legend.columnspacing': 1.0, # the border between the axes and legend edge in fraction of fontsize
    'legend.borderaxespad': 0.5, # the border between the axes and legend edge in fraction of fontsize
    'legend.handlelength': 1.4,  # the length of the legend lines in fraction of fontsize
    'legend.handleheight': 0.85,  # the height of the legend handle in fraction of fontsize
    'legend.handletextpad': 0.5, # the space between the legend line and legend text in fraction of fontsize
    'legend.facecolor': 'inherit',
    'legend.edgecolor': 'inherit',

     # Boxplot parans
    'boxplot.boxprops.color': '#d9d9d9',
    'boxplot.capprops.color': '#d9d9d9',
    'boxplot.flierprops.color': '#d9d9d9',
    'boxplot.flierprops.markeredgecolor': '#d9d9d9',
    'boxplot.whiskerprops.color': '#d9d9d9',

     # Date
    'date.autoformatter.year': "%Y",
    'date.autoformatter.month': "%b",
    'date.autoformatter.day': "%d",
    'date.autoformatter.hour': "%H:%M",
    'date.autoformatter.minute': "%H:%M"
}