import sphinx_bootstrap_theme
import ablog

extensions = ['sphinx.ext.githubpages','ablog']

templates_path = [ablog.get_html_templates_path()]

disqus_shortname = 'sunpy-website'
blog_baseurl = 'https://duygukeskek.github.io/sunpy-website/blog.html'

blog_feed_fulltext = True
blog_feed_length = 10
blog_feed_archives = True

source_suffix = '.rst'
master_doc = 'index'
project = u'SunPy'
author  = 'SunPy'
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
html_theme_options.update({
    'globaltoc_depth': 1
})

html_sidebars = {'about': ['localtoc.html'], 'contribute': ['localtoc.html'], 'help': ['localtoc.html']}
man_pages = [
(master_doc, 'sunpy', u'SunPy Documentation',
[author], 1)]
texinfo_documents = [
(master_doc, 'SunPy', u'SunPy Documentation',
author, 'SunPy', 'One line description of project.',
'Miscellaneous'),
]
intersphinx_mapping = {'https://docs.python.org/': None}
