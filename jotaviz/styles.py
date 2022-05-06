"""jotaviz - A collection of plotting functions and styles used at jota.info"""



__all__ = ['jota_gray', 'jota_white',
           'jota_dark']


# Version 1 astropy plotting style for matplotlib
jota_gray = {

    # errorbar props
    'errorbar.capsize': 0.0,

    # Lines
    'lines.linewidth': 1.7,
    'lines.antialiased': True,

    # Patches
    'patch.linewidth': 0.5,
    'patch.facecolor': '#ebecf0',
    'patch.edgecolor': '#ebecf0',
    'patch.antialiased': True,
    'patch.force_edgecolor': True,
    'hatch.linewidth': 1.0,
    
    'svg.fonttype': 'path',

    # Images
    'image.cmap': 'gist_heat',
    'image.origin': 'upper',

    # Font
    'font.size': 12.0,

    # Axes
    'axes.facecolor': '#FFFFFF',
    'axes.edgecolor': '#AAAAAA',
    'axes.linewidth': 1.0,
    'axes.grid': True,
    'axes.titlesize': 'x-large',
    'axes.labelsize': 'large',
    'axes.labelcolor': 'k',
    'axes.axisbelow': True,

    # Ticks
    'xtick.major.size': 0,
    'xtick.minor.size': 0,
    'xtick.major.pad': 6,
    'xtick.minor.pad': 6,
    'xtick.color': '#565656',
    'xtick.direction': 'in',
    'ytick.major.size': 0,
    'ytick.minor.size': 0,
    'ytick.major.pad': 6,
    'ytick.minor.pad': 6,
    'ytick.color': '#565656',
    'ytick.direction': 'in',

    # Legend
    'legend.fancybox': True,
    'legend.loc': 'best',

    # Figure
    'figure.figsize': [8, 6],
    'figure.facecolor': '1.0',
    'figure.edgecolor': '0.50',
    'figure.subplot.hspace': 0.5,

    # Other
    # set savefig
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02, # Use virtually all space when we specify figure dimensions
    'savefig.format': 'png',
    'savefig.facecolor': '#ebecf0',
    'savefig.edgecolor': '#ebecf0'
}


color_cycle = ['#348ABD',   # blue
               '#7A68A6',   # purple
               '#A60628',   # red
               '#467821',   # green
               '#CF4457',   # pink
               '#188487',   # turquoise
               '#E24A33']   # orange


jota_white = {

}


jota_dark = {
    
}