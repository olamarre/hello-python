# hello-python

![Tests](https://github.com/olamarre/hello-python/actions/workflows/python-conda-tests.yml/badge.svg)
<!-- ![Flake8](https://github.com/utiasSTARS/spatiotemp-planning/actions/workflows/flake8.yml/badge.svg) -->

A sample Python project for robotics researchers.

## Environment setup

After installing conda ([Miniconda3](https://docs.conda.io/en/latest/miniconda.html) recommended), run the following (if you have installed the [mamba](https://mamba.readthedocs.io/en/latest/installation.html#existing-conda-install) package, replace all "conda" commands with "mamba" below):

```sh
git clone https://github.com/olamarre/hello-python.git && cd hello-python

# Create & activate the conda env
conda env create -f environment.yml
conda activate hello-env

# Install the iPython kernel spec file (necessary to use the conda environment
# in Jupyter notebooks)
python -m ipykernel install --user --name hello-env
```
