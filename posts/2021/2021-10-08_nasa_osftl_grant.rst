.. post:: 3rd November 2021
   :author: Stuart Mumford
   :tags: sunpy
   :category: Update

SunPy Awarded NASA Grant
========================

**As part of the NASA "Open Source Tools, Frameworks, and Libraries" program, the SunPy proposal "Strengthening the Foundations of the SunPy Ecosystem" has been funded for the next three years.**

This proposal was submitted in January 2021, and sought funding for both the core `sunpy` package and wider goals of the project.
After `early community input was collected <https://github.com/sunpy/sunpy-project/issues/9>`__, Albert Shih led the proposal itself, with NASA GSFC as the primary institution.
`The proposed effort <https://docs.google.com/document/d/1_gf1HM7iIUVqgHAdDUFQfCUHzHkrEFUTJZP8O3PEoqw>`__ focuses on three main areas:

1. Improving the technical infrastructure.

   This focuses on the tools that the wider project needs to scale up as we adopt more coordinated and affiliated packages.
   To support multiple active projects with a common development workflow, more tooling and infrastructure is needed, both for maintainers of existing packages and developers new to writing affiliated packages.
   As part of this work templates for setting up new packages will be improved, documentation will be written, and new automation and monitoring bots will be developed to ease the burden on the SunPy maintainers.

2. Augmenting science-enabling functionality.

   This section aims to improve the tools provided by the core package to better support future challenges in solar physics data.
   The two main components of this are supporting multi-point observations with improvements to the `sunpy.coordinates` package, and improving the support for very large datasets in `sunpy` and sponsored packages by leveraging the scaling and parallelism tools available from `Dask <https://dask.org>`__.

3. Providing training and outreach

   This section will improve example galleries across both `sunpy` core and affiliated packages, develop training materials for solar physics graduate students, and perform outreach activities with instrument teams and package developers.


What will the money pay for?
----------------------------

The money awarded to this proposal will pay for:

* Albert Shih will manage the project and augment parts of `sunpy.coordinates`.
* Stuart Mumford will work on infrastructure for all sponsored and affiliated packages as discussed in `sunpy/sunpy-project#2 <https://github.com/sunpy/sunpy-project/issues/2>`__.
* Will Barnes will work on the training/outreach and large-dataset-support components of the project.


Finally
-------

This is a major milestone for SunPy - it is the first significant amount of funding dedicated to directly working on the long term sustainability of the project.
This funding will help to significantly grow SunPy, both the core package and the ecosystem of associated packages.
