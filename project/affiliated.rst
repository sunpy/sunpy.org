SunPy Affiliated Packages
=========================

Sponsored Packages
==================

.. list-table::
   :widths: 30 30 30 30
   :header-rows: 1

   * - Package Name
     - Description
     - Documentation
     - Maintainer
   * - `ndcube <https://github.com/sunpy/ndcube>`_
     - A base package for multi-dimensional (non)contiguous coordinate-aware arrays
     - `ndcube docs <https://docs.sunpy.org/projects/ndcube>`_
     - `Daniel Ryan`_
   * - `drms <https://github.com/sunpy/drms>`_
     -  Access HMI, AIA and MDI data with Python
     - `drms docs <https://docs.sunpy.org/projects/drms>`_
     - `Kolja Glogowski`_
   * - `radiospectra <https://github.com/sunpy/radiospectra>`_
     -  This package aims to provide support for some type of radiospectra on solar physics
     - `radiospectra docs <https://docs.sunpy.org/projects/radiospectra>`_
     - `David Pérez-Suárez`_

.. _Daniel Ryan: https://github.com/danryanirish
.. _David Pérez-Suárez: https://github.com/dpshelio
.. _Kolja Glogowski: https://github.com/kbg


Affiliated Packages
===================

What is an affiliated package?
------------------------------

Affiliated packages are well-maintained, open source software packages
that are useful to solar physicists and integrate well with the SunPy
ecosystem. To aid discoverability, all affiliated packages are listed on
the SunPy website, and they are advertised at national and international
conferences and workshops.

A SunPy sponsored package is an affiliated package that is maintained
and governed by the SunPy project.

Review Criteria
---------------

Relevant and Useful Functionality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Status                            | Meaning                           |
+===================================+===================================+
| |image0|                          | Implements functionality relevant |
|                                   | to a large amount of the solar    |
|                                   | physics communtity.               |
+-----------------------------------+-----------------------------------+
| |image1|                          | Implements functionality which is |
|                                   | relevant to a specific subsection |
|                                   | of the solar physics community.   |
+-----------------------------------+-----------------------------------+
| |image2|                          | This package should implement     |
|                                   | functionality relevant to the     |
|                                   | solar physics community to be a   |
|                                   | SunPy affiliated package.         |
+-----------------------------------+-----------------------------------+

Integration
~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Status                            | Meaning                           |
+===================================+===================================+
| |image3|                          | Uses appropriate features in the  |
|                                   | core package and integrates well  |
|                                   | within the affiliated package     |
|                                   | ecosystem (e.g. depends on        |
|                                   | appropriate dependencies, uses    |
|                                   | appropriate data structures).     |
+-----------------------------------+-----------------------------------+
| |image4|                          | Uses some features of the core    |
|                                   | library, but could integrate      |
|                                   | better with the affiliated        |
|                                   | package ecosystem.                |
+-----------------------------------+-----------------------------------+
| |image5|                          | Does not use many features of the |
|                                   | core library and does not         |
|                                   | integrate well within the         |
|                                   | affiliated package ecosystem.     |
+-----------------------------------+-----------------------------------+

Documentation
~~~~~~~~~~~~~

+-------------------------------------+--------------------------------+
| Status                              | Meaning                        |
+=====================================+================================+
| |image6|                            | Extensive online               |
|                                     | documentation, all public API  |
|                                     | has docstrings describing the  |
|                                     | code’s purpose, all inputs and |
|                                     | outputs, and providing         |
|                                     | examples. Provides high level  |
|                                     | documentation; for example, a  |
|                                     | user guide and/or an example   |
|                                     | gallery.                       |
+-------------------------------------+--------------------------------+
| |image7|                            | Some online documentation. The |
|                                     | public API is documented, but  |
|                                     | may have some missing or       |
|                                     | incomplete docstrings. The     |
|                                     | documentation is missing       |
|                                     | guides, tutorials or other     |
|                                     | high level documentation.      |
+-------------------------------------+--------------------------------+
| |image8|                            | Little to no online            |
|                                     | documentation is provided in   |
|                                     | the version control            |
|                                     | repository. No guides or       |
|                                     | tutorials.                     |
+-------------------------------------+--------------------------------+

