import sphinx_bootstrap_theme
import ablog

extensions = ['sphinx.ext.githubpages','ablog']

templates_path = ['_templates', ablog.get_html_templates_path()]
html_static_path = ['_static']

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
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False

html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

html_favicon ='_static/img/favicon-32.ico'
html_theme_options = {
	'navbar_pagenav': False,
	'source_link_position': False,
	'bootswatch_theme': 'flatly',
	'navbar_site_name': "Site",
	'navbar_title': 'sunpy',
	'navbar_links': [("About", "about.html", 1),
					 ("Blog", "blog.html", 1),
					 ("Documentation", "#"),
					 ("Support Us", "contribute.html", 1),
					 ("Affiliated Projects", "affiliated.html", 1),
					 ("Get Help", "help.html", 1),
					 ("The Team", "team.html", 1),
					 ],
					 'globaltoc_depth': 1
}
html_sidebars = {'about': ['localtoc.html'], 
				 'contribute': ['localtoc.html'],
				 'help': ['localtoc.html'],
				 'blog': ['postcard.html','recentposts.html','categories.html','archives.html',]
}
texinfo_documents = [(master_doc, 'SunPy', u'SunPy Documentation',author, 'SunPy', 'One line description of project.','Miscellaneous')]