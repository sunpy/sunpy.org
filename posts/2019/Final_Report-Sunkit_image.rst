Sunkit-Image: Final GSOC Report
===============================

.. post:: August 24, 2019
   :author: Vatsalya Chaubey
   :tags: GSoC, Sunpy, Sunkit-image
   :category: GSoC


This project developed several image processing algorithms and
manipulation routines for sunkit-image, an affiliated Python package of
the Sunpy Project. The rigorous analysis of solar images is of paramount
importance to the Heliophysics community as this can reveal more
information on solar features and events, which in turn can affect the
Earth. This project brought selected solar image processing algorithms
under the umbrella of a new library.

GSOC 2019: Project Goals
------------------------

| There were four major goals as listed on the OpenAstronomy
  `website <https://openastronomy.org/gsoc/gsoc2019/#/projects?project=develop_sunkit-image>`__.
| These included: \* Implement the Normalizing Radial Gradient Filter \*
  Port the Multi-scale Gaussian Normalization \* Implement the OCCULT-2
  algorithm for coronal loop tracing \* Implement Soft Morphological
  filtering of the solar images

Project Goals Completed
-----------------------

-  **Implement the Normalizing Radial Gradient Filter**
   Normalizing Radial Gradient Filter is an algorithm designed to
   enhance features off the solar limb in a solar image. It normalizes
   the radial gradient i.e., the sharp decrease in intensity values in
   images as the pixels increase in radial distance from the Sun’s
   centre which helps in visualizing the coronal structures.
   This has been completed and merged along with its sister algorithm
   the Fourier Normalizing Radial Gradient Filter. The code for this can
   be found on this
   `PR <https://github.com/sunpy/sunkit-image/pull/17>`__.
-  **Port the Multi-scale Gaussian Normalization**
   Any solar image contains information distributed over a very wide
   range of spatial scales which can be mostly hidden due to the
   variation of intensity values in an image. Processing such an image
   to unveil that hidden information is therefore very important.
   Multi-scale Gaussian Normalisation effectively normalizes the pixel
   values locally at different scales by convolving with different
   widths of Gaussian kernels and can reduce noise locally revealing any
   hidden features.
   The algorithm was successfully implemented and the
   `code <https://github.com/sunpy/sunkit-image/pull/30>`__ has already
   been merged.
-  **Implement the OCCULT-2 algorithm**
   Oriented Coronal CUrved Loop Tracing (OCCULT) is an algorithm
   designed to automatically trace out coronal loops in an image. It
   traces out loops starting at the maximum flux position and then
   moving in a bidirectional fashion from that point.
   The code, documentation and examples are complete and can be found
   `here <https://github.com/sunpy/sunkit-image/pull/31>`__, it is
   waiting for further reviews and will be merged shortly (< 2 weeks).
-  **Implement the Soft Morphological filtering**
   The soft morphological filter approach to removing cosmic ray hits in
   a solar image uses image morphology operators and genetic algorithms.
   However, a similar package called
   `Astroscrappy <https://github.com/astropy/astroscrappy>`__ that also
   removes cosmic ray hits was found. We found that the algorithm used
   by Astroscrappy had more citations as compared to the Soft
   Morphological filtering and in our tests, it produced good results on
   solar data. So it was decided that the Soft Morphological filtering
   will not be implemented and rather a detailed example on how to use
   Astroscrappy on solar data was written
   `here <https://github.com/sunpy/sunkit-image/pull/35>`__.

Further Project Work
--------------------

These tasks were not part of the main GSoC
project goals but were worked upon during the GSoC project.

-  **Fourier Linear Correlation Tracking**
   An existing C library was wrapped using Cython to enable Python calls
   to a Fourier Linear Correlation Tracking (FLCT) C library along with
   the tests and documentation for the wrapper. This algorithm aims at
   finding out the 2D flow field between two images.
   This `work <https://github.com/sunpy/sunkit-image/pull/36>`__ is
   complete and under review.
   However, as the C code is licenced under GPL v2 and sunkit-image is
   under BSD, we are waiting on permissions from the original authors
   before this can be merged or if it needs to be spun into a separate
   library.
-  **Fourier Normalizing Radial Gradient Filter**
   This was implemented as a run-up to GSoC and the tests and example
   were written during the coding period.
   `This <https://github.com/sunpy/sunkit-image/pull/17>`__ was merged
   along with the Normalizing Radial Gradient Filter.
-  **Noise Level Estimation**
   There was a preexisting noise estimation class in sunkit-image and it
   was decided that this was to be converted into a series of functions.
   Most of this task had already taken care of in PR
   `22 <https://github.com/sunpy/sunkit-image/pull/22>`__, however, the
   original author was unable to finish this work and so this was
   completed in a new `pull
   request <https://github.com/sunpy/sunkit-image/pull/38>`__ and was
   merged.
