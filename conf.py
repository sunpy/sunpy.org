import os
import sys
from urllib.request import urlretrieve

import ablog
from sunpy_sphinx_theme.conf import *  # NOQA

sys.path.append(os.path.abspath("exts"))
extensions = [
    "ablog",
    "cards",
    "myst_parser",
    "nbsphinx",
    "rawfiles",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinxext.opengraph",
]
myst_update_mathjax = False
templates_path = [ablog.get_html_templates_path(), "_templates"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sunpy": ("https://docs.sunpy.org/en/stable", None),
    "astropy": ("https://docs.astropy.org/en/stable", None),
    "ndcube": ("https://docs.sunpy.org/projects/ndcube/en/stable", None),
    "drms": ("https://docs.sunpy.org/projects/drms/en/stable/", None),
    "aiapy": ("https://aiapy.readthedocs.io/en/stable/", None),
}

rawfiles = ["jitsi.html", "issues.html", "chat.html", "community_meeting_agenda.html"]
mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"
disqus_shortname = "sunpy-org"
blog_baseurl = "https://sunpy.org/"
blog_feed_fulltext = True
blog_feed_length = 10
blog_feed_archives = True

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
exclude_patterns = [
    "posts/*/.ipynb_checkpoints/*",
    ".github/*",
    ".history",
    "github_submodule/*",
    "LICENSE.md",
    "README.md",
    "_build/*",
    "CITATION.rst",
]
master_doc = "index"
project = "SunPy"
author = "SunPy Project"
copyright = "SunPy Project"
show_sphinx = True
version = ""
release = "main"
language = "en"

pygments_style = "sphinx"

default_role = "obj"
html_title = "sunpy.org"
html_static_path = ["_static"]
html_extra_path = ["_static/img"]
html_theme_options.update(
    {
        "navbar_pagenav": False,
        "globaltoc_depth": 1,
        "on_rtd": False,
        "copyright_html": """
<a style= "padding-left: 10px;" rel="licence" href="https://creativecommons.org/licenses/by/4.0/">
<img src="https://i.creativecommons.org/l/by/4.0/80x15.png">
</a>
""",
    }
)

html_sidebars = {
    "index": None,
    "about": ["localtoc.html"],
    "coc": ["localtoc.html"],
    "contribute": ["localtoc.html"],
    "blog": ["searchbox.html", "categories.html", "archives.html"],
    "blog/**": ["searchbox.html", "categories.html", "archives.html"],
    "help": ["localtoc.html"],
    "posts/**": ["postcard.html"],
    # Sphinx dosen't seem to support toctrees relative to an index, so I hacked it.
    "project/index": ["projecttoc.html"],
    "project/roles": ["rolestoc.html"],
    "project/affiliated": ["affiliatedtoc.html"],
}

# nbsphinx options
nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base=None) %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::

        This blog post was written in a `Jupyter notebook`__.
        Click here for an interactive version:
        :raw-html:`<a href="https://mybinder.org/v2/gh/sunpy/sunpy.org/{{ env.config.release }}?filepath={{ docname }}"><img alt="Binder badge" src="https://mybinder.org/badge.svg" style="vertical-align:text-bottom"></a>`

    __ https://github.com/sunpy/sunpy.org/blob/{{ env.config.release }}/{{ docname }}
"""
# sphinxext-opengraph
ogp_site_url = "https://sunpy.org/"
ogp_image = "https://raw.githubusercontent.com/sunpy/sunpy-logo/master/generated/sunpy_logo_word.png"
ogp_description_length = 300
ogp_type = "website"

urlretrieve(
    "https://raw.githubusercontent.com/sunpy/sunpy/main/sunpy/CITATION.rst",
    filename="CITATION.rst",
)
