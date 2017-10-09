import os
import matplotlib as mpl


def main():
    """Put a copy of the matplotlib style spec in the expected location."""

    this_dir = os.path.dirname(os.path.realpath(__file__))
    style_path = os.path.join(this_dir, 'civis.mplstyle')
    with open(style_path) as f:
        style_doc = f.read()

    mpl_style_dir = os.path.join(mpl.get_configdir(), 'stylelib')
    if not os.path.exists(mpl_style_dir):
        os.makedirs(mpl_style_dir)
    with open(os.path.join(mpl_style_dir, 'civis.mplstyle'), 'w') as new_style:
        new_style.write(style_doc)


if __name__ == '__main__':
    main()
