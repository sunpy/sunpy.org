# Background
This site makes use of [Jekyll](http://jekyllrb.com), and was build upon [Bootstrap](http://getbootstrap.com). Static pages can be written using Markdown. Jekyll makes use of [Shopify](http://docs.shopify.com/themes/liquid-basics) as its programming language.

# Testing Locally

To setup your machine to run this site locally, you'll first need to install a few things. Please follow the 
[installation instructions](https://help.github.com/articles/using-jekyll-with-pages) provided by github.

You will likely want test any changes you've made to the site. To do this you'll have the run Jekyll and host the site locally. This can be done by running the following command inside the site directory

    bundle exec jekyll serve --watch

This will create a page hosted locally at http://localhost:4000.

# Creating a Blog Post
Blog posts can be added by creating a new text file in the _posts directory. The filename
must use the following naming convention `YEAR-MONTH-DAY-title.md` and contain [markdown](http://daringfireball.net/projects/markdown/)
formatted text. Each file must also contain the following header for Jekyll to parse
the post properly
```
---
layout: post
title: My post title
author: First Last name
---
```

## Syntax Highlighting
Jekyll has built in support for syntax highlighting of over 100 languages thanks to Pygments.
To include syntax highlighting use the following syntax

    {% highlight python %}
    def foo
      print('foo')
    end
    {% endhighlight %}

More information about highlighting is available [here](http://jekyllrb.com/docs/templates/).
Otherwise standard markdown applies for code blocks and inline code.

# Colors

The colors used in the site are

* #444444
* #fed20b
* #fe7900

# Miscellaneous 

Some things to watch out for
* do not use bare colons inside your post title. If you really need a colon use `&#58;`
