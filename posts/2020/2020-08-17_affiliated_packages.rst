Affiliated Packages
==================

.. post:: August 17 2020
   :author: Laura Hayes
   :tags: sunpy
   :category: Update


What are affiliated packages?
-----------------------------
The SunPy project supports affiliated packages that are packages that build upon or extend the functionality of sunpy. Affiliated packages are well-maintained, open source software packages that are useful to solar physicists and integrate well with the SunPy ecosystem.

these packages provide functionality that is considered outside the scope of the core library but builds upon it. They are reviewed by and registered to the SunPy Project. Together with the core library they form the SunPy software ecosystem.

Not all software falls within the scope of the core SunPy library but it is in the best interest of the general community to have access to a healthy, diverse, and compatible software ecosystem. The primary purpose of the affiliated package system is to support software developers that provide additional tools and functionality that extends and builds upon the core library.

Why would a package become an affiliated package?
-------------------------------------------------
The type of packages that would become an affiliated package is a code-base or package that is useful to the solar physics community but may be outside the scope of sunpy core. This may be for example some software for a specific mission or instrument, such as calibration routies, and instrument-specific software. non-sponsored affiliated packages remain under the control of the original developers

SunPy is starting to develop a set of general affiliated packages, i.e ndcube, sunkit-image and drms as well as instrument specific ones like IRISPy.

The SunPy project will ensure that affiliated packages are maintained and publicized in order to encourage community development.

Call to instrument/mission teams!
----------------
We would invite interested mission or instrument teams that are interesed in developing a python package for there instrument to become a affiliated package. This will allow the code to live and develop within the sunpy ecosystem. 

We would like to start the effort to integrate instrument teams with SunPy :tada

The advantage of this is to aid discoverability and tries to advertise them at national and international conferences and workshops.


Encourange external packages to apply for affiliate status

Incubator!

Futhermore if you have some code that you would like to 'package-together' make sure to check out the sunpy package template. 

(To make it easier for affiliated package developers, the SunPy Project must develop and maintain a publicly available package template.)
provide  a package template has been developed that simplifies
and standardizes packaging, testing, and documentation  https://github.com/sunpy/package-template

How do does a package become an affiliated package?
---------------------------------------------------

We now have a review process for a package to become an affiliated package, and a streamline process for this. This new process is aimed at ... The review process for becoming a SunPy affiliated package is supposed to be approachable, lightweight and open.  A review process ensures that affiliated packages provide useful functionality to the community at a standard of quality similar to the core SunPy package

The packages themselves are not maintained by the sunpy development team, but require a set of standards to be an affiliated package. 

There is an issue template. 

First the editor will check that the package meets the baseline requirements of an affiliated package, such as checking to see that it is apporpiate and is compatible with the sunpy code of conduct. The project must also have an appopoate licence and is on an online version control platform. It also checks the package provides a python interface, is it on pypi and it is useful to the solar physics community. Following this, a review is undertaken based on the criteria listed below. The reviewer independent of the package before it can be approved as an affiliated package. It's an open review process. 

Don't worry - we will have an Affiliated Package Liason that will help you through each step of this process :) 

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





