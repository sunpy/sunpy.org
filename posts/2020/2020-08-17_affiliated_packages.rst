The What, Why and How of SunPy Affiliated Packages
==================

.. post:: August 18 2020
   :author: Laura Hayes
   :tags: sunpy
   :category: Update


What are SunPy affiliated packages?
-----------------------------------
The SunPy project supports affiliated packages that are packages that build upon or extend the functionality of sunpy. Affiliated packages are well-maintained, open source software packages that are useful to solar physicists and integrate well with the SunPy ecosystem.

these packages provide functionality that is considered outside the scope of the core library but builds upon it. They are reviewed by and registered to the SunPy Project. Together with the core library they form the SunPy software ecosystem.

Not all software falls within the scope of the core SunPy library but it is in the best interest of the general community to have access to a healthy, diverse, and compatible software ecosystem. The primary purpose of the affiliated package system is to support software developers that provide additional tools and functionality that extends and builds upon the core library.


A sponsored afilliated package is an affiliated package that is maintained and governed by the SunPy project, examples of these include sunpy core and ndcube. Non-sponsored affiliated packages remain under the control of the original developers, examples of this would be instrument-specific affiliated packages such as AIApy.

Why would a package want to become an affiliated package?
---------------------------------------------------------

The main

The type of packages that would become an affiliated package is a code-base or package that is useful to the solar physics community but may be outside the scope of sunpy core. This may be for example some software for a specific mission or instrument, such as calibration routies, and instrument-specific software. non-sponsored affiliated packages remain under the control of the original developers

SunPy is starting to develop a set of general affiliated packages, i.e ndcube, sunkit-image and drms as well as instrument specific ones like IRISPy.

The SunPy project will ensure that affiliated packages are maintained and publicized in order to encourage community development.


The idea would be lalalla


Call to instrument/mission teams!
---------------------------------
We would invite interested mission or instrument teams that are interesed in developing a python package for there instrument to become a affiliated package. This will allow the code to live and develop within the sunpy ecosystem. 

We would like to start the effort to integrate instrument teams with SunPy :tada

The advantage of this is to aid discoverability and tries to advertise them at national and international conferences and workshops.


Encourange external packages to apply for affiliate status

Incubator!


Package template
----------------

The SunPy project has developed a `package template <https://github.com/sunpy/package-template>`_ which is designed to help developers create new Python packages within the SunPy ecosystem. The idea is that this template provides a simplified way to standarized packaging, testing, and documentation using the same framework as the sunpy core package. The SunPy package template makes it easier for package developers to meet the standards required by SunPy to become an affiliated package!


How does a package become an affiliated package?
---------------------------------------------------

We now have a review process for a package to become an affiliated package, and a streamline process for this. This new process is aimed at ... The review process for becoming a SunPy affiliated package is supposed to be approachable, lightweight and open.  A review process ensures that affiliated packages provide useful functionality to the community at a standard of quality similar to the core SunPy package

The packages themselves are not maintained by the sunpy development team, but require a set of standards to be an affiliated package. 

There is an issue template. 

First the editor will check that the package meets the baseline requirements of an affiliated package, such as checking to see that it is apporpiate and is compatible with the Sunpy `Code of Conduct <https://docs.sunpy.org/en/latest/code_of_conduct.html>`_,  has an appropriate licence, provides a Python interface, is it on pypi and it is useful to the solar physics community. Following this, a reviewer independent to the package is assigned and a review is undertaken based on the criteria listed below. It's an open review process!


The review critera listed:

* Functionality           : General Package / Specialized Package / Not Relevant
* Integration             : Well integrated / Partially Integrated / Minimal Integration
* Documentation           : Extensive / Some / Little
* Testing                 : Excellent / Good / Needs Work
* Duplication             : None / Some / Major
* Community               : Excellent / Good / Needs Work
* Development Status      : Stable / Subject to Change / Low Activity / Needs Work

The criteria is reviewed based on a 'traffic light' system, being 'graded', 'green', 'orange' and 'red' based on the criteria listed aboce. To be accepted the package must be *green* in Functionality, and one other category. It must also not list any red scores.

If the package in its current state does not pass the critera - after review a package is listed as provisional, as long as it is assessed to not have a red score in the “Functionality”, “Duplication” or “Community” criteria and is working towards meeting the rest of the review criteria.

Don't worry - we will have an Affiliated Package Liason that will help you through each step of this process :)

Reach out!
----------
If you are a developer of a package that you think fits nicely into the SunPy ecosystem and will of benefit to the solar physics community and want to chat to us about it please reach out! This can be of course regardless of how far along the package is - from concept to maturity! Join us our live chat `element channel <https://openastronomy.riot.im/#/room/#sunpy:openastronomy.org>`_ or join in on the SunPy weekly community meetings which occur on Wednesdays at 16:00 UTC and are hosted on `jitsi <https://sunpy.org/jitsi>`_.





