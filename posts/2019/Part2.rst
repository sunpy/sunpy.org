Part 2: The Dive
================

.. post:: June 9, 2019
   :author: Vatsalya Chaubey
   :tags: GSoC, Sunpy, Sunkit-image
   :category: GSoC

The **Coding Period** of the Google Summer of Code officially began on
27th May 2019 — for me, it was the day when the “**Dive**” into the
realm of code began.

|image0|

This post is the second post in the series of posts I am writing every
two weeks to describe my journey as a student in Google Summer of Code
Programme working for **Sunpy** for their solar image processing
toolkit, **Sunkit-Image**.

|image1|

--------------

Why do I call it a **dive**, you might wonder? Imagine a man on a boat
in the middle of a lake, rowing it towards the far shore. He has just
started his journey and was hoping he could make it to the other side
without getting himself wet, more than that was necessary. This is was
my condition at the starting of the coding period.

You will still ask where is the **dive** then. Rest assured I am coming
to it. The man is not alone on the boat as you might think. There are
two more people on it. Both of them are excellent swimmers and want that
man to learn to swim.

   One cannot learn to swim without ever entering into the water.

This is the **dive.**\ They encourage the man to go into the water at
the same time supporting him, saving him from drowning. Now I hope you
understand where I am taking this.

The man on the boat is I, the two other people on the boat are my GSOC
mentors — Jack and Nabil, the water is the complexities of the
algorithms and the lake itself is the Google Summer of Code.

--------------

The first two weeks have been just like the way as I have described
above — filled with “first-time” moments which were a little
intimidating once, but with the help of everyone — my mentors, the Sunpy
community everything is going on smoothly.

Now coming to what has been done in these two weeks —

-  **Implemented the Multi-scale Gaussian Normalization**

Multi-scale Gaussian Normalization (MGN) is an algorithm to enhance the
images of solar surface and limb. This is a complex algorithm. During
these two weeks, I wrote the algorithm along with the tests and examples
for it.

An input image to the MGN algorithm

The output of MGN for the above image

-  **Completed the Fourier Normalizing Radial Gradient Filter**

I have written the code for this algorithm before GSOC officially began
but there was still a lot to do. During the past weeks, I wrote more
tests and examples, fixed the documentation. Along with this I also
worked on the Normalizing Radial Gradient Filter adding tests, examples
and documentation fixes.

An input image

The output of the NRGF filter

The output of the FNRGF filter

-  **Implemented the OCCULT-2 algorithm**

Oriented Coronal CUrved Loop Tracing (OCCULT) is an algorithm to
automatically trace out the loops on the solar surface and the corona. I
have just written the code as of now without any testing. I cannot
provide any output image because the code has not been validated and
checked. This is one of the trickiest algorithms and it took me almost a
week to understand it fully but I am confident that it will take some
more time before it is completed.

The work to be done in the coming weeks —

-  Make both the pull requests on MGN and FNRGF ready to be merged.
-  Work on the OCCULT-2 code, perform extensive testing on the code and
   make sure that everything is working fine.

--------------

I hope you enjoyed reading it. Stay tuned for more exciting stories.

-  `Programming <https://medium.com/tag/programming?source=post>`__
-  `Gsoc <https://medium.com/tag/gsoc?source=post>`__
-  `Sunpy <https://medium.com/tag/sunpy?source=post>`__
-  `Image
   Processing <https://medium.com/tag/image-processing?source=post>`__

`Vatsalya Chaubey <https://medium.com/@vatsalyachaubey19980>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |image0| image:: https://cdn-images-1.medium.com/max/1000/1*4FkOWgo5ou2OfJYrxrdZKw.png
.. |image1| image:: https://cdn-images-1.medium.com/max/1000/0*US__hwDUSCu6nNVG.png

