from cycler import cycler 
from jotaviz import defaults

available = ['series_color', 'series_linestyle', 'series_linewidth', 'series_marker', 'series_markersize', 'series_linestyle_color', 'series_marker_color', 'series_linestyle_marker_color', 'series_fontsize', 'series_linestyle_marker']

def series_linestyle():
    return cycler(linestyle=list(defaults.line_styles.values()))

def series_linewidth():
    return cycler(linewidth=list(defaults.line_widths.values()))

def series_color():
    return cycler(color=list(defaults.colors.values()))

def series_marker():
    return cycler(marker=list(defaults.markers.values()))

def series_markersize():
    return cycler(markersize=list(defaults.marker_sizes.values()))

def series_fontsize():
    return cycler(fontsize=list(defaults.font_sizes.values()))

def series_linestyle_color():
    colors = list(defaults.colors.values())
    linestyles=list(defaults.line_styles.values())
    upper_limit = len(colors) if len(colors) < len(linestyles) else len(linestyles)
    c1 = cycler(color=colors[:upper_limit])
    c2 = cycler(linestyle=linestyles[:upper_limit])
    return (c1+c2)

def series_marker_color():
    colors = list(defaults.colors.values())
    markers=list(defaults.markers.values())
    upper_limit = len(colors) if len(colors) < len(markers) else len(markers)
    c1 = cycler(color=colors[:upper_limit])
    c2 = cycler(marker=markers[:upper_limit])
    return (c1+c2)

def series_linestyle_marker():
    linestyles=list(defaults.line_styles.values())
    markers=list(defaults.markers.values())
    upper_limit = len(linestyles) if len(linestyles) < len(markers) else len(markers)
    c1 = cycler(linestyle=linestyles[:upper_limit])
    c2 = cycler(marker=markers[:upper_limit])
    return (c1+c2)

def series_linestyle_marker_color():
    colors = list(defaults.colors.values())
    linestyles=list(defaults.line_styles.values())
    markers=list(defaults.markers.values())
    upper_limit = len(colors) if len(colors) < len(linestyles) else len(linestyles)
    upper_limit = upper_limit if upper_limit < len(markers) else len(markers)
    c1 = cycler(color=colors[:upper_limit])
    c2 = cycler(linestyle=linestyles[:upper_limit])
    c3 = cycler(marker=markers[:upper_limit])
    return (c1+c2+c3)