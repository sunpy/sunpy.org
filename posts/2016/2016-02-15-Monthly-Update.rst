SunPy Update - February 2016
============================

.. post:: 15 February 2016
   :author: Stuart Mumford
   :tags: sunpy, status, monthly
   :category: Update

Hello all,

Sorry for the delay to the January update, but it is here at last.

There has been quite a lot going on in the six weeks since the last update, thanks to David for collating most of this news.

January and February News
=========================

SunPy
-----

SunPy is using now the latest version of `astropy-helpers <https://github.com/astropy/astropy-helpers>`_ (v1.1.1) and astropy's `ci-helpers <https://github.com/astropy/ci-helpers>`_ which eases the maintenance of the package and the tests running.

Few new "badges" has been added now to the readme file in the repository, these badges show the status of the repository, like number of downloads, whether the development version is passing all its tests or not (via `Travis <https://travis-ci.org/sunpy/sunpy>`_ and `appveyor <https://ci.appveyor.com/project/sunpy/sunpy>`_ ), the amount of code tested, two `quality <https://landscape.io/github/sunpy/sunpy/>`_ `measurements <https://www.quantifiedcode.com/app/project/9edd3e28230840038713e1c7dc3eb141>`_ and one that shows `the impact in academia <http://depsy.org/package/python/sunpy>`_.
All these are little helpers to keep an eye on the quality and usage of our beloved project.

One of the important tests problem solved in this last month has been the figures tests.
Some visualisation is being tested for every new contribution people submit - as with any other tests - and if they differ the test suite tells us
something has changed (or is broken). The figures tested are in the new `sunpy-figure-test <https://github.com/sunpy/sunpy-figure-tests>`_ repository.
There you can see the figures and compare them with the previous versions - including the environment used to create them.

OpenAstronomy workshop
----------------------

January started with a 5-day workshop which extended a 2-day `software-carpentry <http://software-carpentry.org/>`_ bootcamp with an
introduction to Astropy and SunPy.
Read more about the success of the workshop in the `openastronomy blog <http://openastronomy.org/2016/01/15/Workshop.html>`_.
This workshop will be repeated in the future, but if you want to organise one don't hesitate to contact us about it.

Coming up
=========

Google Summer of Code
---------------------

SunPy is joining many other teams to apply together under the OpenAstronomy umbrella to Google Summer of code.
If you want to mentor or help mentoring one of the `summer projects already proposed <https://github.com/sunpy/sunpy/wiki/GSoC-2016-Ideas-Page>`_ contact us.
If you have some ideas or see that there's something missing in SunPy... tell us and we can create a project plan for that.

If you are a candidate student, please, don't wait till the last week to get in touch.
Get yourself known in the IRC and mailing list... we don't have all the projects ready yet but they will be soon.
Don't forget that a contribution before applying is compulsory to being accepted.

Weekly Developer Discussions
----------------------------

The weekly meetings will be continuing this month, they are at 1700UTC each week.
We are using Google Hangouts and you can be notified of them by following our Google+ page (normally the join link is posted in IRC once the meeting has started).
These meetings are also recorded and uploaded to YouTube, so you can catch up even if you can not attend in person.

Links to coming meetings can are below:

* Meeting on `15/2 <https://plus.google.com/events/cqj6t37am6vdn73hvb0njc3fv8>`_
* Meeting on `22/2 <https://plus.google.com/events/gi6kd6e97s8mjh9skif8qj0tn8>`_
* Meeting on `29/2 <https://plus.google.com/events/jt7tb05t7k6ct9cqk4i3lnbjj0>`_

Reviewing Pull Requests
-----------------------

As always, reviews on pull requests are always welcome, you don’t have to have merge permissions or anything other than a GitHub account to review PRs.
You can find a list of all the PRs that need reviewing `here <https://plus.google.com/events/jt7tb05t7k6ct9cqk4i3lnbjj0>`_.

Getting in touch
----------------

Finally, I wanted to remind everyone about our public communication methods.
We have two mailing lists, SunPy and sunpy-dev, the main SunPy list is used for general questions and announcements, and the sunpy-dev list is used for developer discussion and organisational emails.
We also have the IRC channel (#SunPy on Freenode), which normally has someone hanging out in it, and is an excellent place to get some real-time help or to just come for a chat.
We also have our Google+ page and a Twitter account.

Happy Pythoning,
David and Stuart
