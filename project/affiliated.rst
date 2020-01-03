Affiliated Packages
===================

An affiliated package is a Python package related to Solar Physics that is not part of the SunPy core library, but can be included in the future as part of the SunPy project’s community.

As a community-driven project SunPy thus encourages contributions from a diverse group of people on building such software that has the potential to be a future **Affiliated SunPy Package.**

Requirements to be satisfied:

*  The package must make use of all appropriate features in the core SunPy library, to reduce code duplication and complexity.
*  The software must provide documentation that explains the function and use of the package, and this documentation should be of comparable standard to the core SunPy library.
*  The code should as far as possible provide an easy to run test suite to verify the correct operation of the package.
*  The developers of an affiliated package should engage with the rest of the SunPy community to encourage knowledge and code sharing within
   the community.

Please look at `this SEP`_ to read about our policies surrounding affiliated packages.
Please send an email to the `mailing list`_ to start a dialogue.

.. _this SEP: https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0004.md
.. _mailing list: https://groups.google.com/forum/#!forum/sunpy

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
