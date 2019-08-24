Google Summer of Code 2019 \| Final Report \| OpenAstronomy \| NDCube
=====================================================================

.. post:: August 24, 2019
   :author: Yash Sharma
   :tags: GSoC, NDCube
   :category: GSoC

Google Summer of Code 2019 \| Final Report \| OpenAstronomy \| NDCube
---------------------------------------------------------------------

.. figure:: https://cdn-images-1.medium.com/max/2000/0*uRGLzjnCFvoPcs7F
   :alt: GSoC FTW!

   GSoC FTW!

For those who are geeky and want to see the PRs submitted…
----------------------------------------------------------

`Here is the
link <https://medium.com/@yashrsharma44/pull-requests-merged-in-for-gsoc19-ndcube-95a9fd15c8b6>`__
where all my PRs for completing the project are present. > # Google
Summer of Code (GSoC) is an online, international > #program designed to
encourage university student participation in open source software
development.

Details of my Organisation and Project
======================================

    Before I start writing my report, I would like to thank my mentors
    `Daniel Ryan <https://github.com/DanRyanIrish>`__ and `Stuart
    Mumford <https://github.com/cadair>`__. They have been quite helpful
    in guiding me through the project, and have been quite responsive.
    Special thanks to `Nabil Freij <https://github.com/nabobalis>`__,
    for guiding through the project here in SunPy/NDCube.

`NDCube` is the fundamental class of the ndcube package and is designed to handle
data contained in a single N-D array described by a single set of WCS
transformations.
`NDCube` is subclassed from
`astropy.nddata.NDData` and so inherits the same attributes for data, wcs, uncertainty, mask, meta,
and unit. The WCS object contained in the .wcs attribute is subclassed
from `astropy.wcs.WCS` and contains a few additional attributes to enable to keep track of its
relationship to the data.

.. figure:: https://cdn-images-1.medium.com/max/2000/0*uqnVlB46CcEgB4CV
   :alt: SunPy: The Sub-Organisation that I worked in.

   SunPy: The Sub-Organisation that I worked in.

My GSoC project was under
`OpenAstronomy <https://openastronomy.org/>`__, and NDCube is a SunPy
affiliated subpackage for handling ND Data arrays and perform
data-analysis on them.

NDCube is a SunPy affiliated package for easily dealing with ND-Data
cubes along with convenience method that allows the data cubes to be
sliced, attach meta-data to it, and easy to use plotting methods, to
visualize an ND-Data. It uses SunPy’s visualization to plot more than
`>2D` cubes and provides sliders to shift the different dimensions, so
even if users are using only 2D dimensions at a time, we can still
leverage the other dimensions.

My project with NDCube was to port the internal API to match all the
proposals laid out in
`APE14 <https://github.com/astropy/astropy-APEs/blob/master/APE14.rst>`__
and make sure that NDCube works in the same manner as it was working.
The project was particularly interesting because I had a first-hand
chance of interacting with API designing and how the different patterns
were used to implement that. NDCube uses FITS-WCS to interact with, but
APE14 leveraged the NDCube to use any WCS object implementing all the
base methods laid out in the proposal. This was really exciting and I
had a chance to use gWCS along with FITS-WCS in NDCube.

Blogging and details of my work
===============================

My weekly notes about my progress have been documented in my
`blog <https://medium.com/@yashrsharma44>`__. Feel free to check out and
suggest changes if needed.

Breakdown of my project
=======================

As described in my
`proposal <https://github.com/yashrsharma44/GSoC-2019-Proposal>`__, I
had broken down my project into three parts —

-  Porting NDCubeBase to use APE14

-  Porting NDCubeSequence to APE14

-  Support plotting in NDCube

All the associated PRs have been blogged in the `PR
post <https://medium.com/@yashrsharma44/pull-requests-merged-in-for-gsoc19-ndcube-95a9fd15c8b6>`__
that I made earlier. Feel free to check them and gauge the progress that
I made.

Some Visuals associated with my project
=======================================

