# JOTA VIZ STYLES

Matplotlib JOTA style for making figures
This repo has Matplotlib JOTA style to format plots and figures for publications and presentation.

<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/lula_bolsonaro_tendendcia_empresa.png" width=500>

<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/bolsonaro_lula_50.0-priors.png" width=500>

## Getting Started
The easist way to install jotaviz is to use [pip](https://pip.pypa.io/en/stable/): 
```
# to install the latest release (from PyPI) 
pip install jotaviz

# in Ubuntu/Debian
python3 -m pip install jotaviz

# to install latest commit (from GitHub)
pip install git+https://github.com/JOTAJornalismo/jotaviz.git

# to clone and install from a local copy
git clone https://github.com/JOTAJornalismo/jotaviz.git
cd jotaviz
pip install -e .
```

The pip installation will automatically move all of the Matplotlib style files ```*.mplstyle``` into the appropriate directory on your computer.

Please see the [FAQ](https://github.com/JOTAJornalismo/jotaviz#faq) section for more information and troubleshooting.

## Using the Style

"extensys" is the main style from this repo. Whenever you want to use it, simply add the following to the top of your python script:

```python
import matplotlib.pyplot as plt
plt.style.use('jotaviz')
```

Available styles include: 

```python
jotaviz, jotaviz-black, jotaviz-white, jotaviz-glass
```

To use any of the styles temporarily, you can use:

```python
with plt.style.context(['jotaviz']):
    plt.figure()
    plt.plot(x, y)
    plt.show()
```

The default format to save figure is ```.png``` with ```dpi=500```. Other formats by obtained by passing it in the ```plt.savefig``` as well as the ```dpi```. For example:

```python
plt.savefig("figures/fig1" + ".pdf", dpi=1000)
```

## Examples
<p /p>

The ```jotaviz``` style:

<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/fig1.png" width=500>


<p /p>

The ```jotaviz-white``` style (with markers)

<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/fig2.png" width=500>


<p /p>

The ```jotaviz-black``` style (with grid)

<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/fig3.png" width=500>


<p /p>

The ```extensys``` + ```dark_background``` style

<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/fig5.png" width=500>


## Custom plots 
<p /p>


<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/plot_pizza-01.png" width=500>


<p /p>


<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/plot_pizza-02.png" width=500>


<p /p>


<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/plot_pizza-03.png" width=500>



<p /p>


<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/plot_pizza-05.png" width=500>



<p /p>


<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/plot_bumpy-01.png" width=500>



<p /p>


<img src="https://github.com/JOTAJornalismo/jotaviz/raw/main/examples/figures/plot_bumpy-04.png" width=500>



## Help and contribution

Please feel free to contribute to the jotaviz repo! Before starting a new style or making any changes, please create an issue through the [GitHub issue tracker](https://github.com/JOTAJornalismo/jotaviz/issues). 

If you need any help with jotaviz, please first check the [FAQ](https://github.com/JOTAJornalismo/jotaviz#faq) and search through the [previous GitHub issues](https://github.com/JOTAJornalismo/jotaviz/issues). If you can't find an answer, create a new issue through the [GitHub issue tracker](https://github.com/JOTAJornalismo/jotaviz/issues).

You can checkout [Matplotlib's documentation](https://matplotlib.org) for more information on plotting settings.



## Citation

You don't have to cite jotaviz if you use it but it's nice if you do:

```latex
@article{jotaviz,
    author    = {Daniel Marcelino},
    title     = {{JOTAJornalismo/jotaviz}},
    month     = {nov},
    year      = {2021},
    publisher = {},
    version   = {1.0.6},
    doi       = {},
    url       = {}
}
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
