.. _role_descriptions:

Community Role Descriptions
===========================

This section describes each of the SunPy projects community (non-board) roles, and lists the current holder(s) of that role.
Roles with no holder listed are vacant and anyone interested in filling them should contact the lead developer or anyone else with a project role.
There is no limit to how many people can share the responsibilities of a role, if you are interested in a role which is filled, contact the person and ask how you can assist them.


.. _role_lead-dev:

Lead Developer and Deputy Lead Developer
----------------------------------------

**Stuart Mumford and Will Barnes (deputy)**

The lead developer (and in their absence their nominated deputy) have overall responsibility for the core package and any sponsored affiliated packages.
The most important responsibility of the lead developer is to have high availability in the communtiy to answer questions and facilitate all contributions.

The role of the lead developer is outlined in `SEP-2 <https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0002.md#the-executive-director>`__ and other SEPs.
They are:

-  Hold regular meetings with the developer community (at least monthly).
-  Make regular reports to the board (at least quarterly).
-  Have push privileges to the SunPy repository and can delegate those privileges.
-  Have ownership privileges to the SunPy GitHub organization and related services.
-  Develop and maintain a submission and review process for proposed affiliated packages which must be included in the core library documentation. (`SEP-4 <https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0004.md#acceptance-process-for-affiliated-packages>`__)
-  Plan a release schedule and present it to the board each calendar year. (`SEP-9 <https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0009.md#detailed-description>`__)

In the governance documents the lead developer is given all the executive responsibilities of running the development side of the SunPy organization.
This roles page splits up these responsibilities, and other related activities, into many roles to share the workload.
The lead developer is expected to assist people who have named roles and ensure that they are happy to continue to fill those roles.

With the roles in this document filled, it is expected that the lead developer(s) perform the following core day-to-day tasks, on the core repo and all sponsored affiliated packages:

-  Reviewing PRs.
-  Triaging issues.
-  Responding to questions on issues, mailing lists and chat.
-  Ensuring releases happen on schedule and making final decisions about what gets included in releases.


**Commitment Level**: The lead developer + deputy roles combined need a large time commitment.
Between running the weekly meetings and ensuring that PRs are reviewed and issues triaged, the shared time commitment of the two roles is probably between 10 and 20 hours a week.

.. _role_ci-maintainer:

Continuous Integration Maintainer
---------------------------------
**Unfilled**

SunPy core and the affiliated packages using the `package-template <https://github.com/sunpy/package-template>`__ all use
the same CI setup.
The primariy responsibility of the CI Maintainer is to keep these resources up to date and fix issues as they arise with new package versions or changes to CI platforms.
An outline of the current CI services used can be found in `the sunpy documentation <https://docs.sunpy.org/en/latest/dev_guide/pr_review_procedure.html#continuous-integration>`__.
A non-exhaustive list of things involved with this role is:

-  Maintaining the `Azure pipeline templates <https://github.com/OpenAstronomy/azure-pipelines-templates>`__.
-  Maintaining Read the Docs.
-  Updating the tox configurations.
-  Investigating new CI services and recommending which ones could be useful.

**Commitment Level**: This role requires keeping an eye on the core repo and other repos’s PRs to spot issues with the CI systems and builds which needs attention.
The time commitment is probably around 3-5 hours per week, with additional scope for improving the status quo.

.. _role_release-manager:

Release Manager
---------------
**Unfilled**

The release manager is responsible for cuting releases of SunPy core,
and assisting with releases of affiliated packages as required. This
comprises of the following main tasks:

-  Ensuring that PRs which need backporting into release branches are backported.
-  Maintaining the CI on release branches.
-  Following the `release checklist <https://github.com/sunpy/sunpy/wiki/Home%3A-Release-Checklist>`__ to make releases.
-  Maintaining the release checklist with updates to the process.
-  Announcing the release to social media, mailing lists and blogs etc.
-  Maintaing the automated release pipeline.
-  Maintaining the conda-forge packages for core and affiliated packages.

