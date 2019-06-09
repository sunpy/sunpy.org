GSoC 2019: Project IRISpy 1.1
=============================

.. post:: June 8, 2019
   :author: Kris Stern
   :tags: GSoC, IRISpy, NDCube
   :category: GSoC

It has been two weeks since the commencement of the coding phase… I can’t believe it, as it seems like time files. But to sum up the time that passed the following is a brief summary report for what tasks have been completed and what remains:

The GitHub PR opened for the project can be found at `link here <https://github.com/sunpy/irispy/pull/108>`_. This picks up from a previous unfinished PR #102 `with link here <https://github.com/sunpy/irispy/pull/102>`_, while also addresses Issue #27 with `link <https://github.com/sunpy/irispy/issues/27>`_. The ultimate goal of the project is to work on IRISpy further until it is in a state where it becomes ready for an official release. Basically, we would like to add a time-dependent iris_response() function as well as a function fit_iris_xput() to compute the time-dependent effective areas based on some input observation times and coefficients. So far, four out of the five planned stages of implementation has been carried out, and they are as follows:

1. Triaging
2. Benchmarking
3. Bug-fixing
4. Improving Code Pythonically
5. Incorporating Time-dependent Fitted Response into Wider IRISpy Code-base

Essentially, the first four of the five steps form the workflow for all similar patterns of package development. The details of the difficulty encountered at each stage are to be outlined in the subsections to follow.
§1.1 Triaging

    Most of the groundwork has already been laid in PR#102. Therefore the remaining things to do include cleaning up the code, debugging, and rewrite where necessary in order to get both the iris_response() and fit_iris_xput() functions to work without the code throwing errors during testing. This turned out to be relatively smooth-sailing (could be partly due to luck).

§1.2 Benchmarking

    Some use cases have been supplied by Dr. Dan Ryan (the primary mentor) which are originated from some IDL software the student has no access to. More details of such data will be given in the appendix.
    A test function has been written specifically to test fit_iris_xput() to allow us to test and understand the output. This incorporates the six use cases mentioned previously from IDL.
    Efforts have been coordinated to compare results from the IDL and IRISpy versions to verify they are giving the same answers. The tolerance has been set at 6 decimal places. It has been found that preliminary results from the crude Python code in iris_tools.py before code enhancement to be carried out at the next stage match the IDL ones quite well, which was very encouraging.
    Most of the time the fall-back tactics have been divide-and-conquer and trial-and-error.

§1.3 Bug-fixing

    The aim has been to render the first functional Python version of the code to give the same or effectively the same answers as the IDL version, except perhaps rounding errors.
    Most common type of bugs encountered arose from differences in syntax, especially from converting between programming languages from IDL to Python.
    One of the more glaring and easily omitted error encountered stemmed from erroneous indentation.
    The final bug to be fixed had to do with units used in the variable for time difference t_diff. This has to be presented in years. However, due to the way the packages were designed before and upgrade, some confusion cropped up as it has to be converted from a datetime.timedelta object in days to seconds first before it can be converted into the proper unit. After software upgrade, particularly sunpy, it became easier to perform the same task as the object is now an astropy.time.time one, so that by using astropy’s powerful units and quantities machinery, the conversion from days to years was direct and efficient.

§1.4 Improving Code Pythonically

    By this stage the code has been made more Pythonic as well as updated to reflect more recent changes in sunpy practices.
    Using astropy’s download_file function instead of Requests’ get to download the IRIS .geny files. This adds the cache and timeout functionalities to the download process.
    Converting the time_obs and time_cal_coeffs into astropy.time.time objects before subtracting to obtain a time difference called t_diff (to be converted into years), which is used to compute the final fit for the effective area(s).

§1.5 Plan for next stage: Incorporating Time-dependent Fitted Response into Wider IRISpy Code-base

    To include a call to fit_iris_xput() plus to add a time input for the _get_interpolated_effective_area() function.
    Add a docstring to the _get_interpolated_effective_area function.
    To include a time input and pass that on to _get_interpolated_effective_area() further up the chain. This chain includes iris_tools.calculate_photons_per_sec_to_radiance_factor(), iris_tools.convert_or_undo_photons_per_sec_to_radiance(), andIRISSpectrogramCube.convert_to(). Will confirm if there are more cases where this chain leads.
    To include cases where a fitted effective area is used in the tests of above functions.

Therefore, so far the project is on schedule… hopefully things will stay that way.
