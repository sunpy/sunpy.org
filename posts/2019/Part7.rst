Part 7: The End Arrives
-----------------------

.. post:: August 19, 2019
   :author: Vatsalya Chaubey
   :tags: GSoC, Sunpy, Sunkit-image
   :category: GSoC


It has now been twelve weeks since I began this journey and finally, the
curtains on this arduous and breathtaking adventure have been begun to
fall. This week it will be last week as an official Google Summer of
Code and this will be my final post as a student. I can feel the
nostalgia gripping me.

Well, this has been one of the most productive summers which helped me
gain a lot of new skills and make new connections and I would really
like to thank Google and Sunpy for giving me this opportunity. I would
also like to thank my mentors Nabil and Jack for being the constant
support which I needed throughout the length of the program.

This post mainly serves as a summary of all the progress which has been
made in the Sunkit-Image project since the commencement of the summer of
code. Speaking statistically, I had opened five pull requests adding
four independent algorithms and image processing techniques along with a
pull request solely dedicated to documentation. This included their
documentation, testing, and examples how to use them which overall
amounted to be about 3,000 lines of code written by me.

Coming to the algorithms which got introduced in Sunkit:

-  **Normalizing Radial Gradient Filter**

This particular algorithm is designed to enhance offlimb features in a
solar image. Though this was already present in Sunkit, it had some
flaws and without any proper documentation and examples to it. I
rectified the code wherever it was needed along with adding proper
documentation and example to it.

-  **Fourier Normalizing Radial Gradient Filter**

This is an advanced version of the Normalizing Radial Gradient Filter
aimed at the same task. This was implemented from scratch as a precursor
to my application for GSOC to sunpy. I completed it when the coding
period began and both the NRGF and the FNRGF were pushed in a single PR
`here <https://github.com/sunpy/sunkit-image/pull/17>`__. This has
already been merged.

-  **Multiscale Gaussian Normalization**

Next, I moved on to the Multiscale Gaussian Normalization which is an
algorithm designed to enhance features on the solar surface. It was
fully implemented along with documentation and examples which can be
found `here <https://github.com/sunpy/sunkit-image/pull/30>`__. This too
has been merged.

-  **Soft Morphological Transform**

The implementation of this particular algorithm did not take place
because we found an Astroscrappy module which actually does the exact
same thing using a different approach. So instead of doing a repeated
work we decided to move on to something more useful. But, nevertheless
an example describing how to use Astroscrappy was written.

-  **Oriented Coronal Loop Tracing (OCCULT)**

This is the part of the programme which took the longest time to code
and debug. It is an algorithm to automatically trace out coronal loops
in an image. This
`PR <https://github.com/sunpy/sunkit-image/pull/31>`__\ is complete with
tests and documentation and is under review presently.

-  **Fourier Local Correlation Tracking**

A python wrapper was created for the FLCT C code such that it becomes
usable in Python. This particular algorithm finds the 2D velocity flow
field between an image. This too took almost a month to be completed and
is under review now. You can have a look at the code
`here <https://github.com/sunpy/sunkit-image/pull/36>`__.

This mostly sums up what has been done during the coding period and I
feel the four major goals which had to be achieved for the successful
completion of the programme have been achieved. I do hope that I will
successfully clear the final evaluation.

Hope you all enjoyed reading the glimpses of my journey through GSOC. It
was a very nice and fascinating experience. I will still try to
contribute to sunkit after the program ends. I do hope I get a second
chance to be a part of this adventure again.
