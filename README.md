# sunpy.org

## Background

This site makes use of [Sphinx](https://www.sphinx-doc.org/en/stable/), and was built upon [Bootstrap](https://getbootstrap.com) via the [Sphinx Bootstrap theme](https://github.com/ryan-roemer/sphinx-bootstrap-theme).
We use [Netlify](https://www.netlify.com/) deploy and host the [website](https://app.netlify.com/sites/sunpy/overview).

## Testing Locally

To set up your computer to run this site locally, you need to install the various Python packages in the [requirements.txt](requirements.txt) at the top level of this repository.

Furthermore, there is a sub-module that we use to get certain files for the build.

```bash
git submodule update --init
```

This will initialize the submodule for you locally.

You will _WANT_ to test any changes you have made to the website.
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

When a PR is opened, [Netlify](https://www.netlify.com/) will create a preview of any content or style changes.

This must pass before the PR will be merged, furthermore, one review is required before a PR can be merged as well.

## Creating a Blog Post

Blog posts can be added by creating a new text file in the `posts/<current year>` directory.
The filename must use the following naming convention `YEAR-MONTH-DAY-title.{ext}` and be written in one of the following formats:

- [ReStructuredText (RST)](https://www.sphinx-doc.org/en/stable/rest.html) formatted text, `ext=rst`,
- [Jupyter Notebook (NB)](https://jupyter.org/), `ext=ipynb`; (notebooks are converted to RST using the [nbsphinx](https://nbsphinx.readthedocs.io) extension)
- [Markdown (MD)](https://www.markdownguide.org/cheat-sheet/) formatted text, `ext=md`,

Please also see the [ABlog documentation](https://ablog.readthedocs.io/) for more information.

### RST

If you write your post in RST formatted text, each file must also contain the following header for Sphinx via [Ablog](https://github.com/sunpy/ablog) to parse the post properly:

```rst
.. post:: <Date>
   :author: <Name>
   :tags: <Tag list with commas>
   :category: <One of the below>

<Title>
=========

```

or

```rst
:blogpost: true
:date: <Date>
:author: <Name>
:category: <One of the below>

<Title>
=========

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

The short description will appear as a preview of your post on the blog page.
See the [nbsphinx docs](https://nbsphinx.readthedocs.io/raw-cells.html) for information on making raw notebook cells compatible with Sphinx and RST.

You might have to open the notebook in a text editor and change the "metadata" for the post cell to include the following

```json
   "metadata": {
    "raw_mimetype": "text/restructuredtext"
   },
```

In theory the alternative rst style and the below markdown style should also work in this cell.

Additionally, Sphinx will automatically add a link to the interactive version of your notebook, hosted on [Binder](https://mybinder.org/), to the top of your post.
If your notebook requires any other dependencies besides SunPy (or its dependencies), they will need to be added to `binder/requirements.txt`.

### Markdown

If you write your post in markdown formatted text, each file must contain the following header for Sphinx via [Ablog](https://github.com/sunpy/ablog) to parse the post properly:

```markdown
---
blogpost: true
date: <Date>
author: <Name>
category: <One of the below>
---

# <Title>
```

### Metadata

Please note that the date for the post is different to the way it is written for the blog filename.
Since this date is reader facing, we want month day year **e.g.,** May 14 2056.
Also, we try to enforce one line per sentence.

The current range of categories we have "officially" are:

- Release
- Update
- GSoC
- SOCIS
- Tutorial

Please select the one that is more appropriate, for many `Update` would be enough.

For tags, you can choose what you prefer for your post but please don't use any that are in the categories list.

## Colors

The colors used in the site are:

- #444444
- #FE7900
- #BDBDBD

## Miscellaneous

Some things to watch out for:

- do not use bare colons inside your post title. If you really need a colon use `&#58;`
