import os
import sys
from urllib.request import urlretrieve

sys.path.append(os.path.abspath("exts"))
extensions = [
    "cards",
    "myst_parser",
    "nbsphinx",
    "rawfiles",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinxext.opengraph",
    "ablog",
    "sphinx_design",
    "sphinx_reredirects",
    "sphinxcontrib.youtube",
]
myst_enable_extensions = ["colon_fence"]
myst_update_mathjax = False
templates_path = ["_templates"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sunpy": ("https://docs.sunpy.org/en/stable", None),
    "astropy": ("https://docs.astropy.org/en/stable", None),
    "ndcube": ("https://docs.sunpy.org/projects/ndcube/en/stable", None),
    "drms": ("https://docs.sunpy.org/projects/drms/en/stable/", None),
    "aiapy": ("https://aiapy.readthedocs.io/en/stable/", None),
}
rawfiles = ["meeting.html", "issues.html", "chat.html", "community_meeting_agenda.html"]
mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"
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
    ".history/*",
    "github_submodule/*",
    "LICENSE.md",
    "README.md",
    "_build/*",
    "CITATION.rst",
    ".tox/*",
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
html_theme = "sunpy"
html_title = "sunpy.org"
html_static_path = ["_static"]
html_extra_path = ["_static/img"]
html_theme_options = {"show_prev_next": False, "sst_is_root": True}

html_css_files = [
    "sunpy_org.css",
]

blog_sidebars = [
    "ablog/postcard.html",
    "ablog/recentposts.html",
    "ablog/tagcloud.html",
    "ablog/categories.html",
    "ablog/archives.html",
]

html_sidebars = {
    "*": [],
    "about": ["about-sidebar.html"],
    "coc": ["about-sidebar.html"],
    "about/**": ["about-sidebar.html"],
    "posts/**": ["ablog/postcard.html"],
    "blog": blog_sidebars,
    "blog/**": blog_sidebars,
}

redirects = {
    "project/meetings": "about/meetings",
    "project/roles": "about/roles",
    "project": "about/project",
    "project/affiliated": "affiliated",
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

# These links have anchors that linkcheck does not like
linkcheck_ignore = [
    "https://app.element.io/#/room/#sunpy:openastronomy.org",
]
linkcheck_anchors_ignore = [
    "/projects\?project=develop_sunkit-image",
    "the-executive",
    "acceptance-process-for-affiliated-packages",
    "detailed-description",
    "!forum/sunpy",
]
