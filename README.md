# Civis Style for Matplotlib

This package contains a Civis matplotlib theme.

## Installation

First, you'll need to install the package with `setup.py` or `pip`:

Bash installation:

```bash
python setup.py install
```

Pip installation:

```bash
pip install git+ssh://git@github.com/civisanalytics/civis-mpl-style.git
```

Next, run the following to put the Civis style in the matplotlib
configuration directory (typically `~/.matplotlib/stylelib/`).

```bash
install-civis-style
```


## Usage

Using the matplotlib style.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100)
y = np.sqrt(x) + np.random.RandomState(42).rand(len(x))

with plt.style.context('civis'):
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    plt.show()
```

See `examples.ipynb` for more examples. 