Testing
~~~~~~~

+-----------------------------------+-----------------------------------+
| Status                            | Meaning                           |
+===================================+===================================+
| |image9|                          | A high quality testing suite      |
|                                   | exists which tests individual     |
|                                   | functions (e.g. functions,        |
|                                   | classes) as well as providing     |
|                                   | integration tests. Code coverage  |
|                                   | is good. Testing is automated and |
|                                   | run frequently.                   |
+-----------------------------------+-----------------------------------+
| |image10|                         | Unit tests of individual          |
|                                   | components (e.g. functions,       |
|                                   | classes) and integration tests,   |
|                                   | but coverage is minimal. Testing  |
|                                   | is automated.                     |
+-----------------------------------+-----------------------------------+
| |image11|                         | Lacks tests and/or tests are not  |
|                                   | executed in a test framework      |
|                                   | (e.g. pytest).                    |
+-----------------------------------+-----------------------------------+

Duplication
~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Status                            | Meaning                           |
+===================================+===================================+
| |image12|                         | No code or functionality is       |
|                                   | duplicated from core other        |
|                                   | affiliated packages, or other     |
|                                   | relevant packages. Builds on top  |
|                                   | of the affiliated package         |
|                                   | exosystem.                        |
+-----------------------------------+-----------------------------------+
| |image13|                         | Some code or functionality        |
|                                   | duplication, functionality        |
|                                   | already exists in the ecosystem.  |
+-----------------------------------+-----------------------------------+
| |image14|                         | Duplicates major existing         |
|                                   | functionality.                    |
+-----------------------------------+-----------------------------------+

Community Engagement
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Status                            | Meaning                           |
+===================================+===================================+
| |image15|                         | The developers are active and     |
|                                   | engaged with the SunPy community. |
|                                   | They actively solicit feedback    |
|                                   | and work with other developers to |
|                                   | improve ecosystem integration.    |
+-----------------------------------+-----------------------------------+
| |image16|                         | The package is developed openly.  |
|                                   | The developers have adopted a     |
|                                   | compatible Code of Conduct. They  |
|                                   | welcome contributions, maintain   |
|                                   | and respond to an issue tracker,  |
|                                   | and implement appropriate         |
|                                   | community feedback.               |
+-----------------------------------+-----------------------------------+
| |image17|                         | Code is maintained in hosted      |
|                                   | version control, but decisions    |
|                                   | are made without community input. |
|                                   | Lacks a Code of Conduct. It is    |
|                                   | not clear how to make a           |
|                                   | contribution or whether           |
|                                   | contributions are welcome.        |
|                                   | Developers do not respond to      |
|                                   | issues or an issue tracker is not |
|                                   | used.                             |
+-----------------------------------+-----------------------------------+

Maturity and Development Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Status                            | Meaning                           |
+===================================+===================================+
| |image18|                         | Public API stable, beaking        |
|                                   | changes limited to across         |
|                                   | released versions, formal         |
|                                   | development and release process   |
|                                   | producing stable versioned        |
|                                   | releases.                         |
+-----------------------------------+-----------------------------------+
| |image19|                         | Public API mostly stable,         |
|                                   | informal development and release  |
|                                   | process producing stable          |
|                                   | versioned releases.               |
+-----------------------------------+-----------------------------------+
| |image20|                         | Public API rapidly changing, no   |
|                                   | established development, release, |
|                                   | deprecation processes.            |
+-----------------------------------+-----------------------------------+

Outcomes
--------

