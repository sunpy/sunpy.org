[Week 02] — Solving Bugs!
=========================
.. post:: June 19, 2019
   :author: Yash Sharma
   :tags: GSoC, NDCube
   :category: GSoC

|image0| 

Solving bugs for eternity!

    To those who have been my blog, it would have been a bit surprising
    for them for getting this blog-post a bit late. This has been a
    result of hectic work schedule and a little bit of procastination :P

This blog-post sums up my work for the second week of Google Summer of
Code 2019.

Telecon with my mentor
======================

As I might have mentioned(or maybe not), but my other mentor,
``@DanRyanIrish``, was away for a while now, and after discussing with
him, we managed to set up a time-slot for a telecon, for getting him
updated with my work.

The main points that we discussed were, getting this
`#PR176 <https://github.com/sunpy/ndcube/pull/176>`__ merged. We also
discussed, the progress of the main PR for the project, and how much did
I make progress. I went through my
`PR <https://github.com/sunpy/ndcube/pull/169>`__, and discussed a few
points about how I refactored the existing methods, and briefly
explained my understanding. Code reviews are necessary, and after
discussing with ``Dan`` we decided to change the logic of some part of
the code.

As I had completed most of the tasks for this week, we agreed to start
the closed `PR <https://github.com/sunpy/ndcube/pull/179>`__. This PR
helped in writing a ``FITS`` file from a ``NDCube`` object. I had
started contributing to ``NDCube`` with this PR, most of the work had
been completed. I had to rebase and write the tests and docs.

Completing the tasks
====================
Throughout this week, I had another discussion with my mentor ``Dan``,
who helped me in understanding the code of ``plotting``. The #PR176 was
failing some tests, which were part of the plotting of ``>1D``
``NDCube`` objects. I had earlier skimmed through the code of plotting
but still found understanding the code of plotting quite complex.

``Dan`` helped me in understanding the flow of code in plotting, and it
helped me in fast-tracking my work with plotting. Refactoring the tests
were much easier, though repetitive. Though the real happiness lies,
when all the tests pass, and there is a green color message, signaling
that all of your tests have passed.

Thoughts for the next week
==========================
With most of the tasks completed for refactoring ``NDCube`` with APE14
methods, it was now clear for me to take on the second stage of my
project — ``Slicing of NDCube``. Slicing by far was presumed by my
mentor ``@Cadair`` as the most complex part of the project. I was
apprised by him about how the slicing can take most of the time of the
project, so I was rather aware of that. I am planning to start playing
with the slicing, and how it used to work for ``NDCube`` earlier, and
how the behavior changes with APE14 changes. This should take a fair
amount of time, so I would hope that this gets completed within a
reasonable amount of time.

Link to my previous post
========================

-  [Week 01] — Getting Stuff Done! —
   `Link <https://medium.com/@yashrsharma44/week-01-getting-stuff-done-a751cb7eb816>`__

    Until the next blog-post, ciao-adios!

.. |image0| image:: https://cdn-images-1.medium.com/max/1144/1*qaM9LjB9PY5pwj9RDtP93g.jpeg

