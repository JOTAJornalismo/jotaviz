# jotaviz_plot.py - collection of plotting functions

import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, YearLocator, MonthLocator, DayLocator, date2num
import collections


def jotaviz_footnote(fig, text='JOTA Labs'):
    """Add a footnote to the figure, at the bottom righthand side"""

    fig.text(0.99, 0.01, text, ha='right', va='bottom',
        fontsize='xx-small', fontstyle='normal', fontweight='bold', color='k', backgroundcolor = '#f05741')


def jotaviz_heading(fig, text=None):
    """Add a heading to a figure"""

    if text:
        fig.suptitle(text, linespacing=1.2)


def jotaviz_save_to_file(fig, filename=None):
    """Save the figure to a filename"""

    if filename:
        fig.savefig(filename, dpi=300)


def jotaviz_hide_first_and_last_yticks(ax):
    """Hide the top and bottom y-tick labels"""

    yticks = ax.yaxis.get_major_ticks()
    for y in yticks:
        y.label1.set_visible(True)
    yticks[0].label1.set_visible(False)
    yticks[-1].label1.set_visible(False)


def jotaviz_hide_first_and_last_xticks(ax):
    """Hide the far left and right x-tick labels"""

    xticks = ax.xaxis.get_major_ticks()
    xticks[0].label1.set_visible(False)
    xticks[-1].label1.set_visible(False)


def jotaviz_get_fax(fax):
    if fax:
        # we have a figure and axes to which we are adding
        fig, ax = fax
    else:
        # get a new figue and axis
        fig, ax = plt.subplots()

    return (fig, ax)


def jotaviz_set_ylims(fax, ax, data):
    currentylim = ax.get_ylim()
    ymin = min(data)
    ymax = max(data)
    yspan = ymax - ymin
    ymin = ymin - (yspan * 0.03)
    ymax = ymax + (yspan * 0.03)
    if fax:
        ax.set_ylim(min(ymin, currentylim[0]), max(ymax, currentylim[1]))
    else:
        ax.set_ylim(ymin, ymax)


def jotaviz_set_labs(ax, xlab, ylab):
    if xlab:
        ax.set_xlabel(xlab)
    if ylab:
        ax.set_ylabel(ylab)


def jotaviz_set_lines(ax, hlines, vlines):
    if hlines is not None:
        ax.axhline(y=hlines, color='gray', linewidth=0.5)
    if vlines is not None:
        ax.axvline(x=vlines, color='gray', linewidth=0.5)


def jotaviz_min_max_end(series, fax, filename=None):
    """Annotate a chart based on a pandas series of data and a datetime.date index
       The series should have an ascending sorted index"""

    fig, ax = fax

    tc = 'gray' # annotation colour

    # placement on y axis
    yr = ax.get_ylim()
    span = yr[1] - yr[0]
    extra = (span * 0.01)
    bottom = yr[0] + extra
    top = yr[1] - extra

    # end - kludge on spacing - come back and think about this
    xr = ax.get_xlim()
    xspan = xr[1] - xr[0]
    xextra = max(1, int(xspan * 0.0075)) * datetime.timedelta(days=1)
    last = str(round(series.iat[len(series)-1], 1))
    lastdate = series.index[len(series)-1]
    ax.axvline(x=lastdate, color=tc, linewidth=0.5)
    ax.text(x=lastdate+xextra, y=bottom, s=last, color=tc, ha='left',
        va='bottom', fontsize='x-small', rotation='vertical')

    # max
    maximum = max(series)
    maxdate = date2num(series[series == maximum].index[0])
    if maxdate != date2num(lastdate):
        ax.axvline(x=maxdate, color=tc, linewidth=0.5)
        maximum = str(round(maximum, 1))
        ax.text(x=maxdate, y=bottom, s=maximum, color=tc, ha='right',
            va='bottom', fontsize='x-small', rotation='vertical')

    # min
    minimum = min(series)
    mindate = date2num(series[series == minimum].index[0])
    if mindate != date2num(lastdate):
        ax.axvline(x=mindate, color=tc, linewidth=0.5)
        minimum = str(round(minimum, 1))
        ax.text(x=mindate, y=top, s=minimum, color=tc, ha='right',
            va='top', fontsize='x-small', rotation='vertical')

    jotaviz_save_to_file(fig, filename)

    return (fig, ax)


