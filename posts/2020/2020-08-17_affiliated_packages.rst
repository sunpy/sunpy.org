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

There are two types of affiliated packages - *sponsered* and *non-sponsered*. A sponsored afilliated package is an affiliated package that is maintained and governed by the SunPy project, examples of these include `sunpy core <https://docs.sunpy.org/en/stable/>`_ and `ndcube <https://docs.sunpy.org/projects/ndcube/en/stable/>`_. Non-sponsored affiliated packages remain under the control and maintainance of the original developers. Examples of these would be instrument-specific affiliated packages such as `AIApy <https://pypi.org/project/aiapy/>`_.

In this blog post we want to outline our new streamline process for becoming an affiliated package and we want to encourgae package developers, particularly instrument teams interested in developing a Python package to apply for SunPy affilaite status!


Why would a package want to become an affiliated package?
---------------------------------------------------------


    
The type of packages that would become an affiliated package is a code-base or package that is useful to the solar physics community but may be outside the scope of sunpy core. This may be for example some software for a specific mission or instrument, such as calibration routies, and instrument-specific software. non-sponsored affiliated packages remain under the control of the original developers

SunPy is starting to develop a set of general affiliated packages, i.e ndcube, sunkit-image and drms as well as instrument specific ones like IRISPy.

The SunPy project will ensure that affiliated packages are maintained and publicized in order to encourage community development.


The idea would be lalalla


Call to instrument/mission teams!
---------------------------------
We would invite interested mission or instrument teams that are interesed in developing a python package for there instrument to become a affiliated package. This will allow the code to live and develop within the sunpy ecosystem. 

We would like to start the effort to integrate instrument teams with SunPy :tada

The advantage of this is to aid discoverability and tries to advertise them at national and international conferences and workshops.

The packages themselves are not maintained by the sunpy development team, but require a set of standards to be an affiliated package. 

Encourange external packages to apply for affiliate status

Incubator!


Package template
----------------

The SunPy project has developed a `package template <https://github.com/sunpy/package-template>`_ which is designed to help developers create new Python packages within the SunPy ecosystem. The idea is that this template provides a simplified way to standarized packaging, testing, and documentation using the same framework as the sunpy core package. The SunPy package template makes it easier for package developers to meet the standards required by SunPy to become an affiliated package!


How does a package become an affiliated package?
---------------------------------------------------

To become a SunPy affiliated package, a set of criteria need to be met to ensure that affiliated packages provide useful functionality to the community at a standard of quality similar to the core SunPy package. We now have a new review process for becoming an affiliated package, aimed at being open, approachable and streamline!

The reviews are performed as an open process through GitHub issues on the `https://github.com/sunpy/sunpy.org` respository. To submit a package for review to become an affiliated package, an issue should be opened on this repository. We now have an issue template for submitting a package for review to make it easier to provide all the required information and to start a dialogue about the process. 

Once an issue is open, the Affiliate Package Liaison will check that the package meets the baseline requirements of an affiliated package. These include checking to see that it is compatible with the Sunpy `Code of Conduct <https://docs.sunpy.org/en/latest/code_of_conduct.html>`_,  has an appropriate licence, provides a Python interface, is on pypi, and is useful to the solar physics community. Following this, a reviewer independent to the package is assigned and a review is undertaken based on the criteria listed below. 

The review criteria that are assessed are listed as follows with the associated gradings:

* **Functionality**          
   - Possible Gradings: General Package / Specialized Package / Not Relevant
* **Integration**            : Well integrated / Partially Integrated / Minimal Integration
* **Documentation**            : Extensive / Some / Little
* **Testing**                 : Excellent / Good / Needs Work
* **Duplication**              : None / Some / Major
* **Community**                : Excellent / Good / Needs Work
* **Development Status**       : Stable / Subject to Change / Low Activity / Needs Work

The criteria is reviewed based on a 'traffic light' system ranked 'green', 'orange', ro'red' based on the criteria listed aboce. To be accepted the package must be *green* in Functionality, and one other category. It must also not list any red scores.

If the package in its current state does not pass the critera - after review a package is listed as provisional, as long as it is assessed to not have a red score in the “Functionality”, “Duplication” or “Community” criteria and is working towards meeting the rest of the review criteria.

Don't worry - we will have an Affiliated Package Liason that will help you through each step of this process :)

Reach out!
----------
If you are a developer of a package that you think fits nicely into the SunPy ecosystem and will of benefit to the solar physics community and want to chat to us about it please reach out! This can be of course regardless of how far along the package is - from concept to maturity! Join us our live chat `element channel <https://openastronomy.riot.im/#/room/#sunpy:openastronomy.org>`_ or join in on the SunPy weekly community meetings which occur on Wednesdays at 16:00 UTC and are hosted on `jitsi <https://sunpy.org/jitsi>`_.





