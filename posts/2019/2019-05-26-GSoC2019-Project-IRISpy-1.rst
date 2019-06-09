GSoC 2019: Project IRISpy 0.2
=============================

.. post:: May 26, 2019
   :author: Kris Stern
   :tags: GSoC, IRISpy, NDCube
   :category: GSoC

Progress has been better than expected… Within the past few weeks, while continuing work on the main PR (which can be accessed via this `link <https://github.com/sunpy/irispy/pull/108>`_) on enabling a time-dependent effective areas determination in the "`iris_tools <https://github.com/sunpy/irispy/blob/1475cfc62c6c83ccf0798cb4b4fa94a6b3b01549/irispy/iris_tools.py>`_" file, which contains some IRIS instrument tools, most of the previous difficulties of translating from the IDL programming language to the Python language have been identified and ironed out. In hindsight, for me the hardest part was to comprehend a computing language for which I have no direct access to (as I do not have in possession a valid IDL licence), but at the same time be able to gain enough insight through freely available online documentation to check the rough work put into place earlier in `another PR <https://github.com/sunpy/irispy/pull/102>`_. Through careful and systematic checking, I have been able to move ahead and implement the new function fit_iris_xput() as well as the get_iris_response() function in a pythonic way with some heavy dose of guidance from my mentors Dr. Dan Ryan and Dr. Laura Hayes well ahead of schedule.

For example, instead of converting from seconds to years by brute force with the conversion factor:

.. code-block:: python
   :linenos:

   yr2sec = np.float64(365.25*24.*3600.)
   t_diff = t_obs - t_cal_coeffs
   t_diff = t_diff/yr2sec

we opted to use Astropy’s powerful Units and Quantities “machinery” for the conversion instead, in the following manner:

.. code-block:: python
   :linenos:

   t_diff = t_obs - t_cal_coeffs
   t_diff = t_diff.flatten()
   t_diff = [x.to(u.year) for x in t_diff]

It has been necessary to flatten the numpy array into an 1D object to allow the list comprehension to be applied.

So the plan ahead would be to incorporate the newly implemented time-dependent fitted response into the wider IRISpy code base.