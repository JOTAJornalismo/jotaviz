# LATEX
from cycler import cycler

available =['jotagray', 'academic']

jotagray = {
     # Patches
    'patch.linewidth': 0.5,
    'patch.facecolor': '#ebecf0',
    'patch.edgecolor': '#ebecf0',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,

    # errorbar props
    'errorbar.capsize': 0.0,
    # Fonts
    'font.family': 'roboto',
    'font.style': 'normal',
    'font.variant': 'normal',
    'font.weight': 'normal',
    'font.stretch': 'normal',
    'font.size': 14.0,
    'text.color': '#222222',
    'mathtext.fontset': 'cm',
    'mathtext.default': 'rm',

    # Lines
    'lines.linewidth': 2.0,
    'lines.antialiased': True,
    'lines.marker': None, 
    'lines.markersize': 10.0,
    'lines.solid_capstyle': 'butt',
    'lines.dashed_pattern': [6.0, 6.0],
    'lines.dashdot_pattern': [3.0, 5.0, 1.0, 5.0],
    'lines.dotted_pattern': [1.0, 3.0],
    'lines.markeredgewidth': 2.0,
    'lines.markerfacecolor': 'auto',
    'lines.markeredgecolor': 'auto',

    # scatter props
    'scatter.marker': 'o',
    'markers.fillstyle': 'full',

    # AXES
    # Documentation for cycler (https://matplotlib.org/cycler/),
    # Axes
    'axes.facecolor': '#ebecf0',
    'axes.edgecolor': '#ebecf0',
    'axes.linewidth': 4.0,
    'axes.labelpad': 5.0,
    'axes.titlesize': 18.0,
    'axes.titleweight': 'bold',
    'axes.xmargin': 0.0, # change the x axis so there is no white space at the end
    'axes.ymargin': 0.0, # change the y axis so there is no white space at the end
    'axes.labelsize': 16.0,
    'axes.labelweight': 'normal',
    # 'axes.axisbelow': True,
    'axes.autolimit_mode': 'round_numbers',
    'axes.unicode_minus': True,
    'axes.spines.left': False,
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.spines.bottom': False,
    'axes.formatter.use_locale': True,
    'axes.formatter.useoffset': False,
    'axes.formatter.offset_threshold': 2,
    'axes.axisbelow': 'line',

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
    # Grid
    'axes.grid': False,
    'grid.color': '#555555',
    'grid.linewidth': 1.0,
    'grid.linestyle': ':',

     # Ticks X
    'xtick.major.size': 10.0, # major tick length in points
    'xtick.minor.size': 0.2, # minor tick length in points
    'xtick.major.width': 1.5,  # major tick width in points
    'xtick.minor.width': 0.5,  # minor tick width in points
    'xtick.major.pad': 5.0, # distance to major tick label in points
    'xtick.minor.pad': 2.0, # distance to the minor tick label in points
    'xtick.minor.visible': False, 
    'xtick.top': False,
    'xtick.labelsize': 18.0, # fontsize of the tick labels
    'xtick.direction': 'in',  # direction: in, out, or inout
    'xtick.color': '#333333',
    # Ticks Y
    'ytick.major.size': 0.0,
    'ytick.minor.size': 0.0,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.5,
    'ytick.major.pad': 0.0,
    'ytick.minor.pad': 0.0,
    'ytick.minor.visible': False,
    'ytick.right': False,
    'ytick.left': False,
    'ytick.labelsize': 18.0,
    'ytick.color': '#333333',
    'ytick.direction': 'out',  # direction: in, out, or inout

    # Images
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Figure
    'figure.figsize': [8.75, 5.92],
    'figure.facecolor': '#ebecf0',
    'figure.edgecolor': '#ebecf0',
    'figure.subplot.hspace': 0.2,
    'figure.subplot.wspace': 0.2,
    'figure.subplot.left': 0.08,
    'figure.subplot.right': 0.95,
    'figure.subplot.bottom': 0.07,
    'figure.subplot.top': 0.95,
    'figure.titlesize': 32.0,
    'figure.titleweight': 'bold',

    # set savefig
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': '#ebecf0',
    'savefig.edgecolor': '#ebecf0',
    'figure.constrained_layout.use': True,
    'svg.fonttype': 'path',

    # Legend
    'legend.fancybox': True,
    'legend.loc': 'best',

     # Date
    'date.autoformatter.year': '%Y',
    'date.autoformatter.month': '%b %Y',
    'date.autoformatter.day': '%b %d %Y',
    'date.autoformatter.hour': '%H:%M:%S',
    'date.autoformatter.minute': '%H:%M:%S.%f',
    'date.autoformatter.second': '%H:%M:%S.%',
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