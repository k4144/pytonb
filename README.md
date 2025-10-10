[![CI](https://github.com/k4144/pytonb/actions/workflows/release.yml/badge.svg?branch=main)](https://github.com/k4144/pytonb/actions/workflows/release.yml)
[![PyPI version](https://img.shields.io/pypi/v/pytonb)](https://pypi.org/project/pytonb/)
[![Python versions](https://img.shields.io/pypi/pyversions/pytonb)](https://pypi.org/project/pytonb/)
[![Wheel](https://img.shields.io/pypi/wheel/pytonb)](https://pypi.org/project/pytonb/)
[![License](https://img.shields.io/github/license/k4144/pytonb)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![codecov](https://codecov.io/gh/k4144/pytonb/branch/main/graph/badge.svg)](https://codecov.io/gh/k4144/pytonb)
[![Downloads](https://static.pepy.tech/badge/pytonb)](https://pepy.tech/project/pytonb)
[![Downloads/month](https://static.pepy.tech/badge/pytonb/month)](https://pepy.tech/project/pytonb)
[![Docs](https://readthedocs.org/projects/pytonb/badge/?version=latest)](https://pytonb.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/k4144/pytonb/main.svg)](https://results.pre-commit.ci/latest/github/k4144/pytonb/main)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/k4144/pytonb/badge)](https://securityscorecards.dev/viewer/?uri=github.com/k4144/pytonb)
[![Type checking: mypy](https://img.shields.io/badge/type%20checking-mypy-blue)](https://github.com/python/mypy)

![Status](https://img.shields.io/badge/status-alpha-orange)
![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)



## simple converter for pa files vs notebooks
### example:
´´´
from pytonb import write_notebook, write_script
write_notebook('filename.py')
´´´
### writes notebook filename.ipynb. optional parameters:
### * save_name, notebook file name
### * use_ast, ignore notebook markers (In[ ]:), create a separate cell for each function
´´´
write_script('filename.ipynb')
´´´
´### writes filename.py, including notebook markers (In[ ]:). optional parameters:
### * save_name, py file name  
### * overwrite, write over existing py file
### example syncing notebook to py file:
´´´
from pytonb import sync, sync_folder
sync('filename.ipynb')
´´´
### sync ipynb file to filename.py. optional parameters:
### * py_path: py file save path
### * delay: delay in s before checking change
### example syncing folder to py files:
´´´
from pytonb import sync, sync_folder           
sync_folder('folder')
´´´
### sync ipynb files in folder to corresponding py files.  optional parameters:
### * recursion_level: sync ipynb files up to this depth 
### * delay: delay in s before checking change

