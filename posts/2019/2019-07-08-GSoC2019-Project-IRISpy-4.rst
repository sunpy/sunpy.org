GSoC 2019: Project IRISpy 2.1
=============================

.. post:: July 8, 2019
   :author: Kris Stern
   :tags: GSoC, IRISpy
   :category: GSoC

Passed Phase 1 of GSoC. And I have just encountered my first roadblock in this project over the past few days, so now I am working hard on various approach to try and understand some IDL code snippets that does not translate well into Python without some more knowledge of the IDL INTERPOL function. (Source: `harrisgeospatial <https://www.harrisgeospatial.com/docs/INTERPOL.html>`_) In IDL, this function takes in a maximum of four arguments: an input vector, the number of points in the result, the abscissa values for the input vector, and abscissa values for the result. In this way, the iris fit can be interpolated onto a new lambda grid readily. However, an exact equivalent does not exist in Python. The closest one we have opted to adopt is SciPy’s interpolate.interp1d function (Source: `scipy <https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html>`_). This method takes the x-coordinates and y-coordinates of the input data, and interpolate some pattern from this, which means that to project to a grid an extra step is necessary. I have now modified the relevant code snippets of in my PR so that I have a functional line. But to project it to some very specific grid distinct from the input one will take extra checking, since I am iffy about my approach. Currently seeking input from my mentors to sort out the issue. Hopefully this roadblock will be cleared soon.