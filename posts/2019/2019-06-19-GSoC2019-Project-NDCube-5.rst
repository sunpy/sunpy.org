[Week 03] — Climbing the Everest — 01
=====================================
.. post:: June 19, 2019
   :author: Yash Sharma
   :tags: GSoC, NDCube
   :category: GSoC


|image0| Climbing the Everest — Starting the trek!

    This blog post deals with the entry of tasks that I did for the
    3\ *rd* week for the project under Google Summer of Code 2019.

Reading through the Docs
========================

This week marks my initial stab to\ ``slicing`` of ``NDCube``. The best
place to start with the refactoring of any code-base, or any method, is
reading through the docs, and figuring out how they work currently.
Sometimes, figuring out how the present behavior is, and what parts are
we looking to refactoring, can easily ease out the process, and help in
breaking the refactoring to small parts.

I had a look into the `astropy
docs <http://docs.astropy.org/en/stable/_modules/astropy/nddata/mixins/ndslicing.html#NDSlicingMixin>`__,
and boy, they have documented each part of the logic, explaining the
what and why of the code. Trust me for I have been contributing to
open-source projects over for more than a year, and this sounds delight
for any developer, for good docs removes the overhead of how the code
works, but to focus on the high-level overview of what we want to
achieve.

Playing with the slicing
========================

Trying out any feature is more realistic than reading about them, and so
I started with creating examples from previous tests of ``NDCube`` and
how they fit into the scheme of things. Hands down to ``@Cadair`` and
``@astrofrog``, for what a concise and behavior agnostic
`API <https://github.com/astropy/astropy/pull/8546>`__ they had made.
This abstracted most part of slicing for ``WCS`` object, that ``NDCube``
uses underneath.

The real deal starts with refactoring the slicing of ``extra_coords``.
This now had to be done using ``APE14`` methods, so I had to first try
out a few examples of slicing ``extra_coords`` before refactoring it.
Soon, after going into the rabbit hole, I realized, it would require
refactoring of internal helper methods that the slicing of
``extra_coords`` uses. This sounded way too much work, but something
that had to be done.

Rewriting the helper methods
============================

The helper methods were based on a logic, which would not apply after we
migrated to APE14. So certainly it required me to rewrite them. A common
practice that I found, while refactoring, was to go top-down. A top-down
approach would mean that you would refactor stuff which you want, to the
methods that would get refactored for working correctly. This helped me
in worrying about methods which would get affected, rather than worrying
which method needs to be refactored.

I started refactoring the helper methods but got stuck at a fundamental
point. But ``@Cadair`` came to rescue, and he suggested some attributes
of ``WCS`` which would do my job. This was really crucial as getting
stuck would have sucked out more time. This solved my problem, as I went
out re-writing the helper methods, working to a behavior as I wanted.

Tasks for the next week
=======================

This week was really busy, as I spent time in reading docs and figuring
out the most optimum plan to approach slicing. Till now it has gone
fairly gone according to plan, though more tasks still await. I keep
chugging along, trying to keep up with the required pace, as the phase
containing the real challenge has arrived.

    “I will come again & conquer you because as a mountain you can’t
    grow, but as a human, I can.” — Sir Edmund Hillary

Link to my previous post
========================

-  [Week 02] — Solving Bugs! —
   `Link <https://medium.com/@yashrsharma44/week-2-solving-bugs-fb7e2eff576e>`__

.. |image0| image:: https://cdn-images-1.medium.com/max/1144/0*O02irLG83RzAyKCm.jpg

