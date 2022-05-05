"""
=====================
Different Units Pizza
=====================

Here we plot a pizza chart where the parameters have the same units, but the maximum
is five instead of 100.
"""

import matplotlib.pyplot as plt

from jotaviz import Pizza, FontManager

##############################################################################
# Load some fonts
# ---------------
# We will use jotaviz's FontManager to load some fonts from Google Fonts.
# We borrowed the FontManager from the excellent
# `ridge_map library <https://github.com/ColCarroll/ridge_map>`_.

font_normal = FontManager(("https://github.com/google/fonts/blob/main/apache/roboto/static/"
                           "Roboto-Regular.ttf?raw=true"))
font_italic = FontManager(("https://github.com/google/fonts/blob/main/apache/roboto/static/"
                           "Roboto-Italic.ttf?raw=true"))
font_bold = FontManager(("https://github.com/google/fonts/blob/main/apache/roboto/static/"
                         "Roboto-Medium.ttf?raw=true"))

##############################################################################
# Different Units
# ---------------
# Till now we were plotting a percentile chart where the upper limit was 100.
# Let's take another example where the lower limit is 0 and upper limit is 5.
# The below code shows how to plot pizza-chart for such case.

# parameter and value list
params = ['Speed', 'Agility', 'Strength', 'Passing', 'Dribbles']
values = [5, 2, 4, 3, 1]

# instantiate Pizza class
baker = Pizza(
    params=params,                  # list of parameters
    straight_line_color="#F2F2F2",  # color for straight lines
    straight_line_lw=1,             # linewidth for straight lines
    straight_line_limit=5.0,        # max limit of straight lines
    last_circle_lw=0,               # linewidth of last circle
    other_circle_lw=0,              # linewidth for other circles
    inner_circle_size=0.4,          # size of inner circle
)

# plot pizza
fig, ax = baker.make_pizza(
    values,                     # list of values
    figsize=(8, 8),             # adjust figsize according to your need
    color_blank_space="same",   # use same color to fill blank space
    blank_alpha=0.4,            # alpha for blank-space colors
    param_location=5.5,         # where the parameters will be added
    kwargs_slices=dict(
        facecolor="cornflowerblue", edgecolor="#F2F2F2",
        zorder=2, linewidth=1
    ),                          # values to be used when plotting slices
    kwargs_params=dict(
        color="#000000", fontsize=12,
        fontproperties=font_normal.prop, va="center"
    ),                          # values to be used when adding parameter
    kwargs_values=dict(
        color="#000000", fontsize=12,
        fontproperties=font_normal.prop, zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="cornflowerblue",
            boxstyle="round,pad=0.2", lw=1
        )
    )                           # values to be used when adding parameter-values
)

# add title
fig.text(
    0.515, 0.97, "Player Name - Team Name", size=18,
    ha="center", fontproperties=font_bold.prop, color="#000000"
)

# add subtitle
fig.text(
    0.515, 0.942,
    "Rank vs Player's Position | Season Name",
    size=15,
    ha="center", fontproperties=font_bold.prop, color="#000000"
)

# plt.show()

plt.savefig("plot_pizza-11.png")