.. figure:: https://cdn-images-1.medium.com/max/2000/1*jPvoayLdAkm8D8sWseUM1g.png
   :alt: Example of a WCS plotting with NDCube

   Example of a WCS plotting with NDCube

.. figure:: https://cdn-images-1.medium.com/max/2000/1*BaYgBlsV9B6f5o-vEAa5sg.png
   :alt: Example of WCS Line Plotting with NDCube

   Example of WCS Line Plotting with NDCube

My Experience with working with NDCube/SunPy
============================================

Right from the start, I was really interested in working in SunPy,
because of its amazing community and responsive mentors which I had
planned to learn from them. The mentors were really helpful, right from
designing the proposal to implementing them, always filling out on
potential hurdles and rescuing me out every now and then.

I decided to list out the tasks which could not be completed, as the
rest of the checkpoints were achieved successfully.

**Here are some tasks which I had planned but could not be done**

-  Writing gWCS test-suite for NDCube — This was an optional part but
   having spent time with the code-base a lot, I realized that this
   could be done in a short time. However, this being an optional part,
   got pushed right at the end, and eventually had to be dropped off
   from the weekly tasks. I have planned to complete it after GSoC, so
   it remains on top of my priority list.

-  Completing
   `plotting <https://github.com/sunpy/ndcube/projects/2#card-21344119>`__
   of NDCubeSequence — I had completed almost all of the tasks as I had
   planned in my
   `proposal <https://github.com/sunpy/ndcube/projects/2>`__ but
   remaining one — Completing the plotting for NDCube Sequence objects.
   I had made the PR, but on close digging with the codebase, I realized
   that the master codebase was buggy, and a bug fix was needed to be
   made before resuming my porting. I made the PR, and after
   consultation with my mentor, we decided to drop the priority for the
   bug fix and just concentrate on my porting. I `made a
   PR <https://github.com/sunpy/ndcube/pull/196>`__ but it remains open
   till the bug is fixed in the master branch.

My Experience with Google Summer of Code
========================================

GSoC had been an integral part of my sophomore life, as it was something
that I wanted to try out, with the associated perks and the hyped-up(
but true!) steep learning curve. I had started my contributions right
from January when people are unsure with the organizations and the type
of projects that they want to commit to for the rest of the summers. I
chose SunPy because of its fantastic community of developers from whom I
learned a lot.

There was
`blogpost <https://numfocus.org/blog/meet-our-2019-gsoc-students-part-3>`__
by NumFocus which highlighted my learnings during GSoC, so I would be
sharing some unique points (not share the old ones :P) that highlighted
my learnings — 

    Make sure you have a good understanding of the subparts of the project

I have had some moments where I just went about my tasks without having
a solid understanding of them. I had to revert back to understand it
again, so I recognized my shortcomings after my first evaluations and
made sure that I had a solid understanding of the problem, rather than
diving into it, without understanding the what and why of the problem. 

    Make sure you have some backup tasks to fall back upon

I have had moments when my work progress
`dried <https://medium.com/@yashrsharma44/week-08-gearing-up-for-the-plotting-ii-e7e17493433b>`__
`out <https://medium.com/@yashrsharma44/week-09-cadair-is-back-ee083d59c71e>`__,
but talking with my mentor(s) and having some backup tasks did help me
with my case of sitting idle. This turned out to be crucial in the last
few weeks, as I had little to no time of starting out on a new feature.
Thanks to my backup tasks, I had to carry forward them rather than
starting them from scratch. 

    Make sure you have fun

Well, this depends on org-to-org, so I would not consider it as a
universal fact. I had fun in interacting with the weekly community
meetings arranged in every Wednesday. Other developers were quite
helpful and curious about the progress of my project, and I was really
happy to share the progress of my work.

GSoC is surely an experience of a lifetime, and I would suggest everyone
who is enthusiastic with Open-Source and want to develop industry graded
software, then GSoC is the right place. 

    Ciaos Adios!