+-----------------------------------+-----------------------------------+
| Outcomes                          | Meaning                           |
+===================================+===================================+
| Accepted                          | Affiliated packages can only be   |
|                                   | accepted into the list if there   |
|                                   | are no red scores and at least    |
|                                   | one green in any category except  |
|                                   | relevant and useful.              |
+-----------------------------------+-----------------------------------+
| Provisional                       | A package may be listed as        |
|                                   | provisional, as long as it is     |
|                                   | assesed to not have a red score   |
|                                   | in “Relevant and useful           |
|                                   | functionality”, “Duplication” or  |
|                                   | “Community Engagement” and is     |
|                                   | working towards meeting the rest  |
|                                   | of the review criteria.           |
+-----------------------------------+-----------------------------------+
| Not accepted                      | A package does not satisfy the    |
|                                   | provisional criteria.             |
+-----------------------------------+-----------------------------------+

Open review process
-------------------

The review process for becoming a SunPy affiliated package is supposed
to be approachable, lightweight and open. Reviews are conducted by
GitHub pull requests on the https://github.com/sunpy/sunpy.org
repository.

Steps for Getting New Packages Reviewed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

0. If you’re not sure whether to submit your package for the affiliated
   package review process, you can open an issue to informally discuss
   your package or contact the Affiliated Package Liason to discuss your
   package privately.
1. Open a new issue with the issue template.
2. The Affiliated Package Liason will identify an independent reviewer.
3. The reviewer evaluates the affiliated package against the review
   criteria.
4. The reviewer adds their review as a comment to the issue.
5. Based on the scores in each of the seven categories, the affiliated
   package is either accepted or given provisional status.
6. Based on the scores, the submitting author can decide if they want
   their package displayed on the website.
7. The submitting author can challenge the review and ask for another
   reviewer. In this case, the Affiliated Package Liason will identify a
   new independent reviewer. This new review will be added to the same
   issue.
8. If the review passed the review criteria then the submitting author
   opens a pull request to add their package to the Sunpy.org
   `affiliated package
   website <https://sunpy.org/project/affiliated>`__.
9. The Affiliated Package Liason merges the pull request.

Steps for Getting Existing Packages Reviewed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Existing affiliated packages will be reviewed once per year. Developers
may challenge a new review which requires the editors to get an external
reviewer to perform the review.

Existing provisional affiliated will be reviewed once per year by the
editors. They must still be working towards meeting the rest of the
review criteria.

.. |image0| image:: https://img.shields.io/badge/General_Package-brightgreen.svg
.. |image1| image:: https://img.shields.io/badge/Specialized_Package-brightgreen.svg
.. |image2| image:: https://img.shields.io/badge/Not_Relevant-red.svg
.. |image3| image:: https://img.shields.io/badge/Well_Integrated-brightgreen.svg
.. |image4| image:: https://img.shields.io/badge/Partially_Integrated-orange.svg
.. |image5| image:: https://img.shields.io/badge/Minimal_Integration-red.svg
.. |image6| image:: https://img.shields.io/badge/Extensive-brightgreen.svg
.. |image7| image:: https://img.shields.io/badge/Some-orange.svg
.. |image8| image:: https://img.shields.io/badge/Little-red.svg
.. |image9| image:: https://img.shields.io/badge/Excellent-brightgreen.svg
.. |image10| image:: https://img.shields.io/badge/Good-orange.svg
.. |image11| image:: https://img.shields.io/badge/Needs_Work-red.svg
.. |image12| image:: https://img.shields.io/badge/Excellent-brightgreen.svg
.. |image13| image:: https://img.shields.io/badge/Good-orange.svg
.. |image14| image:: https://img.shields.io/badge/Needs_Work-red.svg
.. |image15| image:: https://img.shields.io/badge/Excellent-brightgreen.svg
.. |image16| image:: https://img.shields.io/badge/Good-orange.svg
.. |image17| image:: https://img.shields.io/badge/Needs_Work-red.svg
.. |image18| image:: https://img.shields.io/badge/Excellent-brightgreen.svg
.. |image19| image:: https://img.shields.io/badge/Good-orange.svg
.. |image20| image:: https://img.shields.io/badge/Needs_Work-red.svg
