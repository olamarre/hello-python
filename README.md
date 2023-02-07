# hello-python
A sample Python project for robotics researchers.

## Environment setup

After installing conda ([Miniconda3](https://docs.conda.io/en/latest/miniconda.html) recommended), run the following:

```sh
git clone https://github.com/olamarre/hello-python.git && cd hello-python

# Create & activate the conda env
conda env create -f environment.yml
conda activate hello-env

# Install the iPython kernel spec file (necessary to use the conda environment
# in Jupyter notebooks)
python -m ipykernel install --user --name hello-env
```

