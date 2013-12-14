
# Resources
This site makes use of Jekyll, it was build with Bootstrap.

[Shopify](http://docs.shopify.com/themes/liquid-basics)

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

Some things to watch out for
* do not use bare colons inside your post title. If you really need a colon use `&#58;`
