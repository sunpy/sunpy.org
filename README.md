# SunPy Website

Here lays the source code for the current SunPy website.

## Background

This site makes use of [Sphinx](http://www.sphinx-doc.org/en/stable/), and was built upon [Bootstrap](http://getbootstrap.com) via the [Sphinx Bootstrap theme](https://github.com/ryan-roemer/sphinx-bootstrap-theme).
So each static page is written in reStructuredText (RST).

## Testing Locally

To setup your computer to run this site locally, you need to install the various Python packages in the [requirements.txt](https://github.com/sunpy/sunpy.github.io/requirements.txt) at the top level of this repository.

You will *WANT* to test any changes you have made to the website.
To do this, we have a Makefile that you should use:

    make html

This will build a collection of html pages under `build/html` and you can open the `index.html` using your browser of choice.

## Creating a Blog Post

Blog posts can be added by creating a new text file in the _posts/<current year> directory.
The filename must use the following naming convention `YEAR-MONTH-DAY-title.rst` and be written in [RST](http://www.sphinx-doc.org/en/stable/rest.html) formatted text.
 Each file must also contain the following header for Sphinx via [Ablog](https://github.com/abakan/ablog) to parse the post properly:

```rst
<Title>
=========

.. post:: <Date>
   :author: <Name>
   :tags: <Tag list with commas>
   :category: <One of the below>
```

Please note that the date for the post is different to the way it is written for the blog filename.
Since this date is reader facing, we want month day year **e.g.,** 14 May 2056.
Also we try to enforce one line per sentence.

The current range of categories we have "officially" are:

* Release
* Update
* GSoC
* SOCIS

Please select the one that is more appropriate, for many `Update` would be enough.
I am sure more will be added with time.

For tags, you can choose what you prefer for your post but please don't use any that are in the categories list.

## Colors

The colors used in the site are:

* #444444
* #FE7900
* #BDBDBD

## Miscellaneous

Some things to watch out for:

* do not use bare colons inside your post title. If you really need a colon use `&#58;`
