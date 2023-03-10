#!/usr/bin/env python

"""
    Utilities only for the development of the hello package

    Author: <your name, <email>>
    Affl.: <your affiliation>
"""

from pathlib import Path


# Absolute path to project repo
REPO_PATH = Path(__file__).resolve().parents[1]


class _Config:
    root_dir = REPO_PATH
    data_dir = Path(REPO_PATH, 'data')
    config_dir = Path(REPO_PATH, 'config')


print(f"Repository root directory: {_Config.root_dir}")
print(f"Repository data directory: {_Config.data_dir}")
print(f"Repository config directory: {_Config.config_dir}")

REPO_CFG = _Config()

