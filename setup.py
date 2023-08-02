import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kimariplot",
    version="1.2.5",
    author="Kimariyb",
    author_email="kimariyb@163.com",
    description="A tool for generating Kimari-plots.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kimariyb/kimariPlot",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'kimariplot=kimariplot.plotter:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)