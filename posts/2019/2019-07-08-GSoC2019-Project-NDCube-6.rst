[Week 04] — Climbing the Everest — 02
=====================================

.. post:: July 08, 2019
   :author: Yash Sharma
   :tags: GSoC, NDCube
   :category: GSoC

|image0| Sustaining the journey!

    This blog post deals with the entry of tasks that I did for the 4th
    week for the project under Google Summer of Code 2019.

Using the Slicing API
=====================

The previous week, I had went through the docs, and played with some of
the test cases of slicing. Now I was fairly ready to implement them in
``NDCube`` . I had long chats with my mentor, ``@Cadair`` who was always
free to hear out my doubts, sometimes suggesting alternative ways to
approach, filling me with hints and tips to approach the problem, rather
than serving it out in a platter. This was really crucial and ensured
that I enjoy the coding without hampering the learning part.

So I used the new slicing API, which was written by ``@Cadair`` and
``@astrofrog``, and boy, it was a breeze in using it, as it required
minimal code refactoring for performing slicing of wcs object. Since an
``NDCube`` object contains ``WCS``, ``extra_coords`` and bunch of other
helper methods, so the slicing of ``extra_coords`` was something, that
wasn’t implemented earlier, and I had to do it from scratch. I had a
talk with ``@Cadair``, who warned me about thinking out the slicing of
``extra_coords`` in advance, and it turned out to be true, as it was
another beast to be taken care of.

Rewriting the slicing API of extra\_coords
==========================================

So far, after implementing the slicing of ``WCS`` object, I was left
with refactoring the code of slicing API(more of a redesign) of
``extra_coords`` and I was up to the task. After consulting numerous
examples and test cases for the ideal working of sliced
``extra_coords``, I went after writing up the slicing API. It was
confusing, but at the same time, I had broken down the code rewriting
into small subparts, and I finished off each of the small portions, as I
consolidated my way towards completing my work.

Finishing up the refactoring
============================

Well, after testing out numerous cases(well not exactly a lot of
examples!), I finally pushed my changes to GitHub, and a
`PR <https://github.com/sunpy/ndcube/pull/169>`__ was made for the
changes that I made. The code was written, and I was mostly convinced
about the behavior of the code, though the test suite was failing, and
needed to be resurrected. This was ok, for me the most challenging part
of the project was implemented, and considering the plan that I had
earlier chalked out while rewriting the API, I was sure that it would
work as intended.

Task for the next week
======================

So, after rewriting and installing the new API for slicing, I was now
left with modifying the slicing tests, partly because the type of object
returned by APE14 (the API that I was implementing) was different from
the earlier ones while having the same return values. So that was
considered by me more of a manual work rather than requiring the
brainstorming stuff. In a way, I was happy to work with the tests, for
it was mentally frustrating to cover such an intense task in a week, and
I wanted to cherish the way how the new API was working, and what a way
to do that was the testing. So I am looking forward to it.

Link to my previous post
========================

-  [Week 03] — Climbing the Everest — 01
   —`Link <https://medium.com/@yashrsharma44/week-03-climbing-the-everest-01-6d9508a819a>`__

.. |image0| image:: https://cdn-images-1.medium.com/max/1144/0*GuhDaaal6sTcCY1K