def jotaviz_vertical_annotate(fax, date, text):

    fig, ax = fax
    tc = 'gray' # annotation colour
    yr = ax.get_ylim()
    span = yr[1] - yr[0]
    extra = (span * 0.01)
    bottom = yr[0] + extra
    top = yr[1] - extra

    nDate = date2num(date)
    ax.axvline(x=nDate, color=tc, linewidth=0.5)
    ax.text(x=nDate, y=top, s=text, color=tc, ha='right',
        va='top', fontsize='x-small', rotation='vertical')

    return (fig, ax)


def jotaviz_set_xticks_for_dates(ax, min_date, max_date):
    """manage the x-axis the way I like it ...
       ax - a matplotlib axes
       min_date - a datetime.date object
       max_date - a datetime.date object

       Assumes we are dealing with daily data or less frequent"""

    # give a bit of space at each end of the plot - aesthetics
    span = max_date - min_date
    extra = int(span.days * 0.025) * datetime.timedelta(days=1)
    ax.set_xlim([min_date - extra, max_date + extra])

    # place a sensible selection of xticks and labels
    if (span) <= datetime.timedelta(days=7):
        ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
        ax.xaxis.set_major_locator(DayLocator())
    elif (span) <= datetime.timedelta(days=14):
        ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
        ax.xaxis.set_major_locator(DayLocator(interval=2))
    elif (span) <= datetime.timedelta(days=21):
        ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
        ax.xaxis.set_major_locator(DayLocator(interval=3))
    elif (span) <= datetime.timedelta(days=28):
        ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
        ax.xaxis.set_major_locator(DayLocator(interval=4))
    elif (span) <= datetime.timedelta(days=35):
        ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
        ax.xaxis.set_major_locator(DayLocator(interval=5))
    elif (span) <= datetime.timedelta(days=42):
        ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
        ax.xaxis.set_major_locator(DayLocator(interval=6))
    elif (span) <= datetime.timedelta(days=49):
        ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
        ax.xaxis.set_major_locator(DayLocator(interval=7))
    elif (span) <= datetime.timedelta(days=100):
        ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
        ax.xaxis.set_major_locator(DayLocator(interval=14))
    elif (span) <= datetime.timedelta(days=180):
        ax.xaxis.set_major_formatter(DateFormatter('%b-%y'))
        ax.xaxis.set_major_locator(MonthLocator(bymonthday=1, interval=1))
    elif (span) <= datetime.timedelta(days=370):
        ax.xaxis.set_major_formatter(DateFormatter('%b-%y'))
        ax.xaxis.set_major_locator(MonthLocator(bymonthday=1, interval=2))
    elif (span) <= datetime.timedelta(days=740):
        ax.xaxis.set_major_formatter(DateFormatter('%b-%y'))
        ax.xaxis.set_major_locator(MonthLocator(bymonthday=1, interval=3))
    elif (span) <= datetime.timedelta(days=1000):
        ax.xaxis.set_major_formatter(DateFormatter('%b-%y'))
        ax.xaxis.set_major_locator(MonthLocator(bymonthday=1, interval=6))
    else:
        ax.xaxis.set_major_formatter(DateFormatter('%Y'))
        ax.xaxis.set_major_locator(YearLocator())


