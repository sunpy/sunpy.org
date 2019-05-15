GSoC 2019: Project IRISpy 0.1
=============================

.. post:: May 15, 2019
   :author: Kris Stern
   :tags: GSoC, IRISpy, NDCube
   :category: GSoC

The community bonding period of this year’s GSoC is officially under way. The project I am embarking on has to do with adding a new feature to IRISpy, which is a essentially a package that is developed on top of SunPy’s NDCube package, and is written in the popular Python programming language. IRISpy itself (albeit not yet released) provides functionalities to read, manipulate, and visualize data collected with NASA’s `IRIS satellite <http://iris.lmsal.com/>`_ which looks at UV emission from the solar chromosphere. The proposed new feature is a time-dependent instrument response function, which will give scientists far greater power and ability to perform IRIS data analysis in Python, as well as to make new discoveries regarding the energetics and dynamics of the solar chromosphere and transition region than previously allowed. For more information on both the IRIS instrument and IRISpy, please take a look at `the SunPy documentations for IRISpy <https://docs.sunpy.org/projects/irispy/en/latest/introduction.html>`_. 

As the IRISpy repo is hosted on GitHub, most of the “action” will take place there. (Such that the version control will be performed using Git.) `A Pull Request <https://github.com/sunpy/irispy/pull/108>`_ has already been opened in that repo where some preliminary work on the project has already been carried out. And, the required development environment has been set up on my personal computer to develop the new code so that it can be tested locally. For this project, I have opted to use Anaconda as the package management system to create an virtual environment, providing easy access and management to all dependencies via the command line.

The coding part of the IRISpy project is 3-month long, and will kick off on May 28th, 2019 (Hong Kong Standard Time). In the meantime I plan to read up on the background regarding both IRIS and IRISpy, and to study the existing IDL code of the same feature some more before attacking the problem of converting this code from IDL to Python, then benchmarking, and bugfixing, and finally improving the flow and efficiency of the produced Python code. After that, proper documentation will be added to guide the user through the steps of using the new feature. Such documentation will include but not limited to the feature’s docstrings, additions to official SunPy website documentation, and perhaps a brand new Learn Astropy tutorial. After the completion of the project, it is expected that the following tasks will have been accomplished:

1. An improved function for deriving the time-dependent IRIS response function written entirely in Python.
2. Reliably maintaining this new software in terms of benchmarking and unit tests.
3. The new software must be incorporated into the existing methods and functions in IRISpy that depend on the instrument response function.

The IRISpy project is on a topic that is not directly related to my current PhD research (which is mostly on late-stage stellar evolution focusing on planetary nebulae), but will supplement it by expanding my general knowledge of solar physics. And, I expect this undertaking to be a challenge I can grow with, especially by helping me developing good time management skills.

I am looking forward to a great Google Summer of Code ahead.