**Commitment Level**: The main component of this role is monitoring PRs which get milestoned to be backported to release branches and ensuring the backports happen correctly, and releasing bug fix versions.
This role is probably upto a 3-5 hour time commitment per week, although it varies based on the SunPy release schedule.

.. _role_webmaster:

Webmaster
---------
**Nabil Freij**

The webmaster maintains and improves the sunpy.org website, `sunpy-sphinx-theme <https://github.com/sunpy/sunpy-sphinx-theme>`__ and the `ablog <https://github.com/sunpy/ablog/>`__ sphinx plugin.
This primarily involves:

-  Reviewing pull requests and issues on these repositories.
-  Making releases of the theme and ablog.
-  Updating the website as needed.
-  Implementing analytics on the website and docs.


.. _role_subpackage-maintainer:

Subpackage Maintainer
---------------------
See :ref:`subpackage_maintainers`.

Responsibilities of sub-package maintainers include:

* Evaluating and soliciting new pull requests which are consistent with the sub-package scope and contribution standards.
* Providing material support for open pull requests to enable merging.
* Maintaining and developing the sub-package roadmap consistent with the roadmap of the overall core package.
* Mentoring the next generation of maintainers and developers.

Responsibilities of documentation maintainers include:

* Overseeing and improving content.
* Soliciting and implementing improvements and new additions to the content.
* Maintaining and improving the documentation infrastructure.


.. _role_lead-mentor:

Lead Newcomer and Summer of Code Mentor
---------------------------------------
**Unfilled and David Pérez-Suárez (GSOC Admin)**

The newcomer mentor is responsible for supporting new users and contributors to sunpy and sponsored affiliated packages.
This involves:

-  Being responsive to GitHub issues, pull requests, mailing lists and chat.
-  Helping new contributors understand SunPy’s development methodologies.
-  Maintaining the `Newcomers Guide <https://github.com/sunpy/sunpy/blob/master/CONTRIBUTING.rst>`__.
-  Leading SunPy’s participation in sprints and events to attract new contributors.
-  Finding other suitable mentors and pairing them with mentees.
-  Leading the project’s interaction with the Open Astronomy organization for the Google Summer of Code project.

**Commitment Level**: This role is seasonal, the peak time for newcomers to the project is during the lead up to GSOC (Feb - April) and Hacktoberfest (October).
During these times the time commitment is probably upwards of 5 hours a week.
There is also a lot of scope for improving our onboarding process as part of this role.

.. _role_comms-lead:

Communication and Education Lead
--------------------------------
**Sophie Murray**

-  Recruits people to write interesting blog posts.
-  Recruits members of the SunPy community to present about the project at relevant conferences (e.g. AAS/SPD, AGU) and maintaining the `Github repo of presentations <https://github.com/sunpy/presentations>`__.
-  Sends updates to the community about the project.
-  Manages the @SunPyProject Twitter account.
-  Moderates the mailing list.
-  Organizes and provides support for tutorials.
-  Maintains the `tutorial notebook repository <https://github.com/sunpy/tutorial-notebooks>`__.
-  Maintains a list of ideas for tutorials and solicits members of the community to develop tutorials according to set standards.
-  Provides any input or guidance to the board Chair about the Code of Conduct.

**Commitment Level**: This role requires 2-3 hours of effort per week, with a lot of scope for developing new community engagement methods.

.. _role_affiliated-liaison:

Affiliated Package Liaison
--------------------------
**Unfilled**

SunPy is starting to develop a set of general affiliated packages, i.e ndcube, sunkit-image and drms as well as instrument specific ones like IRISPy.
Affiliated packages are not very structured currently, although a framework for them exists in
`SEP-4 <https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0004.md#acceptance-process-for-affiliated-packages>`__.

This role would develop a set of processes for both sponsored and non-sponsored affiliated packages, a review procedure for new affiliated packages, and lead the effort to integrate instrument teams with SunPy.

**Commitment Level**: This role needs an investment of time at the beggining to set up the processes for affiliated packages. These processes would then determine the likely time commitment after that.
