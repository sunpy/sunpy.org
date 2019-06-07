[Week 01]— Getting Stuff Done!
==============================
.. post:: June 03, 2019
   :author: Yash Sharma
   :tags: GSoC, NDCube
   :category: GSoC

|image0| 

It’s time for Action ; Code-Sleep-Coffee Repeat!

This blog post marks my account for the first week of coding for
GSoC’19. While it may not be as long as my previous posts, I would hope
to make posts every week, so it would be as recent and relevant.

Making Progress for the Week
============================

While I had already made progress with the tasks, now it was time to get
the unmerged PRs merged. I started to refine my PRs, and after going
through lot of iterations, I decided to drop this idea and do something
else. A fresh mind would be more receptive to find bugs.

Frankly speaking, I did not make any progress, even though in my mind I
thought I made 😛. I mostly had a lot of discussion with ``@Cadair``
about the issue of failing tests of ``NDCube``, and I spent a lot of
time understanding the plotting of ``NDCube``. The plotting seems to be
very complex, and it contained small portions of code which made no
sense to me at all. All the time, I spent time understanding the code,
but made no progress.

|image1| 

Sometimes debugging is helpful in understanding the flow of
code!

I had been spending time in understanding, more than making real
progress. This is wrong as writing some code always help in getting
*unstuck*. A lot of times people suggest to understand the code before
making changes, but if you spend a lot of time understanding the flow of
code without any progress, it is better to crack open your favourite
editor and start using breakpoint to identify the flow of code and make
notes (yes notes!) of the changes unexpected.

Another thing I did is use test-cases to identify how the input was
getting modified. Sometimes, an example is really helpful to map the
abstraction of a method into something practical. I used the tests to
inspect the portions of code which were creating nuisance, as I
submitted another PR about fixing most the issues. There are few test
cases which are failing, so it would take more time before this
`PR <https://github.com/sunpy/ndcube/pull/176>`__ is merged.

Link to previous post
=====================

-  Contributing my way to SunPy1.0 —
   `Link <https://medium.com/@yashrsharma44/contributing-my-way-for-sunpy1-0-76bbc5673b8f>`__

.. |image0| image:: https://cdn-images-1.medium.com/max/1144/0*z7jar2Q3sthcusYq.jpg
.. |image1| image:: https://cdn-images-1.medium.com/max/1144/0*PjHq4AuTbMjXz7Gq.jpg

