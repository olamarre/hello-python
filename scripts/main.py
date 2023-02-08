#!/usr/bin/env python

""" 
    A sample python script

    Usage: python main.py -h
    (use a module like argparse to define a helper function and
    describe input variables)

    Author: <yourself, <email>>
    Affl.: <your affiliation>
"""

from pathlib import Path
import logging
import logging.config
import json

from hello_python.config import REPO_CFG

def main():
    pass

if __name__ == "__main__":

    # Load the repository's logging configuration
    with open(Path(REPO_CFG.root_dir, 'logging.json')) as f:
        log_cfg = json.load(f)
    
    log_dir = Path(REPO_CFG.data_dir, 'logs')
    log_dir.mkdir(exist_ok=True)

    lfn = Path(log_dir, f'{Path(__file__).stem}.log')
    log_cfg['handlers']['file']['filename'] = lfn
    logging.config.dictConfig(log_cfg)
    log = logging.getLogger(__name__)
    print(f"Logging to {lfn}")

    main()
