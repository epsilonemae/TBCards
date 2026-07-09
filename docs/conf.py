import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "TBCards"
copyright = "Aspen A.M. Meissner"
author = "Aspen A.M. Meissner"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]  # noqa

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
