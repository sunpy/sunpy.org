import sys
import os
import ablog


sys.path.append(os.path.abspath('exts'))
extensions = ['sphinx.ext.githubpages', 'ablog', 'sphinxcontrib.rawfiles', 'cards']
templates_path = [ablog.get_html_templates_path()]

# Files you want to copy
rawfiles = ['CNAME']

disqus_shortname = 'sunpy-website'
blog_baseurl = 'https://duygukeskek.github.io/sunpy-website/blog.html'

blog_feed_fulltext = True
blog_feed_length = 10
blog_feed_archives = True

source_suffix = '.rst'
master_doc = 'index'
project = u'SunPy'
author = 'SunPy Community'
version = u''
release = u''
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
from sunpy_sphinx_theme.conf import *

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_title = 'SunPy Website' 

html_static_path = ['_static']

html_theme_options.update({'base_url': 'sunpy.org',
                           'seo_description': 'SunPy Website',
                           'navbar_pagenav': False,
                           'globaltoc_depth': 1})

html_sidebars = {
    'about': ['localtoc.html'],
    'contribute': ['localtoc.html'],
    'blog': ['searchbox.html', 'categories.html', 'archives.html'],
    'blog/**': ['searchbox.html', 'categories.html', 'archives.html'],
    'help': ['localtoc.html'],
    'posts/**': ['postcard.html'],
    'team': ['localtoc.html'],
    'newcomers': ['localtoc.html']
}

intersphinx_mapping = {'https://docs.python.org/': None}
