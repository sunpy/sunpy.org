=========================
SunPy Affiliated Packages
=========================

What is an affiliated package?
==============================

Affiliated packages are well-maintained, open source software packages
that are useful to solar physicists and integrate well with the SunPy
ecosystem. To aid discoverability, all affiliated packages are listed on
the SunPy website, and they are advertised at national and international
conferences and workshops.

A SunPy sponsored package is an affiliated package that is maintained
and governed by the SunPy project.

Sponsored Packages
==================


SunPy Core
----------
A core package for solar physics in Python.

.. list-table::
   :widths: 15, 20, 60
   :header-rows: 1

   * - Links
     - Maintainer(s)
     - Review
   * - `Docs <https://docs.sunpy.org/>`__, `Code <https://github.com/sunpy/sunpy>`__
     - The SunPy Community
     - |package_general| |integration_well| |docs_extensive| |tests_excellent| |duplication_excellent| |community_excellent| |dev_excellent|
     - :ref:`The SunPy Community <subpackage_maintainers>`


NDCube
------
A base package for multi-dimensional (non)contiguous coordinate-aware arrays.

.. list-table::
   :widths: 15, 20, 60
   :header-rows: 1

   * - Links
     - Maintainer(s)
     - Review
   * - `Docs <https://docs.sunpy.org/projects/ndcube>`__, `Code <https://github.com/sunpy/ndcube>`__
     - `Daniel Ryan`_, `Stuart Mumford`_
     -


drms
----
Access HMI, AIA and MDI data with Python.

.. list-table::
   :widths: 15, 20, 60
   :header-rows: 1

   * - Links
     - Maintainer(s)
     - Review
   * - `Docs <https://docs.sunpy.org/projects/drms>`__, `Code <https://github.com/sunpy/drms>`__
     - `Kolja Glogowski`_
     -


radiospectra
------------
This package aims to provide support for some type of radiospectra on solar physics.

.. list-table::
   :widths: 15, 20, 60
   :header-rows: 1

   * - Links
     - Maintainer(s)
     - Review
   * - `Docs <https://docs.sunpy.org/projects/radiospectra>`__, `Code <https://github.com/sunpy/radiospectra>`__
     - `David Pérez-Suárez`_
     -

Affiliated Packages
===================

Your package here!!



.. _Daniel Ryan: https://github.com/danryanirish
.. _David Pérez-Suárez: https://github.com/dpshelio
.. _Kolja Glogowski: https://github.com/kbg
.. _Stuart Mumford: https://github.com/Cadair


Affiliated Package Review
=========================

Affiliated packages are reviewed before they are accepted for listing on this page.

Review Criteria
---------------

Functionality
~~~~~~~~~~~~~

+---------------+----------------------------------------------------+
|  Status       | Meaning                                            |
+===============+====================================================+
|  |general|    | Implements functionality relevant                  |
|               | to a large amount of the solar                     |
|               | physics communtity.                                |
+---------------+----------------------------------------------------+
| |specialized| | Implements functionality which is                  |
|               | relevant to a specific subsection                  |
|               | of the solar physics community.                    |
+---------------+----------------------------------------------------+
| |notrelevant| | This package should implement                      |
|               | functionality relevant to the                      |
|               | solar physics community to be a                    |
|               | SunPy affiliated package.                          |
+---------------+----------------------------------------------------+

Integration
~~~~~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |well|        | Uses appropriate features in the                    |
|               | core package and integrates well                    |
|               | within the affiliated package                       |
|               | ecosystem (e.g. depends on                          |
|               | appropriate dependencies, uses                      |
|               | appropriate data structures).                       |
+---------------+-----------------------------------------------------+
| |partially|   | Uses some features of the core                      |
|               | library, but could integrate                        |
|               | better with the affiliated                          |
|               | package ecosystem.                                  |
+---------------+-----------------------------------------------------+
| |minimal|     | Does not use many features of the                   |
|               | core library and does not                           |
|               | integrate well within the                           |
|               | affiliated package ecosystem.                       |
+---------------+-----------------------------------------------------+

