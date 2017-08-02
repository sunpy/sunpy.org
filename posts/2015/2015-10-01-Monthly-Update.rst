SunPy Update - October 2015
===========================

.. post:: 1 October 2015
   :author: Stuart Mumford
   :tags: sunpy, status, monthly
   :category: Update

I wanted to keep people in the loop about what is happening in the SunPy project, so I thought I would start sending out monthy updates about things that have happened and things that are going to happen.
This update might be a little longer than usual due to the fact it's the first one, and I want to get everyone up to speed.
Before I start I just wanted to introduce myself just incase any of you have had the fortune of not knowing.
I am Stuart Mumford, I submitted my PhD thesis last week at the University of Sheffield.
I am currently lead developer of the SunPy project (again) having taken over from Albert.

September News
==============

* `SunPy 0.6.1 released <#>`_
* `Three summer students succesfully completed their projects <#>`_
* `SunPy board meeting <#>`_

SunPy 0.6.1
-----------

0.6.1 contained a few bug fixes, mainly to the new WCS implementation because it was not working correctly with old-style headers.
For the release announcement `see here: <https://groups.google.com/forum/#!topic/sunpy/Sg-ucpW-9Y>`_

Summer Students
---------------

This year we were lucky enough to have three summer students, two through Google Summer of Code (GSOC) and one through ESAs Summer of Code in Space (SOCIS).

Rupak Kumar Das worked on ginga improvements for multi-dimensional data, for anyone who has worked on IRIS or ground-based data using the CRISPEX software, ginga now has some of the core features you might find useful.
The main things that have been implemented are 2D slit support when drawing paths on the image, mouse over line profiles and saving of animations and data.
This is on top of the existing features in ginga which make it an excellent graphical tool for viewing FITS files.
You can `check it out here: <https://ginga.readthedocs.io/en/latest/>`_

Ankit Kumar worked on implementing support for more sources in the sunpy.lightcurve module, focusing on SEP instruments on SOHO and STEREO.
He has been implementing downloaders and readers for these new data sources on top of the new downloader class which will be released in SunPy 0.7. His work is in PR `#1476 <https://github.com/sunpy/sunpy/pull/1476>`_

Alex Hamilton, our SOCIS student, has implemented the first SunPy Affiliated Package, which is a framework for magnetic field extrapolations in Python.
The package currently provides a simple potential field extrapolator and tools for visulaising the output using MayaVi.
The goal of this project was to implement a base from which more extrapolation algorithms could be implemented or wrapped into Python.
Finalisation work is still on going with more documentation and an example gallery to come, for more information `checkout the repository here: <https://github.com/sunpy/solarbextrapolation>`_

SunPy Board Meeting
-------------------

The SunPy project is managed by the SunPy board, information on the structure of the SunPy project can be found in its founding
`document <https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0002.md>`_ .
The board holds roughly quarterly meetings and discusses the general direction of the project, sponsorship and other things, not normally, directly linked to library development.

The minutes of this meeting (and previous meetings) can be seen `here. <https://github.com/sunpy/sunpy/wiki/Minutes-of-SunPy-Board-Meeting-2015-09-21>`_

The highlights are:

* Kevin Reardon from the DKIST project has joined the board to further collaboration between DKIST and SunPy.
* Stuart Mumford has been nominated as lead developer.
* Future board meetings will be advertised on the SunPy lists and people are welcome to observe.

Coming up in October
--------------------

* `Weekly developer meetings <#>`_
* `Merging of the new downloader branch <#>`_

Weekly Developer Discussions
----------------------------

These weekly meetings have been on hiatus recently as Albert and I have been busy and we were sharing reposnsibility for organising them.
As I have now submitted my thesis, and therefore have marginally more time on my hands they will be resuming.
These meetings take place at 1600UT (until UK daylight savings kicks in) on Mondays, currently we use Google Hangouts and you can be notified of them by following our `Google+ page <https://plus.google.com/+SunpyOrg/posts>`_ (normally the join link is posted in IRC once the meeting has started).
These meetings are also recorded and uploaded to YouTube, so you can catch up even if you can not attend in person.

Links to Octobers meetings are below:

* Meeting on `5/10 <https://plus.google.com/events/c6bro29vfok8q3tramjor0m14mg>`_
* Meeting on `12/10 <https://plus.google.com/events/cdtdo3grb8g5264qnb09a4s54is>`_
* Meeting on `19/10 <https://plus.google.com/events/courcu6oondna63l7jiu89l698o>`_
* Meeting on `26/10 <https://plus.google.com/events/cdd6f6nttuu388enddjqm53rp3o>`_

Merging in the new 'FIDO' Downloader
------------------------------------

After the 0.6 release, it was decided that the focus of the next release (0.7) would be the Lightcurve module and the new downloader that was built to work with it.
To this end the first priority at the moment is to get the unidown branch merged into SunPy master.
For anyone who wishes to contribute testing this branch is an excellent place to start, the PR can be found `here <https://github.com/sunpy/sunpy/pull/1300>`_

Getting in touch
----------------

Finally, I wanted to remind everyone about our public communication methods.
We have two mailing lists, `SunPy <https://groups.google.com/forum/#!forum/sunpy>`_ and `sunpy-dev <https://groups.google.com/forum/#!forum/sunpy-dev>`_, the main SunPy list is used for general questions and announcements, and the sunpy-dev list is used for developer discussion and organisational emails.
We also have the IRC channel (`#SunPy <https://kiwiirc.com/client/irc.freenode.net/#SunPy>`_ on Freenode), which normally has someone hanging out in it, and is an excellent place to get some real-time help, or to just come for a chat.
We also have our `Google+ page <https://plus.google.com/+SunpyOrg/posts>`_ and a `Twitter <https://twitter.com/sunpyproject>`_ account.

I hope this email wasn't so long nobody made it to the end. I will try and keep future ones a little shorter.

Happy Pythoning,
Stuart
