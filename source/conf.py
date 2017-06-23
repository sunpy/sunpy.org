import sphinx_bootstrap_theme

extensions = ['sphinx.ext.intersphinx','sphinx.ext.githubpages']

templates_path = ['_templates']
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
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_favicon ='_static/img/favicon-32.ico'
html_theme_options = {
	'navbar_pagenav': False,
	'source_link_position': False,
	'bootswatch_theme': 'flatly',
	'navbar_site_name': "Site",
	'navbar_title': 'sunpy',
	'navbar_links': [("About", "about.html", 1),
					 ("Blog", "blog.html", 1),
					 ("Docs", "#"),
					 ("Contribute", "contribute.html", 1),
					 ("Affiliated Packages", "affiliated.html", 1),
					 ("Help", "help.html", 1),
					 # ("GitHub", "https://github.com/DuyguKeskek/sunpy-website", True),
					 ],
					 'globaltoc_depth': 1
}
html_static_path = ['_static']
html_sidebars = {'about': ['localtoc.html'], 'contribute': ['localtoc.html'], 'help': ['localtoc.html']}
man_pages = [(master_doc, 'sunpy', u'SunPy Documentation',[author], 1)]
texinfo_documents = [(master_doc, 'SunPy', u'SunPy Documentation',author, 'SunPy', 'One line description of project.','Miscellaneous')]
intersphinx_mapping = {'https://docs.python.org/': None}