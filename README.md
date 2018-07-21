# SunPy Website

[![Build Status](https://travis-ci.org/sunpy/sunpy.github.io.svg?branch=master)](https://travis-ci.org/sunpy/sunpy.github.io)

Here lays the source code for the current SunPy website.

## Background

This site makes use of [Sphinx](http://www.sphinx-doc.org/en/stable/), and was built upon [Bootstrap](http://getbootstrap.com) via the [Sphinx Bootstrap theme](https://github.com/ryan-roemer/sphinx-bootstrap-theme).
So each static page is written in reStructuredText (RST).

We use [Netlify](https://www.netlify.com/) deploy and host the [website](https://app.netlify.com/sites/sunpy/overview).

## Testing Locally

To setup your computer to run this site locally, you need to install the various Python packages in the [requirements.txt](https://github.com/sunpy/sunpy.github.io/requirements.txt) at the top level of this repository.

You will *WANT* to test any changes you have made to the website.
To do this, we have a Makefile that you should use:

```bash
    make html
```

This will build a collection of html pages under `_build/html` and you can open the `index.html` using your browser of choice.

## Creating a PR

When you are happy with any changes you have made to the website.
We recommend building the website and making sure that everything is building fine.
You should see no warnings for the build.

Once you are sure everything is in order, you can send in a PR to this repository.
If you are unfamiliar with this, please see this guide from [GitHub.](https://help.github.com/articles/about-pull-requests/)

## PR Review

When a PR is opened, two continuous integration services will trigger.
We use [Travis](https://travis-ci.org/) to test the build and if it fails we wil get a full build log to debug.
While [Netlify](https://www.netlify.com/) will create a preview of any content or style changes.

Both of these services must pass before the PR will be merged, furthermore, one review is required before a PR can be merged as well.

## Creating a Blog Post

Blog posts can be added by creating a new text file in the _posts/<current year> directory.
The filename must use the following naming convention `YEAR-MONTH-DAY-title.{ext}` and be written in one of the following formats:

* [RST](http://www.sphinx-doc.org/en/stable/rest.html) formatted text, `ext=rst`,
* [Jupyter notebook](http://jupyter.org/), `ext=ipynb`; (notebooks are converted to RST using the [nbsphinx](http://nbsphinx.readthedocs.io) extension)

If you write your post in RST formatted text, each file must also contain the following header for Sphinx via [Ablog](https://github.com/sunpy/ablog) to parse the post properly:

```rst
<Title>
=========

.. post:: <Date>
   :author: <Name>
   :tags: <Tag list with commas>
   :category: <One of the below>
```

When writing posts as Jupyter notebooks, the first cell should be a Markdown cell with the title as a top level heading (i.e. using a single `#`) and the second cell should be a raw cell containing the post information listed above. See the [nbsphinx docs](http://nbsphinx.readthedocs.io/raw-cells.html) for information on making raw notebook cells compatible with Sphinx and RST.

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
