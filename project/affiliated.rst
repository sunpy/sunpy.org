:tocdepth: 3

=========================
SunPy Affiliated Packages
=========================

What is an affiliated package?
==============================

Affiliated packages are well-maintained, open source software packages that are useful to solar physicists and integrate well with the SunPy ecosystem.
To aid discoverability, all affiliated packages are listed on the SunPy website, and the SunPy project tries to advertise them at national and international conferences and workshops.

A SunPy sponsored package is an affiliated package that is maintained and governed by the SunPy project.

Sponsored Packages
==================


sunpy core
----------
A core package for solar physics in Python.

.. list-table::
   :widths: 15, 20, 60
   :header-rows: 1

   * - Links
     - Maintainer(s)
     - Review
   * - `Docs <https://docs.sunpy.org/>`__, `Code <https://github.com/sunpy/sunpy>`__
     - :ref:`The SunPy Community <subpackage_maintainers>`
     - |package_general| |integration_well| |docs_extensive| |tests_excellent| |duplication_none| |community_excellent| |dev_stable|


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
     - |package_general| |integration_well| |docs_extensive| |tests_excellent| |duplication_none| |community_excellent| |dev_stable|


drms
----
Provides search capability for the JSOC DRMS server which enables complex queries of HMI, AIA and MDI data.

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


Provisional Affiliated Packages
===============================

Your package here!!


.. _Daniel Ryan: https://github.com/danryanirish
.. _David Pérez-Suárez: https://github.com/dpshelio
.. _Kolja Glogowski: https://github.com/kbg
.. _Stuart Mumford: https://github.com/Cadair


Affiliated Package Review
=========================

Each candidate package is reviewed by a reviewer independent of the package before it can be approved as an affiliated package.

Review Criteria
---------------

.. _review_functionality:

Functionality
~~~~~~~~~~~~~

+---------------+----------------------------------------------------+
|  Status       | Meaning                                            |
+===============+====================================================+
|  |general|    | Implements functionality relevant                  |
|               | to a large cross-section of the solar              |
|               | physics community.                                 |
+---------------+----------------------------------------------------+
| |specialized| | Implements functionality which is                  |
|               | relevant to a specific subsection                  |
|               | of the solar physics community.                    |
+---------------+----------------------------------------------------+
| |notrelevant| | This package does not implement                    |
|               | functionality relevant to the                      |
|               | solar physics community.                           |
+---------------+----------------------------------------------------+

.. _review_integration:

Integration
~~~~~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |well|        | Uses appropriate features in the                    |
|               | sunpy core package and integrates well              |
|               | within the affiliated package                       |
|               | ecosystem (e.g., has                                |
|               | appropriate dependencies, uses                      |
|               | appropriate data structures).                       |
+---------------+-----------------------------------------------------+
| |partially|   | Uses some features of the core                      |
|               | library and affiliated package ecosystem, but could |
|               | integrate better or use more features.              |
+---------------+-----------------------------------------------------+
| |minimal|     | Makes little use of the applicable features of the  |
|               | core library and does not                           |
|               | integrate well within the                           |
|               | affiliated package ecosystem.                       |
+---------------+-----------------------------------------------------+

.. _review_documentation:

Documentation
~~~~~~~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |extensive|   | Extensive online                                    |
|               | documentation, the public API                       |
|               | has formatted docstrings describing the             |
|               | code’s purpose, all inputs and                      |
|               | outputs, and includes                               |
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

.. _review_testing:

Testing
~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |excellent|   | A high quality testing suite                        |
|               | exists which test all of the                        |
|               | individual components (e.g. functions,              |
|               | classes) as well as providing                       |
|               | integration tests. Code coverage                    |
|               | is good. Testing is automated and                   |
|               | runs frequently.                                    |
+---------------+-----------------------------------------------------+
| |good|        | Unit tests of individual                            |
|               | components (e.g. functions,                         |
|               | classes) and integration tests,                     |
|               | but coverage is not extensive. Testing              |
|               | is automated.                                       |
+---------------+-----------------------------------------------------+
| |needs_work|  | Lacks tests and/or tests are not                    |
|               | executed in a test framework                        |
|               | (e.g. pytest).                                      |
+---------------+-----------------------------------------------------+

.. _review_duplication:

Duplication
~~~~~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |none|        | No code or functionality is                         |
|               | duplicated from core, other                         |
|               | affiliated packages, or other                       |
|               | relevant packages.                                  |
+---------------+-----------------------------------------------------+
| |some|        | Some code or functionality                          |
|               | duplication, functionality                          |
|               | already exists in other affiliated packages.        |
+---------------+-----------------------------------------------------+
| |major|       | Duplicates major existing functionality in other    |
|               | affiliated packages.                                |
+---------------+-----------------------------------------------------+

