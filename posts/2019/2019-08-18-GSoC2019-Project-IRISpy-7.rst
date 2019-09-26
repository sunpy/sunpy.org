GSoC 2019: Project IRISpy 3.2
=============================

.. post:: August 18, 2019
   :author: Kris Stern
   :tags: GSoC, IRISpy
   :category: GSoC

It is my pleasure to report that with my mentors’ assistance as well as my many hours of contributing to the sunpy/irispy GitHub repo, I have been able to reach all four goals original set out by the primary mentor Danny Ryan, which are as follows:

1. The time-dependent instrument function response code must be rewritten to be more efficient and Python-friendly.
2. Formal benchmarking between the results it produces and those found using the original IDL code must be performed.
3. Tests for the Python version must be written.
4. This software must be incorporated into methods and functions in IRISpy that depend on the instrument response function.

Accordingly, the three outcomes have been accomplished as below:

1. A function for deriving the time-dependent IRIS response function.
2. Benchmarking and unit tests so this new software can be reliably maintained.
3. Updated intensity conversion methods between instrument and physical units that correct for the time observations were taken.

For a product of this effort, please go `here <https://github.com/sunpy/irispy/pull/119>`_ , which is to merge the four PR’s already merged into the time_dependent_response branch into the master branch in order to incorporate our work into IRISpy officially.

I would particularly like to take the time to thank every one in the SunPy community for their support of me over the past few months, in particular my project mentors Danny Ryan and Laura Hayes. They have been very helpful in answering my questions and in helping me solve some very thorny IDL questions. The time I spent on GSoC this year is the moments I will not forget!