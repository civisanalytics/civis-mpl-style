from collections import OrderedDict

from matplotlib.colors import ListedColormap
try:
    import seaborn.apionly as sns
    _HAS_SEABORN = True
except ImportError:
    _HAS_SEABORN = False


__ALL__ = ['cmap', 'add_to_mpl']


_colors = OrderedDict(
    darkyellow="#F4A800",
    darkblue="#006082",
    darkred="#D8432C",
    darkgreen="#00AA7F",
    black="#3C383C",
    yellow="#FFC425",
    blue="#0194D3",
    red="#F77552",
    green="#49DEA4",
    purple="#86518D",
    brown="#BF8669",
    gray="#555555",
    lightyellow="#FFE180",
    lightblue="#4DC0E8",
    lightred="#FFCBC2",
    lightgreen="#C5E5D4",
    lightpurple="#C9B2CE",
    lightbrown="#E7C8A9",
    lightgray="#D1D3D4",
    mediumgray="#929292",
    lighteryellow="#FFEBB3",
    lighterblue="#86CFE8",
    lightergray="#ECECEC",
)


def add_to_mpl():
    import matplotlib as mpl
    mpl.colors.ColorConverter.colors.update(
        {'civis.' + k: v for k, v in _colors.items()}
    )


cmap = ListedColormap(_colors.values())

if _HAS_SEABORN:
    seaborn_palette = sns.color_palette(_colors.values())
    __ALL__.append('seaborn_palette')
else:
    seaborn_palette = None
