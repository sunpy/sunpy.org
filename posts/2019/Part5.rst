Part 5: The Second Evaluation Awaits
====================================

.. post:: July 21, 2019
   :author: Vatsalya Chaubey
   :tags: GSoC, Sunpy, Sunkit-image
   :category: GSoC


The fifth part of the ongoing series of my blog posts on my experience
in the Google Summer of Code. I am working with Sunpy on their solar
image processing toolkit, Sunkit-image. As of now two months have
already and it has been an enriching experience. The second evaluation
is also just around the corner and I am very hopeful that I will be able
to clear it.

|image0|

In this post, I describe the last two weeks of my work which was
essentially only one week of work as I was on a vacation for a week. I
had already discussed with my mentors regarding taking a vacation and
they were fine with it if I could compensate for the lost time.

Now coming to the details of the work in the past week. I had been
working on writing a python wrapper for FLCT C code. Fourier Linear
Correlation Tracking is an algorithm which finds the 2D flow field
between two images taken within a close interval to each other. I had
earlier written the wrapper for the subroutines of the FLCT main code.
During this week, I fixed the original wrapper for the subroutines and
also implemented the main FLCT file, which makes FLCT available in
python.

There are few errors hidden in my code as of yet which are being
diligently hunted. Hopefully, the code would soon be bug-free. I am also
working on the testing and documentation of the sub-package
simultaneously. The entire wrapping has been done using Cython where the
numpy arrays have been converted to C-compatible types like pointers or
pointer to pointers.

Overall this particular section of work was very interesting. It was the
first time I had used Cython and power which it provides to use of C
codes in plain Python is amazing. The knowledge of this opens up various
avenues of optimization in other python functions.

Hope you enjoyed reading this. Stay tuned for further updates!!!

.. |image0| image:: https://cdn-images-1.medium.com/max/2000/0*_F_2zXKc0Rcc90Gn
