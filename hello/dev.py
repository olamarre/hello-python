#!/usr/bin/env python

""" 
    Utilities only for the development of the hello package

    Author: Olivier Lamarre
    Affl.: STARS Laboratory, University of Toronto
"""

from pathlib import Path


# Absolute path to project repo
REPO_PATH = Path(__file__).resolve().parents[1] 

class _Config:
    root_dir = REPO_PATH
    data_dir = Path(REPO_PATH, 'data')

print(f"Repository root directory: {_Config.root_dir}")
print(f"Repository data directory: {_Config.data_dir}")

REPO_CFG = _Config()

