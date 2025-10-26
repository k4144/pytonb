# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pytonb'
copyright = '2025, k4144'
author = 'k4144'
release = 'v1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys, pathlib
 
sys.path.insert(0, pathlib.Path(__file__).resolve().parents[1] / "src")
extensions = [
      "sphinx.ext.autodoc",
      "sphinx.ext.napoleon",        # Google/Numpy docstrings
      "sphinx_autodoc_typehints",   # use PEP 484 hints in docs
  ]



templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
