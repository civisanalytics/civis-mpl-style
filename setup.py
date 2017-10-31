from setuptools import setup


def main():
    setup(
        name="civis-mpl-style",
        version="1.0.0",
        author="Civis Analytics Inc",
        author_email="opensource@civisanalytics.com",
        url="https://www.civisanalytics.com",
        description="Civis matplotlib style",
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
