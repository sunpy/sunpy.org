Affiliated Packages
===================

An affiliated package is a Python package related to Solar Physics that is not part of the SunPy core library, but can be included in the future as part of the SunPy project’s community.

As a community-driven project SunPy thus encourages contributions from a diverse group of people on building such software that has the potential to be a future **Affiliated SunPy Package**.

Requirements to be satisfied:

*  The package must make use of all appropriate features in the core SunPy library, to reduce code duplication and complexity.
*  The software must provide documentation that explains the function and use of the package, and this documentation should be of comparable standard to the core SunPy library.
*  The code should as far as possible provide an easy to run test suite to verify the correct operation of the package.
*  The developers of an affiliated package should engage with the rest of the SunPy community to encourage knowledge and code sharing within
   the community.

Please look at `SEP-4`_ to read about our policies surrounding affiliated packages.
Please send an email to `our mailing list`_ to start a dialogue.

.. _SEP-4: https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0004.md
.. _our mailing list: https://groups.google.com/forum/#!forum/sunpy

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
   * - `IRISPy <https://github.com/sunpy/irispy>`_
     - 	A package for handling data from the IRIS satellite
     - `IRISPy docs <https://docs.sunpy.org/projects/irispy/en/latest/>`_
     - `Daniel Ryan`_

.. _Daniel Ryan: https://github.com/danryanirish
.. _David Pérez-Suárez: https://github.com/dpshelio
.. _Kolja Glogowski: https://github.com/kbg


Affiliated Package Review Process
=================================

Review Criteria
---------------

+-----------------------------------+-----------------------------------+
| Status                            | Meaning                           |
+===================================+===================================+
| |image0|                          | This is the standard we want all  |
|                                   | packages to aim for.              |
+-----------------------------------+-----------------------------------+
| |image1|                          | Having orange scores is fine, but |
|                                   | is both a warning to the user     |
|                                   | that not all is perfect about the |
|                                   | package, and an incentive for     |
|                                   | developers to improve and reach   |
|                                   | green.                            |
+-----------------------------------+-----------------------------------+
| |image2|                          | Affiliated packages can only be   |
|                                   | accepted into the list if there   |
|                                   | are no red scores and at least    |
|                                   | one green in any category except  |
|                                   | relevant and useful.              |
+-----------------------------------+-----------------------------------+

**Provisional Status**

A package may be listed as provisional, as long as it is assesed to not
have a red score in “Relevant and useful functionality”, “duplication”
or “communtiy engagement” and is working towards meeting the rest of the
review criteria.

Relevant and Useful Functionality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Status                            | Meaning                           |
+===================================+===================================+
| |image3|                          | Implements functionality relevant |
|                                   | to a large amount of the solar    |
|                                   | physics communtity.               |
+-----------------------------------+-----------------------------------+
| |image4|                          | Implements functionality which is |
|                                   | relevant to a specific subsection |
|                                   | of the solar physics community.   |
+-----------------------------------+-----------------------------------+
| |image5|                          | This package should implement     |
|                                   | functionality relevant to the     |
|                                   | solar physics community to be a   |
|                                   | SunPy affiliated package.         |
+-----------------------------------+-----------------------------------+

Make use of all appropriate features in the core library/Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Status                            | Meaning                           |
+===================================+===================================+
| |image6|                          | Uses appropriate features in the  |
|                                   | core package and integrates well  |
|                                   | within the affiliacted package    |
|                                   | ecosystem (e.g. depends on        |
|                                   | appropriate dependencies, uses    |
|                                   | appropriate data structures).     |
+-----------------------------------+-----------------------------------+
| |image7|                          | Uses some features of the core    |
|                                   | library, but could integrate      |
|                                   | better with the affiliated        |
|                                   | package ecosystem.                |
+-----------------------------------+-----------------------------------+
| |image8|                          | Does not use many features of the |
|                                   | core library and does not         |
|                                   | integrate well within the         |
|                                   | affiliated package ecosystem.     |
+-----------------------------------+-----------------------------------+

Documentation
~~~~~~~~~~~~~

+-------------------------------------+--------------------------------+
| Status                              | Meaning                        |
+=====================================+================================+
| |image9|                            | Extensive online               |
|                                     | documentation, all public API  |
|                                     | has docstrings describing the  |
|                                     | code’s purpose, all inputs and |
|                                     | outputs, and providing         |
|                                     | examples. Provides high level  |
|                                     | documentation; for example, a  |
|                                     | user guide and/or an example   |
|                                     | gallery.                       |
+-------------------------------------+--------------------------------+
| |image10|                           | Some online documentation. The |
|                                     | public API is documented, but  |
|                                     | may have some missing or       |
|                                     | incomplete docstrings. The     |
|                                     | documentation is missing       |
|                                     | guides, tutorials or other     |
|                                     | high level documentation.      |
+-------------------------------------+--------------------------------+
| |image11|                           | Little to no online            |
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
| |image12|                         | A high quality testing suite      |
|                                   | exists which tests individual     |
|                                   | functions (e.g. functions,        |
|                                   | classes) as well as providing     |
|                                   | integration tests. Code coverage  |
|                                   | is good. Testing is automated and |
|                                   | run frequently.                   |
+-----------------------------------+-----------------------------------+
| |image13|                         | Unit tests of individual          |
|                                   | components (e.g. functions,       |
|                                   | classes) and integration tests,   |
|                                   | but coverage is minimal. Testing  |
|                                   | is automated.                     |
+-----------------------------------+-----------------------------------+
| |image14|                         | Lacks tests and/or tests are not  |
|                                   | executed in a test framework      |
|                                   | (e.g. pytest).                    |
+-----------------------------------+-----------------------------------+