.. _review_community:

Community
~~~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |excellent|   | The developers actively solicit input on decisions  |
|               | and feedback and work with other developers to      |
|               | improve ecosystem integration. The developers are   |
|               | active and engaged with the community.              |
|               | The package must also meet the requirements for a   |
|               | 'Good' rating.                                      |
+---------------+-----------------------------------------------------+
| |good|        | The package is developed openly.                    |
|               | The developers have adopted a                       |
|               | Code of Conduct compatible with SunPy's. They       |
|               | welcome contributions, maintain                     |
|               | and respond to an issue tracker,                    |
|               | and are receptive to appropriate                    |
|               | community feedback.                                 |
+---------------+-----------------------------------------------------+
| |needs_work|  | Code is maintained in hosted                        |
|               | version control, but decisions                      |
|               | are often made without considering community input  |
|               | or feedback. Lacks a Code of Conduct. It is         |
|               | not clear how to make a                             |
|               | contribution or whether                             |
|               | contributions are welcome.                          |
|               | Developers do not respond to                        |
|               | issues or an issue tracker is not                   |
|               | used.                                               |
+---------------+-----------------------------------------------------+

.. _review_development:

Development Status
~~~~~~~~~~~~~~~~~~

+---------------+-----------------------------------------------------+
| Status        | Meaning                                             |
+===============+=====================================================+
| |stable|      | Package is well maintained, contributions are       |
|               | responded to by the developers. API stability       |
|               | is prioritised and regular versioned releases       |
|               | are made, with any breaking changes well documented.|
+---------------+-----------------------------------------------------+
| |stc_dev|     | Package is well maintained, but large API changes   |
|               | may be frequent due to rapid development.           |
|               | Contributions are responded to by the developers.   |
|               | Versioned releases exist and changes are documented.|
+---------------+-----------------------------------------------------+
||low_activity| | Package is functional but with little or no activity|
|               | from the developers. The package has versioned      |
|               | releases and is functional.                         |
+---------------+-----------------------------------------------------+
| |needs_work|  | Package is no longer maintained and is not          |
|               | functional.                                         |
+---------------+-----------------------------------------------------+

.. _review_outcomes:

Outcomes
--------

+---------------+-----------------------------------------------------+
| Outcomes      | Meaning                                             |
+===============+=====================================================+
| Accepted      | To be accepted, affiliated packages must have a     |
|               | green score in relevant and useful and at least one |
|               | other. They must also have no red scores.           |
+---------------+-----------------------------------------------------+
| Provisional   | After review a package is listed as                 |
|               | provisional, as long as it is                       |
|               | assessed to not have a red score                    |
|               | in the “Functionality",                             |
|               | “Duplication” or                                    |
|               | “Community” criteria and is                         |
|               | working towards meeting the rest                    |
|               | of the review criteria.                             |
+---------------+-----------------------------------------------------+
| Not accepted  | A package does not currently satisfy the            |
|               | provisional criteria.                               |
+---------------+-----------------------------------------------------+

Open review process
-------------------

The review process for becoming a SunPy affiliated package is designed to be approachable, lightweight and open.
Reviews are conducted in GitHub issues through the https://github.com/sunpy/sunpy.org repository.

Steps for Getting New Packages Reviewed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

0. If you’re not sure whether to submit your package for the affiliated package review process, you can open an issue to informally discuss your package or contact the :ref:`role_affiliated-liaison` to discuss your package privately.
1. Open a new issue with the issue template.
2. The :ref:`role_affiliated-liaison` will identify a reviewer independent of your package.
3. The reviewer evaluates the affiliated package against the review criteria.
4. The reviewer adds their review as a comment to the issue.
5. Based on the scores in each of the seven categories, the affiliated package is either accepted, given provisional status, or provided feedback on how to meet the criteria.
6. Based on the scores, the submitting author can decide if they want their package displayed on the website.
7. The submitting author has the right to ask for another review. In this case, the :ref:`role_affiliated-liaison` will identify a new independent reviewer. This new review will be added to the same issue.
8. If the review passed the review criteria then the submitting author or the :ref:`role_affiliated-liaison` opens a pull request to add their package to the sunpy.org website.
9. The :ref:`role_affiliated-liaison` merges the pull request.
    

Steps for Getting Existing Packages Reviewed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Existing affiliated packages will be reviewed once per year by the :ref:`role_affiliated-liaison` to ensure the review is current.
Developers may challenge a new review, which then requires the liaison to get an independent reviewer to perform the review.

Existing provisional affiliated packages will be reviewed once per year by the :ref:`role_affiliated-liaison`.
They must still be working towards meeting the rest of the review criteria.


