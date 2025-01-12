# My Python package scaffolding

<!-- cSpell:ignore pytest pyproject -->

Sunday, January 12, 2025

This is my attempt to understand Python packaging. Material I am based is (Packaging Python Projects)[https://packaging.python.org/en/latest/tutorials/packaging-projects/].

## Installation of this scaffolding package

I do not put my package in [PyPI](https://pypi.org/). Download the package, maybe in a zip file format, unzip it, and install it from the current directory. Command you should run is:

`python -m pip install ./  # install from the current directory.`

After installation, you can optionally run tests with [pytest](https://docs.pytest.org/).

`pytest ./tests`


## What I don't understand...

`pyproject.toml` and `setup.py` has many settings in common. What is `pyproject.toml` for?