Duplication
~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Status                            | Meaning                           |
+===================================+===================================+
| |image15|                         | No code or functionality is       |
|                                   | duplicated from core other        |
|                                   | affiliated packages, or other     |
|                                   | relevant packages. Builds on top  |
|                                   | of the affiliated package         |
|                                   | exosystem.                        |
+-----------------------------------+-----------------------------------+
| |image16|                         | Some code or functionality        |
|                                   | duplication, functionality        |
|                                   | already exists in the ecosystem.  |
+-----------------------------------+-----------------------------------+
| |image17|                         | Duplicates major existing         |
|                                   | functionality.                    |
+-----------------------------------+-----------------------------------+

Community Engagement
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Status                            | Meaning                           |
+===================================+===================================+
| |image18|                         | The developers are active and     |
|                                   | engaged with the SunPy community. |
|                                   | They actively solicit feedback    |
|                                   | and work with other developers to |
|                                   | improve ecosystem integration.    |
+-----------------------------------+-----------------------------------+
| |image19|                         | The package is developed openly.  |
|                                   | The developers have adopted a     |
|                                   | compatible Code of Conduct. They  |
|                                   | welcome contributions, maintain   |
|                                   | and respond to an issue tracker,  |
|                                   | and implement appropriate         |
|                                   | community feedback.               |
+-----------------------------------+-----------------------------------+
| |image20|                         | Code is maintained in hosted      |
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
| |image21|                         | Public API stable, beaking        |
|                                   | changes limited to across         |
|                                   | released versions, formal         |
|                                   | development and release process   |
|                                   | producing stable versioned        |
|                                   | releases.                         |
+-----------------------------------+-----------------------------------+
| |image22|                         | Public API mostly stable,         |
|                                   | informal development and release  |
|                                   | process producing stable          |
|                                   | versioned releases.               |
+-----------------------------------+-----------------------------------+
| |image23|                         | Public API rapidly changing, no   |
|                                   | established development, release, |
|                                   | deprecation processes.            |
+-----------------------------------+-----------------------------------+

Open review process
-------------------

Packages can apply for SunPy Affiliated Package status by going through
the following review process: \* Look at `rOpenSci review
process <https://ropensci.org/blog/2016/03/28/software-review/>`__ \*
Look at `pyOpenSci review
process <https://www.pyopensci.org/dev_guide/peer_review/peer_review_proc.html>`__
\* Look at `AstroPy review
process <https://github.com/astropy/project/blob/master/affiliated/affiliated_package_review_guidelines.md>`__
\* Look at `Mozilla Review
Process <https://mozillascience.github.io/codeReview/review.html>`__

Steps to Get Your Package Reviewed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open PR against website with details of package

   -  Provide template (maybe md or yaml)

-  Editors will identify an non-conflicted reviewer
-  Review against criteria
-  The reviewer will issue a review.
-  Add review results to PR
-  The developer can challenge the review and asked for another
   reviewer. This new review will be added to the same PR.
-  Merge PR
-  If the review passed the review criteria then then Build affiliated
   package list into website

The same process as above will be applied for asking for provisional
status.

Potential packages may request a private pre-review assesment by opening
an issue or contacting the editor.

Need to create a template PR.

Existing affiliated Packages will be reviewed by the editors once per
year. The new review will be posted as a PR. Developers may challenge a
new review which requires the editors to get an external reviewer to
perform the review.

Existing provisional affiliated will be reviewed once per year by the
editors. They must still be working towards meeting the rest of the
review criteria.

**Affiliated package designation** Once a package is accepted as a SunPy
Affiliated Package, the SunPy Project will support it as follows: \*
Look at
`SEP-4 <https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0004.md>`__

.. |image0| image:: https://img.shields.io/badge/Excellent-brightgreen.svg
.. |image1| image:: https://img.shields.io/badge/Good-orange.svg
.. |image2| image:: https://img.shields.io/badge/Needs_Work-red.svg
.. |image3| image:: https://img.shields.io/badge/General_Package-brightgreen.svg
.. |image4| image:: https://img.shields.io/badge/Specialized_Package-brightgreen.svg
.. |image5| image:: https://img.shields.io/badge/Not_Relevant-red.svg
.. |image6| image:: https://img.shields.io/badge/Well_Integrated-brightgreen.svg
.. |image7| image:: https://img.shields.io/badge/Partially_Integrated-orange.svg
.. |image8| image:: https://img.shields.io/badge/Minimal_Integration-red.svg
.. |image9| image:: https://img.shields.io/badge/Extensive-brightgreen.svg
.. |image10| image:: https://img.shields.io/badge/Some-orange.svg
.. |image11| image:: https://img.shields.io/badge/Little-red.svg
.. |image12| image:: https://img.shields.io/badge/Excellent-brightgreen.svg
.. |image13| image:: https://img.shields.io/badge/Good-orange.svg
.. |image14| image:: https://img.shields.io/badge/Needs_Work-red.svg
.. |image15| image:: https://img.shields.io/badge/Excellent-brightgreen.svg
.. |image16| image:: https://img.shields.io/badge/Good-orange.svg
.. |image17| image:: https://img.shields.io/badge/Needs_Work-red.svg
.. |image18| image:: https://img.shields.io/badge/Excellent-brightgreen.svg
.. |image19| image:: https://img.shields.io/badge/Good-orange.svg
.. |image20| image:: https://img.shields.io/badge/Needs_Work-red.svg
.. |image21| image:: https://img.shields.io/badge/Excellent-brightgreen.svg
.. |image22| image:: https://img.shields.io/badge/Good-orange.svg
.. |image23| image:: https://img.shields.io/badge/Needs_Work-red.svg

