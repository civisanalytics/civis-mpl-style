from setuptools import setup


def main():
    setup(
        name="civis-mpl-style",
        version="1.0.0",
        packages=['civis_mpl_style'],
        install_requires=[
            'matplotlib~=2.0'
        ],
        entry_points={
            'console_scripts': [
                'install-civis-style = civis_mpl_style.install_style:main'
            ]
        },
        package_data = {'': ['civis.mplstyle']}
    )


if __name__ == "__main__":
    main()
