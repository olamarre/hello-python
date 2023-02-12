#!/usr/bin/env bash

# Example script to set environment variables in a conda env
# 
# Author: Author: <your name, <email>>
# Affl.: <your affiliation>

USAGE="Add an environment variable to the currently active conda env

    Usage:
        bash $(basename "$0") [-h] -n <variable_name> -v <variable_value>

    Args:
        -h  Shows this help text
        -n  Variable name
        -v  Variable value
"

while getopts hn:v: flag
do
    case "${flag}" in
        h) echo "$USAGE" && exit 0;;
        n) VAR_NAME=${OPTARG};;
        v) VAR_VALUE=${OPTARG};;
    esac
done

echo "Creating env variable ${VAR_NAME}=${VAR_VALUE}"

# Create the directories where the (de)activation scripts are called from 
mkdir -v -p $CONDA_PREFIX/etc/conda/activate.d
mkdir -v -p $CONDA_PREFIX/etc/conda/deactivate.d

echo "export ${VAR_NAME}=${VAR_VALUE}" >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo "unset ${VAR_NAME}" >> $CONDA_PREFIX/etc/conda/deactivate.d/env_vars.sh

echo "Deactivate & (re)activate the conda environment"