def jotaviz_plot_ts_long(df, data, var, fax=None, filename=None, colors=None, formats=None,
    heading=None, xlab=None, ylab=None, hlines=None, vlines=None, xlim=None, yLim=None):
    """Plot the data in the column named data, against the timeseries in df.index"""

    # - preliminaries
    df = df.copy() # let's not damage the original data source

    # - establish the figure and axes
    fig, ax = jotaviz_get_fax(fax)

    # - convert index to datetime.date
    dates = None
    if isinstance(df.index, pd.tseries.period.PeriodIndex):
        dates = [zzz.to_timestamp().date() for zzz in df.index]
    if isinstance(df.index, pd.tseries.index.DatetimeIndex):
        dates = df.index.date # note: attribute
    if dates is None:
        dates = df.index # assume index is of type datetime.date
    df['__Dates'] = dates

    # - plot preparation
    if var is not None:
        variables = df[var].unique()
    else:
        variables = ['-'] # single data series plot

    if not formats:
        formats = ['<', '>', '^', 'v', 'o', 's', 'd', 'h', 'p']
    if isinstance(formats, str):
        formats = np.repeat(formats, len(variables)).tolist()

    # - plotting
    for v, i in zip(variables, range(len(variables))):
        if var is not None:
            y = df[df[var] == v]
        else:
            y = df
        x = y['__Dates']
        ax.plot_date(x=x, y=y[data], fmt=formats[i],
            label=v, markerfacecolor='None',
            tz=None, xdate=True, ydate=False)

    # - set axes labels
    jotaviz_set_labs(ax=ax, xlab=xlab, ylab=ylab)

    # set y-axis limits
    jotaviz_set_ylims(fax=fax, ax=ax, data=df[data])
    jotaviz_hide_first_and_last_yticks(ax)

    # hlines and vlines
    jotaviz_set_lines(ax, hlines, vlines)

    # fix x-axis
    if not fax:
        #print(type(df['__Dates'][0]))
        mind = min(df['__Dates'])
        maxd = max(df['__Dates'])
        jotaviz_set_xticks_for_dates(ax, mind, maxd)

    # heading
    jotaviz_heading(fig, heading)
    if not fax:
        fig.tight_layout()

    # legend above
    if(len(variables)) > 1:
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width, box.height * 0.89])
        ax.legend(bbox_to_anchor=(0.5, 1.09), loc='upper center', ncol=9, numpoints=1)

    # footnote
    if not fax:
        jotaviz_footnote(fig)

    # save
    jotaviz_save_to_file(fig, filename)

    return (fig, ax)


def jotaviz_bayes_ts(df, fax=None, filename=None, color=None, formats=None, legend=True,
    heading=None, xlab=None, ylab=None, hlines=None, vlines=None, xlim=None, yLim=None):

    # - establish the figure and axes
    fig, ax = jotaviz_get_fax(fax)

    if not color:
        color = 'royalblue'

    if fax:
        oldLegend = ax.get_legend()

    # plotting the data
    dates_as_nums = date2num(df.Date.values)
    ax.fill_between(x=dates_as_nums, y1=df.l005, y2=df.u995, color=color, alpha=0.1) # , label='middle 99%'
    ax.fill_between(x=dates_as_nums, y1=df.l025, y2=df.u975, color=color, alpha=0.2) # , label='middle 95%'
    ax.fill_between(x=dates_as_nums, y1=df.l10, y2=df.u90, color=color, alpha=0.3) # , label='middle 80%'
    ax.fill_between(x=dates_as_nums, y1=df.l25, y2=df.u75, color=color, alpha=0.4) # , label='middle 50%'
    ax.plot_date(x=df.Date, y=df['median'], fmt='-', color=color, alpha=0.9) # , label='median'

    # proxy artist kludge for the legend ...
    m99 = plt.Rectangle((0, 0), 1, 1, fc=color, alpha=0.1)
    m95 = plt.Rectangle((0, 0), 1, 1, fc=color, alpha=0.22)
    m80 = plt.Rectangle((0, 0), 1, 1, fc=color, alpha=0.366)
    m50 = plt.Rectangle((0, 0), 1, 1, fc=color, alpha=0.5464)
    import matplotlib.lines as mlines
    mid = mlines.Line2D([], [], color=color)

    jotaviz_set_ylims(fax=fax, ax=ax, data=df.l005.tolist()+df.u995.tolist())
    jotaviz_hide_first_and_last_yticks(ax)

    if not fax:
        # give a bit of space at each end of the plot - aesthetics
        mind = min(df.Date)
        maxd = max(df.Date)
        jotaviz_set_xticks_for_dates(ax, mind, maxd)

    # hlines and vlines
    jotaviz_set_lines(ax, hlines, vlines)

    # - set axes labels
    jotaviz_set_labs(ax=ax, xlab=xlab, ylab=ylab)

    # heading
    jotaviz_heading(fig, heading)

    # positioning the legend
    if legend:
        if fax: # adding to existing chart
            box = ax.get_position()
            ax.add_artist(oldLegend)
            ax.set_position([box.x0, box.y0, box.width, box.height * 0.93])
            positions = 1.18
        else: # new chart
            fig.tight_layout()
            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width, box.height * 0.89])
            positions = 1.09

        ax.legend([mid, m50, m80, m95, m99],
            ['Median', 'Middle 50%', 'Middle 80%', 'Middle 95%', 'Middle 99%'],
            loc='upper center', ncol=5,
            bbox_to_anchor=(0.5, positions))

    # footnote
    if not fax:
        jotaviz_footnote(fig)

    jotaviz_save_to_file(fig, filename)

    return (fig, ax)