Documentation
~~~~~~~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |extensive|   | Extensive online                                    |
|               | documentation, all public API                       |
|               | has docstrings describing the                       |
|               | code’s purpose, all inputs and                      |
|               | outputs, and providing                              |
|               | examples. Provides high level                       |
|               | documentation; for example, a                       |
|               | user guide and/or an example                        |
|               | gallery.                                            |
+---------------+-----------------------------------------------------+
| |some|        | Some online documentation. The                      |
|               | public API is documented, but                       |
|               | may have some missing or                            |
|               | incomplete docstrings. The                          |
|               | documentation is missing                            |
|               | guides, tutorials or other                          |
|               | high level documentation.                           |
+---------------+-----------------------------------------------------+
| |little|      | Little to no online                                 |
|               | documentation is provided in                        |
|               | the version control                                 |
|               | repository. No guides or                            |
|               | tutorials.                                          |
+---------------+-----------------------------------------------------+

Testing
~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |excellent|   | A high quality testing suite                        |
|               | exists which tests individual                       |
|               | functions (e.g. functions,                          |
|               | classes) as well as providing                       |
|               | integration tests. Code coverage                    |
|               | is good. Testing is automated and                   |
|               | run frequently.                                     |
+---------------+-----------------------------------------------------+
| |good|        | Unit tests of individual                            |
|               | components (e.g. functions,                         |
|               | classes) and integration tests,                     |
|               | but coverage is minimal. Testing                    |
|               | is automated.                                       |
+---------------+-----------------------------------------------------+
| |needs_work|  | Lacks tests and/or tests are not                    |
|               | executed in a test framework                        |
|               | (e.g. pytest).                                      |
+---------------+-----------------------------------------------------+

Duplication
~~~~~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |none|        | No code or functionality is                         |
|               | duplicated from core other                          |
|               | affiliated packages, or other                       |
|               | relevant packages. Builds on top                    |
|               | of the affiliated package                           |
|               | ecosystem.                                          |
+---------------+-----------------------------------------------------+
| |some|        | Some code or functionality                          |
|               | duplication, functionality                          |
|               | already exists in the ecosystem.                    |
+---------------+-----------------------------------------------------+
| |major|       | Duplicates major existing                           |
|               | functionality.                                      |
+---------------+-----------------------------------------------------+

Engagement
~~~~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |excellent|   | The developers are active and                       |
|               | engaged with the SunPy community.                   |
|               | They actively solicit feedback                      |
|               | and work with other developers to                   |
|               | improve ecosystem integration.                      |
+---------------+-----------------------------------------------------+
| |good|        | The package is developed openly.                    |
|               | The developers have adopted a                       |
|               | compatible Code of Conduct. They                    |
|               | welcome contributions, maintain                     |
|               | and respond to an issue tracker,                    |
|               | and implement appropriate                           |
|               | community feedback.                                 |
+---------------+-----------------------------------------------------+
| |needs_work|  | Code is maintained in hosted                        |
|               | version control, but decisions                      |
|               | are made without community input.                   |
|               | Lacks a Code of Conduct. It is                      |
|               | not clear how to make a                             |
|               | contribution or whether                             |
|               | contributions are welcome.                          |
|               | Developers do not respond to                        |
|               | issues or an issue tracker is not                   |
|               | used.                                               |
+---------------+-----------------------------------------------------+

Development Status
~~~~~~~~~~~~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |excellent|   | Public API stable, beaking                          |
|               | changes limited to across                           |
|               | released versions, formal                           |
|               | development and release process                     |
|               | producing stable versioned                          |
|               | releases.                                           |
+---------------+-----------------------------------------------------+
| |good|        | Public API mostly stable,                           |
|               | informal development and release                    |
|               | process producing stable                            |
|               | versioned releases.                                 |
+---------------+-----------------------------------------------------+
| |needs_work|  | Public API rapidly changing, no                     |
|               | established development, release,                   |
|               | deprecation processes.                              |
+---------------+-----------------------------------------------------+

Outcomes
--------

