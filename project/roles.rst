.. _role_descriptions:

===========================
Community Role Descriptions
===========================

This section describes each of the SunPy projects community (executive) roles, and lists the current holder(s) of that role. Community members can also participate by being members of the board.
We would like to encourage anyone interested parties to apply to roles which are currently unfilled by contacting  the lead developer or the deputy lead developer.
It is possible for more than one person to share the responsibilities of a role. If you are interested in a role which is filled, contact the individual(s) and ask how you can help.

.. _role_lead-dev:

Lead Developer and Deputy Lead Developer
----------------------------------------

**Stuart Mumford and Will Barnes (deputy)**

The lead developer team have overall responsibility for the core package and any sponsored affiliated packages.
The most important responsibility of the lead developer is to lead the developer community. It is therefore important for this role to be available to the community to answer questions and facilitate and direct contributions.

The role of the lead developer is outlined in `SEP-2 <https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0002.md#the-executive-director>`__ and other SEPs. The lead developer team have push privileges to the SunPy repository and maintain ownership of the SunPy GitHub organization and related services.
Some of the responsibility of the lead developer team are:

-  Hold regular meetings with the developer community (at least monthly).
-  Make regular reports to the board (at least quarterly).
-  Select and support sub-package maintainers. Delegate push privileges to the SunPy repository.
-  Develop and maintain a submission and review process for proposed affiliated packages which must be included in the core library documentation. (`SEP-4 <https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0004.md#acceptance-process-for-affiliated-packages>`__)
-  Plan and execute a release schedule consistent with `SEP-9 <https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0009.md#detailed-description>`__).

The lead developer is delegated all executive responsibilities of running the development side of the SunPy organization.
The following roles are identified and delegate the executive responsibilities of the lead developer to share the workload.
The community and lead developer can define new roles as necessary. It is expected that this team of people work together to support each other and identify new people to fill these roles as needed.

It is expected that the lead developer(s), assisted by the sub-package maintainers, perform the following core day-to-day tasks, on the core repo and all sponsored affiliated packages:

-  Review Pull Requests.
-  Perform triage on the list of issues.
-  Respond to users and developers through various communications channels.
-  Ensure releases occur on time and decide on the scope of releases.

**Estimated Commitment Level**: The lead developer roles require a large commitment, between 10 to 20 hours per week, between the two roles.

.. _role_ci-maintainer:

Continuous Integration Maintainer
---------------------------------
**Conor MacBride**

SunPy core and the affiliated packages using the `package-template <https://github.com/sunpy/package-template>`__ all use
the same CI setup.
The primariy responsibility of the CI Maintainer is to keep these resources up to date and fix issues as they arise with new package versions or changes to CI platforms.
An outline of the current CI services used can be found in `the sunpy documentation <https://docs.sunpy.org/en/latest/dev_guide/pr_review_procedure.html#continuous-integration>`__.
A non-exhaustive list of things involved with this role is:

-  Maintaining the `Azure pipeline templates <https://github.com/OpenAstronomy/azure-pipelines-templates>`__.
-  Maintaining the documentation build pipeline (i.e. Read the Docs).
-  Updating the tox configurations.
-  Investigating new CI services and recommending which ones could be useful.

**Estimated Commitment Level**: 3-5 hours per week. This role requires keeping an eye on the core repo and other repos' PRs to spot issues with the CI systems and builds which needs attention.
The time commitment is probably around 3-5 hours per week, with additional scope for improving the status quo.

.. _role_release-manager:

Release Manager
---------------
**David Stansby**

The release manager is responsible for the logistics of sunpy core releases,
and assisting with releases of affiliated packages as required. This
comprises of the following main tasks:

-  Ensuring that PRs are backported as appropriate.
-  Working with the CI maintainer to maintain the CI on release branches.
-  Following, maintaining, and improving the `release checklist <https://github.com/sunpy/sunpy/wiki/Home%3A-Release-Checklist>`__ for each release.
-  Notifying the Communications Lead of new releases.
-  Maintaing the automated release pipeline.
-  Maintaining the conda-forge packages for core and affiliated packages.

**Estimated Commitment Level**: 3-5 hours/week. The main component of this role is monitoring PRs which get milestoned to be backported to release branches and ensuring the backports happen correctly, and releasing bug fix versions.

.. _role_webmaster:

Webmaster
---------
**Unfilled**

The webmaster maintains and improves the sunpy.org website, `sunpy-sphinx-theme <https://github.com/sunpy/sunpy-sphinx-theme>`__ and the `ablog <https://github.com/sunpy/ablog/>`__ sphinx plugin.
This primarily involves:

-  Reviewing pull requests and issues on these repositories.
-  Maintaining and improving the website theme and ablog.
-  Updating the website as needed.
-  Implementing analytics on the website and docs.


**Estimated Commitment Level**: Around 1 hour per week, but comes in bursts as PRs are opened.

.. _role_subpackage-maintainer:

Subpackage Maintainer
---------------------

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
-  Helping new contributors understand SunPy's development methodologies.
-  Maintaining the `Newcomers Guide <https://github.com/sunpy/sunpy/blob/master/CONTRIBUTING.rst>`__.
-  Leading SunPy's participation in sprints and events to attract new contributors.
-  Finding other suitable mentors and pairing them with mentees.
-  Leading the project's interaction with the Open Astronomy organization for the Google Summer of Code project.

**Estimated Commitment Level**: 5 hours/week. This role is highly seasonal as the peak time for newcomers to the project is during the lead up to GSOC (Feb - April) and Hacktoberfest (October).
During these times the time commitment is probably around 5 hours per week, at other times it will be less.
There is also a lot of scope for improving our onboarding process as part of this role.

.. _role_comms-lead:

Communication and Education Lead
--------------------------------
**Laura Hayes**

-  Recruits people to write interesting blog posts.
-  Recruits members of the SunPy community to present about the project at relevant conferences (e.g. AAS/SPD, AGU) and maintaining the `Github repo of presentations <https://github.com/sunpy/presentations>`__.
-  Sends updates to the community about the project.
-  Manages the @SunPyProject Twitter account.
-  Moderates the mailing list.
-  Organizes and provides support for tutorials.
-  Maintains the `tutorial notebook repository <https://github.com/sunpy/tutorial-notebooks>`__.
-  Maintains a list of ideas for tutorials and solicits members of the community to develop tutorials according to set standards.
-  Provides any input or guidance to the board Chair about the Code of Conduct.

**Estimated Commitment Level**: 2-3 hours / week. This role has a lot of scope for developing new community engagement methods.

.. _role_affiliated-liaison:

Affiliated Package Liaison
--------------------------
**Unfilled**

SunPy is starting to develop a set of general affiliated packages, i.e ndcube, sunkit-image and drms as well as instrument specific ones like IRISPy.
Affiliated packages are not very structured currently, although a framework for them exists in
`SEP-4 <https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0004.md#acceptance-process-for-affiliated-packages>`__.

This role would develop a set of processes for both sponsored and non-sponsored affiliated packages, a review procedure for new affiliated packages, and lead the effort to integrate instrument teams with SunPy.

**Commitment Level**: This role needs an investment of time at the beggining to set up the processes for affiliated packages. These processes would then determine the likely time commitment after that.