def jotaviz_plot_house_effects(df, heading=None, filename=None, color='royalblue',
    xlab='Relative Pro-Coalition House Effect (Percentage Points)',
    vlines=0):

    df = df.sort('median')
    fig, ax = plt.subplots()

    # the data
    ax.barh(bottom=pd.Series(range(len(df)))-0.4, left=df['l005'],
        width=df['u995']-df['l005'], height=0.8, color=color, alpha=0.1)
    ax.barh(bottom=pd.Series(range(len(df)))-0.4, left=df['l025'],
        width=df['u975']-df['l025'], height=0.8, color=color, alpha=0.2)
    ax.barh(bottom=pd.Series(range(len(df)))-0.4, left=df['l10'],
        width=df['u90']-df['l10'], height=0.8, color=color, alpha=0.3)
    ax.barh(bottom=pd.Series(range(len(df)))-0.4, left=df['l25'],
        width=df['u75']-df['l25'], height=0.8, color=color, alpha=0.4)

    if vlines is not None:
        ax.axvline(x=vlines, color='gray', linewidth=0.5)

    # text labels for medians
    for i, d in zip(range(len(df['median'])), df['median'].values):
        mid = ax.scatter(x=d, y=i-0.15, s=70, marker='^', facecolor="white",
            edgecolor=color, linewidth=0.5, zorder=2)
        ax.text(x=d, y=i, s=str(round(d, 2)), ha='center', va='bottom', color='black',
            fontsize='x-small')

    # y-axis
    ax.set_ylim([-0.5, len(df)-0.5])
    ax.set_yticks([x for x in range(0, len(df))])
    ax.set_yticklabels(df['House'].tolist())

    # x-axis
    ax.set_xlabel(xlab)
    xmin = min(df['l005'])
    xmax = max(df['u995'])
    ax.set_xlim([xmin-0.1, xmax+0.1])
    jotaviz_hide_first_and_last_xticks(ax)

    # rest of chart
    jotaviz_heading(fig, heading)
    fig.tight_layout()

    # proxy artist kludge for the legend ...
    m99 = plt.Rectangle((0, 0), 1, 1, fc=color, alpha=0.1)
    m95 = plt.Rectangle((0, 0), 1, 1, fc=color, alpha=0.22)
    m80 = plt.Rectangle((0, 0), 1, 1, fc=color, alpha=0.366)
    m50 = plt.Rectangle((0, 0), 1, 1, fc=color, alpha=0.5464)

    # positioning the legend
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.89])
    ax.legend([mid, m50, m80, m95, m99], ['Median', 'Middle 50%', 'Middle 80%', 'Middle 95%', 'Middle 99%'],
        loc='upper center', ncol=5,bbox_to_anchor=(0.5, 1.09), scatterpoints=1)

    jotaviz_footnote(fig)

    jotaviz_save_to_file(fig, filename)

