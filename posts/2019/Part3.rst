Part 3: The Debugging
=====================

.. post:: June 22, 2019
   :author: Vatsalya Chaubey
   :tags: GSoC, Sunpy, Sunkit-image
   :category: GSoC

This is part 3 of the ongoing series of my blog posts describing my
journey as a Google Summer Of Code student working with Sunpy to develop
Sunkit-image, an image processing toolbox for solar images.

|image0|

This particular part describes the work that has been done from 10th
June to date. This part of the project was especially tricky involving
lots of debugging. But, first I would like to begin on a positive note.
My both the initial pull requests — one on the Fourier Normalizing
Radial Gradient Filter and the other on Multiscale Gaussian
Normalization were finally merged. It was such a delightful moment when
your code gets accepted, I am sure all the coders reading this
understand how I feel!! You can have a look at my pull requests here —

-  `Fourier Normalizing Radial Gradient
   Filter <https://github.com/sunpy/sunkit-image/pull/17>`__
-  `Multi-scale Gaussian
   Normalization <https://github.com/sunpy/sunkit-image/pull/30>`__

--------------

Now coming to the tricky part of the affairs. I spent these two weeks
almost entirely on implementing the Oriented Coronal CUrved Loop Tracing
(OCCULT-2) algorithm, which is aimed at automatic tracing of coronal
loops. The initial implementation of the algorithm was relatively easy
but then the complications started to manifest themselves. The major
issue was the paper describing the algorithm and the code written by the
author in IDL had some differences. So figuring out why those changes
were made was a very tiring job.

Those modifications were finally incorporated in the python code but
still, my implementation is not performing the way it should. So it is
clear that there are some bugs still present. So began the process of
bug hunting. Being such a complex algorithm find those hidden bugs was a
challenge. I had many of “Eureka” moments which later turned out to be
false alarms. There were a few moments when I actually got frustrated
and thought of moving to something else. But I stuck to it, hoping I
will find it soon.

The hunt for the culprit is still on though. I was able to fix many
other minor bugs in this entire endeavour but the mighty one is still
elusive. I am still working on it and hope to locate it soon enough.

The left image is an image of the solar surface showing some very
prominent loops. The right image shows the output of my code. My code is
being able to trace the loops but the loops are not being traced
continuously rather there are traced in parts having breaks in between
them. This is the major bug in the code which I am unable to find out
till now.

I am still on my schedule and have some more days to tackle this issue
and I am confident that I can make it work.

--------------

Hope you enjoyed this. Join me again in the coming weeks to see what
comes out of this algorithm and all the other cool things I would be
working on.

-  `Programming <https://medium.com/tag/programming?source=post>`__
-  `Sunpy <https://medium.com/tag/sunpy?source=post>`__
-  `Gsoc <https://medium.com/tag/gsoc?source=post>`__
-  `Sun <https://medium.com/tag/sun?source=post>`__
-  `Sunkit Image <https://medium.com/tag/sunkit-image?source=post>`__

`Vatsalya Chaubey <https://medium.com/@vatsalyachaubey19980>`__
---------------------------------------------------------------

.. |image0| image:: https://cdn-images-1.medium.com/max/1000/0*MeSBNvJPnHChX6Yn.png
