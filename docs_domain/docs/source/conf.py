# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sales'
copyright = '2026, Platon Zhuman'
author = 'Platon Zhuman'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]/"src"))

extensions = [
    "myst_parser",
    "sphinx.ext.autodot", #автоматический сбор докстринг
    "sphinx.ext.napoleon", # поддержка стандартов докстринг
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode"
]

sourse_suffic = {
    ".md": "markdown",
    ".rst": "restructuredtext",

}

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
