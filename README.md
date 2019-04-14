# SunPy Website

Here lays the source code for the SunPy website.

## Background

This site makes use of [Sphinx](https://www.sphinx-doc.org/en/stable/), and was built upon [Bootstrap](https://getbootstrap.com) via the [Sphinx Bootstrap theme](https://github.com/ryan-roemer/sphinx-bootstrap-theme).
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

Blog posts can be added by creating a new text file in the `posts/<current year>` directory.
The filename must use the following naming convention `YEAR-MONTH-DAY-title.{ext}` and be written in one of the following formats:

* [RST](https://www.sphinx-doc.org/en/stable/rest.html) formatted text, `ext=rst`,
* [Jupyter notebook](https://jupyter.org/), `ext=ipynb`; (notebooks are converted to RST using the [nbsphinx](https://nbsphinx.readthedocs.io) extension)

### RST

If you write your post in RST formatted text, each file must also contain the following header for Sphinx via [Ablog](https://github.com/sunpy/ablog) to parse the post properly:

```rst
<Title>
=========

.. post:: <Date>
   :author: <Name>
   :tags: <Tag list with commas>
   :category: <One of the below>
```

### Jupyter Notebook

When writing posts as Jupyter notebooks, the first cell should be a Markdown cell with the title as a top level heading (i.e. using a single `#`) and the second cell should be a raw cell containing the following

```rst
.. post:: <Date>
   :author: <Name>
   :tags: <Tag list with commas>
   :category: <One of the below>
   :exclude:

   <Short description of post>
```

You might have to open the notebook in a text editor and change the "metadata" for the post cell to include the following

```
   "metadata": {
    "raw_mimetype": "text/restructuredtext"
   },
```

The short description will appear as a preview of your post on the blog page. See the [nbsphinx docs](https://nbsphinx.readthedocs.io/raw-cells.html) for information on making raw notebook cells compatible with Sphinx and RST.

Additionally, Sphinx will automatically add a link to the interactive version of your notebook, hosted on [Binder](https://mybinder.org/), to the top of your post. If your notebook requires any other dependencies besides SunPy (or its dependencies), they will need to be added to `binder/requirements.txt`.

### Metadata

Please note that the date for the post is different to the way it is written for the blog filename.
Since this date is reader facing, we want month day year **e.g.,** 14 May 2056.
Also we try to enforce one line per sentence.

The current range of categories we have "officially" are:

* Release
* Update
* GSoC
* SOCIS
* Tutorial

Please select the one that is more appropriate, for many `Update` would be enough.

For tags, you can choose what you prefer for your post but please don't use any that are in the categories list.

## Colors

The colors used in the site are:

* #444444
* #FE7900
* #BDBDBD

## Miscellaneous

Some things to watch out for:

* do not use bare colons inside your post title. If you really need a colon use `&#58;`