Acknowledgements
~~~~~~~~~~~~~~~~

Sections of this page are heavily inspired by the `Astropy affiliated package review process <https://github.com/astropy/project/blob/master/affiliated/affiliated_package_review_guidelines.md>`__.

.. |general| image:: https://img.shields.io/badge/General_Package-brightgreen.svg
.. |specialized| image:: https://img.shields.io/badge/Specialized_Package-brightgreen.svg
.. |notrelevant| image:: https://img.shields.io/badge/Not_Relevant-red.svg
.. |well| image:: https://img.shields.io/badge/Well_Integrated-brightgreen.svg
.. |partially| image:: https://img.shields.io/badge/Partially_Integrated-orange.svg
.. |minimal| image:: https://img.shields.io/badge/Minimal_Integration-red.svg
.. |extensive| image:: https://img.shields.io/badge/Extensive-brightgreen.svg
.. |some| image:: https://img.shields.io/badge/Some-orange.svg
.. |little| image:: https://img.shields.io/badge/Little-red.svg
.. |none| image:: https://img.shields.io/badge/None-brightgreen.svg
.. |major| image:: https://img.shields.io/badge/Major-red.svg
.. |stable| image:: https://img.shields.io/badge/Stable-brightgreen.svg
.. |stc_dev| image:: https://img.shields.io/badge/Subject_to_change-orange.svg
.. |low_activity| image:: https://img.shields.io/badge/Low_activity-orange.svg
.. |excellent| image:: https://img.shields.io/badge/Excellent-brightgreen.svg
.. |good| image:: https://img.shields.io/badge/Good-orange.svg
.. |needs_work| image:: https://img.shields.io/badge/Needs_Work-red.svg


.. |package_general| image:: https://img.shields.io/badge/Functionality-General_Package-brightgreen.svg
   :target: `review_functionality`_
.. |package_specialized| image:: https://img.shields.io/badge/Functionality-Specialized_Package-brightgreen.svg
   :target: `review_functionality`_
.. |package_not_relevant| image:: https://img.shields.io/badge/Functionality-Not_Relevant-red.svg
   :target: `review_functionality`_
.. |integration_well| image:: https://img.shields.io/badge/Integration-Well_Integrated-brightgreen.svg
   :target: `review_integration`_
.. |integration_partially| image:: https://img.shields.io/badge/Integration-Partially_Integrated-orange.svg
   :target: `review_integration`_
.. |integration_minimal| image:: https://img.shields.io/badge/Integration-Minimal_Integration-red.svg
   :target: `review_integration`_
.. |docs_extensive| image:: https://img.shields.io/badge/Documentation-Extensive-brightgreen.svg
   :target: `review_documentation`_
.. |docs_some| image:: https://img.shields.io/badge/Documentation-Some-orange.svg
   :target: `review_documentation`_
.. |docs_little| image:: https://img.shields.io/badge/Documentation-Little-red.svg
   :target: `review_documentation`_
.. |tests_excellent| image:: https://img.shields.io/badge/Testing-Excellent-brightgreen.svg
   :target: `review_testing`_
.. |tests_good| image:: https://img.shields.io/badge/Testing-Good-orange.svg
   :target: `review_testing`_
.. |tests_needs_work| image:: https://img.shields.io/badge/Testing-Needs_Work-red.svg
   :target: `review_testing`_
.. |duplication_none| image:: https://img.shields.io/badge/Duplication-None-brightgreen.svg
   :target: `review_duplication`_
.. |duplication_some| image:: https://img.shields.io/badge/Duplication-Some-orange.svg
   :target: `review_duplication`_
.. |duplication_major| image:: https://img.shields.io/badge/Duplication-Major-red.svg
   :target: `review_duplication`_
.. |community_excellent| image:: https://img.shields.io/badge/Engagement-Excellent-brightgreen.svg
   :target: `review_community`_
.. |community_good| image:: https://img.shields.io/badge/Engagement-Good-orange.svg
   :target: `review_community`_
.. |community_needs_work| image:: https://img.shields.io/badge/Engagement-Needs_Work-red.svg
   :target: `review_community`_
.. |dev_stable| image:: https://img.shields.io/badge/Development_Status-Stable-brightgreen.svg
   :target: `review_development`_
.. |dev_stc| image:: https://img.shields.io/badge/Development_Status-Subject_to_change-orange.svg
   :target: `review_development`_
.. |dev_low| image:: https://img.shields.io/badge/Development_Status-Low_Activity-orange.svg
   :target: `review_development`_
.. |dev_needs_work| image:: https://img.shields.io/badge/Development_Status-Needs_Work-red.svg
   :target: `review_development`_
