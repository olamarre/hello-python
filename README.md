# hello-python

![Tests](https://github.com/olamarre/hello-python/actions/workflows/python-conda-app.yml/badge.svg)

A sample Python project for robotics researchers.

Presented as part of the University of Toronto's Robotics Institute Tutorial Series.

## Environment setup

1. Install conda ([Miniconda3](https://docs.conda.io/en/latest/miniconda.html) recommended)
2. (Optional) install the [mamba](https://mamba.readthedocs.io/en/latest/installation.html#existing-conda-install) package. In this case, replace all the "conda" commands with "mamba" below.
3. Run the following:

```sh
git clone https://github.com/olamarre/hello-python.git && cd hello-python

# Create & activate the conda env
conda env create -f environment.yml
conda activate hello-env

# Install the iPython kernel spec file (necessary to use the conda environment
# in Jupyter notebooks)
python -m ipykernel install --user --name hello-env
```

## Tests & checkups

```sh
# Coding style checkup / linting
flake8 .

# Verify tests & code coverage
pytest .
```
