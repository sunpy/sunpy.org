.. _roadmap:

=====================
SunPy Project Roadmap
=====================

This section describes the roadmap for the SunPy project which includes the **sunpy** core library.
This roadmap is discussed and reviewed at the yearly SunPy coordination meeting.
It provides a broad outline of what areas we will be investing our time and energy in.

Spectra
*******

Spectra are a vital missing data object in the sunpy core library.
Such a data object should support ingesting data files but also some of the common tasks such as fitting.
Thankfully, significant development has been performed by the astropy community in the `specutils package <https://specutils.readthedocs.io/en/stable/>`__ though it is not yet stable.
We aim to work with the astropy community to build spectrum support that can be utilized for solar spectra.

Multi-dimensional data sets
***************************

N-dimensional data sets are common in solar physics.
For example, a series of images taken sequentially with a CCD camera can be stored as a single 3-D array with two spatial axes and one temporal axis.
The value in each array-element can represent the reading in a pixel at a given time.
In solar physics and astronomy, the relationship between the array element and physical coordinates (e.g. position in the sky, wavelength and others) the location and time in the Universe being observed is often represented by the World Coordinate System (WCS) framework.

The `**ndcube** <https://docs.sunpy.org/projects/ndcube/en/stable/index.html>`__ package has been written to handle these kinds of datasets.
This package provides signficant capabilities that go beyond those of `MapSequence <https://docs.sunpy.org/en/stable/generated/api/sunpy.map.MapSequence.html>`__ for example and can handle data from slit spectragraphs.
We aim to integrate **ndcube** into **sunpy** to improve some of our existing data classes as well as support new ones.

Enabling Contributors, Developers and Users
*******************************************

Feedback from the community has made it clear that improvements are needed to better support our contributors, developers, as well as users.
The following key objectives have been identified to provide the maximum impact.
#. Supporting and encouraging new and existing contributors. 
    Submitting new code or documentation to **sunpy** or affiliated packages has been, historically, an arduous task.
    Many code standards and expectations are not well documented in the developer documentation.
    Merge requests frequently take several rounds of back and forth with reviewers asking for changes which is frustrating and demoralizing especially for new contributors.
    We aim to improve our support for contributors by improving our developer documentation generally but especially by better documenting expectations.
    In addition, we will offer to actively help contributors during development and work to minimize the amount of work needed to contribute.
#. Better support for affiliated packages.
    ???
#. Onboarding new Python users.
    Our documentation and gallery make the assumption that users are already familiar with Python and the scientific Python ecosystem.
    We will aim to provide a range of tutorials for users to learn both Python and **sunpy** at the same time to support users transition from other languages or those just starting their Python journey.
    We plan to use these in live tutorials during conferences and other events depending on the audience.
