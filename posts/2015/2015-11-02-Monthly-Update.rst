SunPy Update - November 2015
============================

.. post:: 2 November 2015
   :author: Stuart Mumford
   :tags: sunpy, status, monthly
   :category: Update

Hello all,

Time for a quick rundown of October.

October News
============

* `Python 3 Port <#>`_
* `Astropy 1.1 beta <#>`_

Python 3 Port
-------------

One of the major features scheduled for the 0.7 release is Python 3 compatibility.
To this end a subpackage by subpackage porting effort is underway.
The master branch of SunPy will now install and import using Python 3.4 or 3.5 (3.3 is untested) and the map, data, util, cm, time, image, io and sun subpackges now have their tests passing.
The next major effort is to port the large net submodule across.
If anyone has any time to contribute to the effort, please drop in to IRC and find me (Cadair).

Astropy 1.1 Beta
----------------

Just a quick note to let you all know that the 1.1 release of Astropy is getting close.
This release contains a couple of cool things for SunPy, as well as some improvements to coordinates which will make things easier for SunPy coordinates, it contains an implementation of astropy table with an index column, which makes it possible to store timeseries in astropy tables.

Coming up in November
=====================

* `Weekly developer meetings. <#>`_

Weekly Developer Discussions
----------------------------

The weekly meetings will be continuing this month, they are now at 1700UTC each week, and will be for the next ~6 months.
We are using Google Hangouts and you can be notified of them by following our `Google+ page <https://plus.google.com/+SunpyOrg/posts>`_ (normally the join link is posted in IRC once the meeting has started).
These meetings are also recorded and uploaded to YouTube, so you can catch up even if you can not attend in person.

Links to November's meetings are below:

* Meeting on `2/11 <https://plus.google.com/events/ckedfpc7tsbjtqfsajv1vmdbkps>`_
* Meeting on `9/11 <https://plus.google.com/events/c6p3updmqne67e92gfqujbcvfho>`_
* Meeting on `16/11 <https://plus.google.com/events/cggbdujsjamcg7j4m5ssri5jb8c>`_
* Meeting on `23/11 <https://plus.google.com/events/c516k5sn5l7q05gft7hbi5m5adk>`_
* Meeting on `30/11 <https://plus.google.com/events/ca9ag6c6mg66uibvtkjbqnlno28>`_

Getting in touch
----------------

Finally, I wanted to remind everyone about our public communication methods.
We have two mailing lists, `SunPy <https://groups.google.com/forum/#!forum/sunpy>`_ and `sunpy-dev <https://groups.google.com/forum/#!forum/sunpy-dev>`_, the main SunPy list is used for general questions and announcements, and the sunpy-dev list is used for developer discussion and organisational emails.
We also have the IRC channel (`#SunPy <https://kiwiirc.com/client/irc.freenode.net/#SunPy>`_ on Freenode), which normally has someone hanging out in it, and is an excellent place to get some real-time help, or to just come for a chat.
We also have our `Google+ page <https://plus.google.com/+SunpyOrg/posts>`_ and a `Twitter <https://twitter.com/sunpyproject>`_ account.

Happy Pythoning,
Stuart
