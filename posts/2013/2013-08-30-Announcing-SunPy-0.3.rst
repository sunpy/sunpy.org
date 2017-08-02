Announcing SunPy 0.3
====================

.. post:: 30 August 2013
   :author: Stuart Mumford
   :tags: sunpy, 0.3
   :category: Release

It gives me great pleasure to announce the release of a new version of SunPy.
This version has been rather too long in the making, but is here at last!

SunPy 0.3 is now available through `PyPI <https://pypi.python.org/pypi/sunpy>`_ and via `GitHub <https://github.com/sunpy/sunpy/releases/tag/v0.3.0>`_.
The biggest change in 0.3 is a shift away from our Map and Spectra datatypes inheriting numpy.ndarray to having their array in a `.data` attribute.
This was done to make development of these objects easier and more flexible and also to improve our compatibility with Astropy.
In the process of doing this the map submodule has undergone a massive refactor to streamline the creation and inheritance structure of the module.

Below I highlight some of the major changes, the full change log can be found `here <https://github.com/sunpy/sunpy/blob/stable/RELEASE.txt>`_.

* The biggest change to the Map API is the deprecation of the `make_map` function. It has been replaced by the new `sunpy.Map` factory which is much more intelligent and able to have custom map sources external to the SunPy library register with it, which is handy if you are developing a custom Map source. Along with this change the old top-level map class Map is now called `GenericMap` and is to be created using the Map factory under normal circumstances.
* `MapCube` and `CompositeMap` have also seen some improvements, including the implementation of `draw_limb` and `draw_grid` for both datatypes and a new animation based `plot()` method for `MapCube`.
* To facilitate the changes to map there have also been a lot of improvements to the `io` submodule, including the ability to read all the HDUs from a FITS file and the addition of a `extract_waveunit` function that checks the header for common ways to encode the wavelength unit.
* There has also been a big cleanup of the various top level and submodule namespaces to make imports simpler. Most of this has not changed the user facing API, however there are not nicer ways to import submodules, like `sunpy.util.util` is now the same as sunpy.util.
* The spectra module has been refactored so it also has a `.data` attribute and it’s plotting API is now consistent with that of Map and LightCurve

SunPy 0.3 consits of 9 months of work from 15 people and over 300 commits to the git repository.
The people who have contributed to this release are (in commit order):

* Stuart Mumford
* Russell Hewett
* Florian Mayer
* Steven Christe
* Albert Shih
* Simon Liedtke
* Ankit Angrawal
* Jack Ireland
* Matt Bates
* Nabil Freij
* Keith Hughitt
* David Perez-Suarez
* Tomas Meszaros
* Benjamin Mampaey
* Andrew Leonard

On behalf of all the SunPy developers, we hope you enjoy 0.3!
