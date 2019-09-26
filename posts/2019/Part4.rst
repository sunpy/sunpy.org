Part 4: Weeks after the first evaluation
========================================

.. post:: July 7, 2019
   :author: Vatsalya Chaubey
   :tags: GSoC, Sunpy, Sunkit-image
   :category: GSoC

This is part 4 of the ongoing series of my blog posts describing my
journey as a Google Summer Of Code student working with Sunpy to develop
Sunkit-image, an image processing toolbox for solar images.

|image0|

In this installment, I describe the work in the two weeks following the
first evaluation on June 24. It has finally been a month since I started
this adventurous journey of Google Summer of Code. This past month
helped me learn a lot of new stuff, methodologies and techniques. It
really has been a fascinating experience for me. And when the results of
the first evaluation came out I was filled with joy and happiness that I
made it through the first hurdle.

--------------

Now, coming back to the progress I made during the last two weeks. I
mostly spent my weeks working on two problems :

-  **Soft Morphological Transform**

Soft Morphological Transform is a routine which aims to remove cosmic
ray hits from solar images. As per our earlier plan, we would implement
this algorithm from scratch if and only if the
“astroscrappy.detect_cosmics” did not work for solar images. So our
first course of action was to validate the performance of the
astroscrappy module for solar data and to our delight, it worked
perfectly for solar data.

|image1|

|image2| Images depicting the working of astroscrappy module. The left
one is the input image whereas the right one is the output after using
that module.

Once the module was found to be working I wrote an example about
showcasing how to use it which can be found
`here <https://github.com/sunpy/sunkit-image/pull/35>`__.

-  **Wrapping the FLCT C code into Python**

Fourier Linear Correlation Tracking is an algorithm which finds the 2D
flow field between two images taken close to each other. The FLCT code
is already written in C and is publicly available. But to make this
accessible in python I am wrapping it using Cython. As of now, I have
wrapped the subroutines required for the FLCT code and the wrapping of
the main code is underway. Hope to finish this in a couple of days
before I go on a short vacation.

--------------

I hope you enjoyed reading this. Stay tuned for further updates and
happenings in the coming weeks.

.. |image0| image:: https://cdn-images-1.medium.com/max/1000/0*jYVo2Hd2fjX5ktgS.png
.. |image1| image:: https://cdn-images-1.medium.com/max/1500/1*NLloXogpIcKRFGLeKOa5ow.png
.. |image2| image:: https://cdn-images-1.medium.com/max/1500/1*lz4cZ19aQOz8q9eC7tEXAg.png
