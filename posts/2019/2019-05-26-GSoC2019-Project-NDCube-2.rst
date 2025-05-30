GSoC 2019: Community Bonding Period — II
========================================
.. post:: May 26, 2019
   :author: Yash Sharma
   :tags: GSoC, NDCube
   :category: Google Summer of Code

|image0|

So as I discussed in my earlier posts about how I started my Community
Bonding Period, so this post deals with the remaining tasks that I did
for the remaining part of the Community Bonding Period. ### Starting
with the Week 01 tasks

I had a chat with ``@Cadair`` who is my mentor, and we decided that I
start with the tasks of the
first part of
the project. GitHub has these awesome project tabs, which help you sort
out all the tasks and todo for a GitHub project, and even though it is a
simple feature, it makes managing the stuff look neat and easy.

So I approached the tasks as it was given, and by refactoring each of
the methods, I realised that as simple as the work sounds, there is a
lot of overhead to cover, before a method is refactored. Even though, I
have written lots of tests in my short developer period, but
contributing and making changes to a new repository requires a lot of
learning and unlearning, especially modifying the tests.

After going through each of the test cases, I realised, that it is a
different beast all together. However the overhead does make a lot of
sense, as it makes sure that the intention of a developer is shown as
he/she thinks while coding up the features.

Making progress with the tasks : Coding 101
===========================================

As it happens, I made lot of refactoring, and I tested out each of the
methods, if they are performing as expected. The mantra for making a
successful contribution is ``Code — Test — Document`` all along. Well
lets add another dimension to it — ``Code Reviews``. Code reviews are
really important, if not the most underrated task, as I got my first
`PR <https://github.com/sunpy/ndcube/pull/169>`__, reviewed by
``@Cadair`` and ``@DanRyanIrish``.

Even though I have had my code reviewed by many people earlier, I still
was a bit nervous about going through, as Code Reviews differ from the
person who are reviewing. I got few suggestions as they went through,
and believe me it was a really good experience, as they shared how
coding style should be maintained for a given codebase, and how
wandering away from them can be a nightmare for maintainers.

Overall, my PR hasn't been merged, as it is a bigger part of my project,
so lot more changes are expected, before it gets merged.

Contributing to SunPy1.0
========================

While the title sounds a bit misleading, as I have made PRs to
``SunPy/NDCube`` it does not directly affect ``SunPy``, but I have made
changes which might affect ``SunPy`` indirectly.

After completing most of the
tasks, I
decided to do something else, unrelated to my project. I had a chat with
``@Cadair`` and he suggested me to help him to fix some tests which were
failing in ``SunPy/NDCube``. As ``SunPy`` was quite near to be released,
so some changes were breaking ``SunPy/NDCube``. On skimming through, I
wasn't able to make any sense of what was happening, so I used debugging
techniques to figure out the issue. Those who don't know about debugging
and the techniques, believe me it's *Just Like Heaven.*

Python has a lot of tools by its toolbox, one of the most powerful and
the elementary tools for debugging is ``breakpoint()``. It is supported
in ``Python3.7`` , and it turned out as a saviour for me.
``Breakpoint()`` helps in stopping the flow of code at the point of time
where the code breaks; where stuff happens the way it shouldn't have
happened. It helps us in inspecting the state of the object and the
logic of the code, so you can understand the context of the issue
generated by the failing tests.

Enough of the technical jargons, let me discuss the work that I did,
which marked the ending of the Community Bonding Period. After countless
debugging, I found that the ``plotting`` code of ``NDCube`` used
``pixel-values`` instead of ``pixel-edges``, and since ``SunPy`` had
changed its API, now requesting ``pixel-edges`` instead of
``pixel-values`` . I made a PR for changing the support to
``pixel-edges`` instead of ``pixel-values``. I got a
`PR <https://github.com/sunpy/ndcube/pull/174>`__ merged for ``1D``
plotting, but the `PR <https://github.com/sunpy/ndcube/pull/176>`__ for
``>1D`` needs to be merged.

Links to previous post
======================

-  First meeting and plan of action —
   `Link <https://medium.com/@yashrsharma44/first-meeting-and-plan-of-action-60cedf1e2fd>`__

.. |image0| image:: https://cdn-images-1.medium.com/max/1144/0*2ViVFo_JvjR1r5ih.png