+-------------+-----------------------------------------------------+
| Outcomes    | Meaning                                             |
+=============+=====================================================+
| Accepted    | Affiliated packages can only be                     |
|             | accepted into the list if there                     |
|             | are no red scores and at least                      |
|             | one green in any category except                    |
|             | relevant and useful.                                |
+-------------+-----------------------------------------------------+
| Provisional | A package may be listed as                          |
|             | provisional, as long as it is                       |
|             | assesed to not have a red score                     |
|             | in “Relevant and useful                             |
|             | functionality”, “Duplication” or                    |
|             | “Community Engagement” and is                       |
|             | working towards meeting the rest                    |
|             | of the review criteria.                             |
+-------------+-----------------------------------------------------+
| Not accepted| A package does not satisfy the                      |
|             | provisional criteria.                               |
+-------------+-----------------------------------------------------+

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


Acknowledgements
~~~~~~~~~~~~~~~~

Sections of this page are heavily inspired by the Astropy affiliated package review process.

.. |general| image:: https://img.shields.io/badge/General_Package-brightgreen.svg
.. |specialized| image:: https://img.shields.io/badge/Specialized_Package-brightgreen.svg
.. |notrelevant| image:: https://img.shields.io/badge/Not_Relevant-red.svg
.. |well| image:: https://img.shields.io/badge/Well_Integrated-brightgreen.svg
.. |partially| image:: https://img.shields.io/badge/Partially_Integrated-orange.svg
.. |minimal| image:: https://img.shields.io/badge/Minimal_Integration-red.svg
.. |extensive| image:: https://img.shields.io/badge/Extensive-brightgreen.svg
.. |some| image:: https://img.shields.io/badge/Some-orange.svg
.. |little| image:: https://img.shields.io/badge/Little-red.svg
.. |excellent| image:: https://img.shields.io/badge/Excellent-brightgreen.svg
.. |good| image:: https://img.shields.io/badge/Good-orange.svg
.. |needs_work| image:: https://img.shields.io/badge/Needs_Work-red.svg
.. |none| image:: https://img.shields.io/badge/None-brightgreen.svg
.. |major| image:: https://img.shields.io/badge/Major-red.svg


.. |package_general| image:: https://img.shields.io/badge/Functionality-General_Package-brightgreen.svg
.. |package_specialized| image:: https://img.shields.io/badge/Functionality-Specialized_Package-brightgreen.svg
.. |package_not_relevant| image:: https://img.shields.io/badge/Functionality-Not_Relevant-red.svg
.. |integration_well| image:: https://img.shields.io/badge/Integration-Well_Integrated-brightgreen.svg
.. |integration_partially| image:: https://img.shields.io/badge/Integration-Partially_Integrated-orange.svg
.. |integration_minimal| image:: https://img.shields.io/badge/Integration-Minimal_Integration-red.svg
.. |docs_extensive| image:: https://img.shields.io/badge/Documentation-Extensive-brightgreen.svg
.. |docs_some| image:: https://img.shields.io/badge/Documentation-Some-orange.svg
.. |docs_little| image:: https://img.shields.io/badge/Documentation-Little-red.svg
.. |tests_excellent| image:: https://img.shields.io/badge/Testing-Excellent-brightgreen.svg
.. |tests_good| image:: https://img.shields.io/badge/Testing-Good-orange.svg
.. |tests_needs_work| image:: https://img.shields.io/badge/Testing-Needs_Work-red.svg
.. |duplication_none| image:: https://img.shields.io/badge/Duplication-None-brightgreen.svg
.. |duplication_some| image:: https://img.shields.io/badge/Duplication-Some-orange.svg
.. |duplication_major| image:: https://img.shields.io/badge/Duplication-Major-red.svg
.. |community_excellent| image:: https://img.shields.io/badge/Engagement-Excellent-brightgreen.svg
.. |community_good| image:: https://img.shields.io/badge/Engagement-Good-orange.svg
.. |community_needs_work| image:: https://img.shields.io/badge/Engagement-Needs_Work-red.svg
.. |dev_excellent| image:: https://img.shields.io/badge/Development_Status-Excellent-brightgreen.svg
.. |dev_good| image:: https://img.shields.io/badge/Development_Status-Good-orange.svg
.. |dev_needs_work| image:: https://img.shields.io/badge/Development_Status-Needs_Work-red.svg
