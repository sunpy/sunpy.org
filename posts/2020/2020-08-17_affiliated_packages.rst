The What, Why, and How of SunPy Affiliated Packages
===================================================

.. post:: August 18 2020
   :author: Laura Hayes
   :tags: sunpy
   :category: Update


What are SunPy affiliated packages?
-----------------------------------
SunPy affiliated packages are well-maintained, open-source software packages that build upon or extend the functionality of the SunPy core library.
The main idea behind affiliated packages is to provide additional tools and functionality to the solar physics community that is considered outside the scope of the SunPy core library, but builds upon it.
Affiliated packages are aimed to integrate well with the SunPy ecosystem and together with the core library offer a diverse software ecosystem for which to perform solar data analysis.
Affiliated packages are reviewed and registered to the SunPy project. 

There are two types of affiliated packages - *sponsored* and *non-sponsored*.
A sponsored affiliated package is an affiliated package that is maintained and overseen by the SunPy project, examples of these include `sunpy core <https://docs.sunpy.org/en/stable/>`_ and `ndcube <https://docs.sunpy.org/projects/ndcube/en/stable/>`_.
Non-sponsored affiliated packages on the other hand remain under the control and maintenance of the original developers, but must meet a set of standards of the SunPy project.
Examples of non-sponsored affiliated packages would be instrument-specific affiliated packages such as `AIApy <https://pypi.org/project/aiapy/>`_.

In this blog post we want to outline our new streamline process for becoming an affiliated package and we want to encourage package developers, particularly instrument teams interested in developing a Python package, to submit their package for review for SunPy affiliate status!

Why would a package want to become an affiliated package?
---------------------------------------------------------
SunPy supports the developement of affiliated packages through our community development efforts and by providing our package template. The SunPy project will also ensure that affiliated packages are publicized to encourage community development.
For example, affiliated packages are listed on the SunPy website, and SunPy adverstises them at conferences and workshops.


Call to instrument/mission teams!
---------------------------------
We invite instrument and mission teams that are interested in developing a Python package to become a SunPy affiliated package. Integrating mission/instrument-specific software within the SunPy ecosystem will be of great benefit to the solar community and will allow for a simplified and unified process for users to perform solar data analysis.
For example, a package may consist of instrument-specific calibration routines which would be outside the scope of SunPy core package, but could build upon the functionality provided by core such as the data containers and file readers.
Developing a mission/instrument specific package as a SunPy affiliated package will allow the code to live and integrate within the SunPy ecosystem.

Furthermore, for mission/instrument teams that would like to begin developing specific Python software, the SunPy project offers support through our package template and community resources for the package to be 'incubated' until it is at the level of affiliate status.
We would really like to encourage instrument/mission teams to reach out!

Package template
----------------
The SunPy project has developed a `package template <https://github.com/sunpy/package-template>`_ which is designed to help developers create new Python packages within the SunPy ecosystem.
The idea is that this template provides a simplified way to standardized packaging, testing, and documentation using the same framework as the SunPy core package.
The SunPy package template makes it easier for package developers to meet the standards required by SunPy to become an affiliated package!


How does a package become an affiliated package?
------------------------------------------------
To become a SunPy affiliated package, a set of criteria need to be met to ensure that affiliated packages provide useful functionality to the community at a standard of quality similar to the core SunPy package.
We now have a new review process for becoming an affiliated package, aimed at being open, approachable and streamlined!

The reviews are performed as an open process through GitHub issues on the `https://github.com/sunpy/sunpy.org` repository.
To submit a package for review to become an affiliated package, an issue should be opened on this repository.
We now have an issue template for submitting a package for review to make it easier to provide all the required information and to start a dialogue about the process. 

Once an issue is open, the Affiliate Package Liaison will check that the package meets the baseline requirements of an affiliated package.
These include checking to see that it is compatible with the Sunpy `Code of Conduct <https://docs.sunpy.org/en/latest/code_of_conduct.html>`_,  has an appropriate licence, provides a Python interface, is on pypi, and is useful to the solar physics community.
Following this, a reviewer independent to the package is assigned and a review is undertaken based on the criteria listed below. 

The review criteria that are assessed are listed as follows with the associated gradings:

* **Functionality**  Does the package provide functionality that is useful and relevant to the solar physics community?

* **Integration**  - Does that package integrate well within the SunPy ecosystem? for example does it make use of all appropriate features in the core library, including the applicable data structures and dependencies?

* **Documentation**  - Does the package have satisfactory documentation that is up to the standard of the core sunpy library including a user guide and examples?

* **Testing** - Does the package use a testing suite to verify the code functionality within its codebase? Does it provide integration tests?

* **Duplication** - Does the package duplicate functionality within sunpy core or any of the other affiliated packages or other relevant packages?

* **Community**  - Is the package openly developed with active input and engagement from users within the community? Does the package have a code of conduct and does this reflect the same values as the SunPy project? 

* **Development Status** - Is the package well maintained? Are contribution responded to by developers? Is the package still under developement with large API changes?

These criteria are reviewed on a 'traffic light' system and ranked 'green', 'orange', or 'red' based on the submitted package.
For full details of how each of criteria are ranked please check out the `Review Criteria <https://sunpy.org/project/affiliated#affiliated-package-review>`_.

For a submitted package to be accepted to affiliate package status, the package must be 'green' in **Functionality**, and one other category.
It must also not list any 'red' scores.

If the package in its current state does not pass the criteria, it can be listed as *Provisional* once it does not list 'red' in the **Functionality**, **Duplication** or **Community** criteria.
The idea is that the package can be listed as Provisional as it is working towards addressing the criteria for which it did not pass the review in. 

We would really like to encourage packages interested in becoming an affiliated SunPy package to please submit an issue and open up a review dialogue. 
We will have an Affiliated Package Liaison that will help you through each step of this process :).
Even if you are unsure about whether you want to submit a package, please feel free to open an issue and informally discuss your package. 

Reach out!
----------
If you are a developer of a package that you think fits nicely into the SunPy ecosystem and will of benefit to the solar physics community and want to chat to us about it please reach out!
This can be of course regardless of how far along the package is - from concept to maturity! Join us our live chat `element channel <https://openastronomy.riot.im/#/room/#sunpy:openastronomy.org>`_ or join in on the SunPy weekly community meetings which occur on Wednesdays at 16:00 UTC and are hosted on `jitsi <https://sunpy.org/jitsi>`_.








