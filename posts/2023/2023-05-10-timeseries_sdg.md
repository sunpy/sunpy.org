```{post} May 10 2023
:author: David Stansby

```

# The future of time series data in `sunpy`

In late 2022 I got a [small development grant](https://numfocus.org/programs/small-development-grants) from [NumFocus](https://numfocus.org/) to scope the future of time series data in `sunpy`.
The successful application [can be read on the sunpy wiki](https://github.com/sunpy/sunpy/wiki/2022-Timeseries-Small-Development-Grant).
The application contains context that I won't repeat here.
This blog post is the key outcome of this grant, with a record of what I did, the recommendations I made, and any decisions we came to as a community.

## User requirements
The first stage of my work investigated what the user requirements are for a sunpy data container for time series data. As part of this I used my own experience and the following community engagement:
- Discussion at one of the weekly sunpy community meetings in December 2022
- [Discussion on the Python in Heliophysics mailing list](https://groups.google.com/g/pyhc-list/c/ujnZEZcsI_k/m/gNfYrIJdBgAJ)
- [Discussion on the SunPy forum](https://community.openastronomy.org/t/choosing-a-future-data-container-for-timeseries-data/556?u=dstansby)

From these discsusions came the following list of requirements:

| Requirement | Notes |
| ----------- | ----- |
| Store data that is a function of time | This means the time column should be treated as the index or coordinates to the data, and be stored as a time-like type. |
| Handle different time scales | Data can have times defined in a variety of different time scales (e.g. UTC, TAI) |
| Store multi-dimensional data | Although time is a common index to timeseries data, it isn't always the only one. As an example, velocity distribution functions measured in the solar wind are 4D datasets, with data as a function of time and three dimensions in velocity space. |
| Handle time scales with leapseconds | Some timescales can contain timestamps that occur within a leapsecond.  |
| Store and use physical units with the data and any non-time indices | |
| Store data in a format that can be used with scientific Python libraries | |
| Support for storing out-of memory datasets | |
| Store metadata alongside actual data | |
| Have a way to store an observer coordinate alongside the time index | |
| Have an easy way to do common data manipulation tasks | e.g. interpolating, resampling, rebinning |
| Have a way to combine multiple timeseries objects, and keep track of metadata | |
| Ability to convert to other common time series objects (e.g. `pandas.DataFrame`) | |
| Functionality for loading and saving out to common file formats | |

## Existing options for a data container
The next step was to identify a set of possible data containers that could be used to store time- series data in sunpy.
The identified options were:

- `astropy.timeseries.TimeSeries`
- `pandas.DataFrame`
- `xarray.DataArray` (or `xarray.DataSet`)
- `numpy.ndarray`
- `ndcube`

### What do other projects use?
I also looked at what [Python in Heliophysics projects](https://heliopython.org/projects/) use (as of writing, in Jan 2023):

| Package | Container |
| ------- | --------- |
| [sunpy](https://github.com/sunpy/sunpy/) | Custom `TimeSeries` object, backed by `pandas.DataFrame` |
| [HAPI Client](https://github.com/hapi-server/client-python) | `numpy.ndarray` |
| [pySPEDAS](https://github.com/spedas/pyspedas) | Not clear if users can access the data itself |
| [spacepy](https://github.com/spacepy/spacepy) | Unclear if there is any specific timeseries container object |
| [aidapy](https://gitlab.com/aidaspace/aidapy) | `xarray.DataArray`|
| [cdflib](https://github.com/MAVENSDC/cdflib) | `numpy.ndarray` |
| [NDCube](https://github.com/sunpy/ndcube) | `NDCube` |
| [pytplot](https://github.com/MAVENSDC/pytplot) | `xarray.DataArray` |
| [solo-epd-loader](https://github.com/jgieseler/solo-epd-loader) | `pandas.DataFrame` |
| [speasy](https://github.com/SciQLop/speasy) | Custom `DataContainer` object, backed by `numpy.ndarray` |

There is no common container used, with only `astropy.TimeSeries` not represented out of the possible options above.

### What datasets does sunpy currently support?
sunpy currently has built in support for reading CDF files that conform to the [Space Physics Guidelines for CDF](https://spdf.gsfc.nasa.gov/sp_use_of_cdf.html), as long as the dataset is one- or two- dimensional.
Alongside this several custom data readers have been written to support different data sources:

(links point to the data source information web page)
| Data product(s) | File format |
| -- | -- |
| [SDO EVE/ESP L1](https://lasp.colorado.edu/eve/data_access/eve_data/products/level1/esp/2020/) | FITS | |
| [SDO EVE/ESP L0CS](https://lasp.colorado.edu/home/eve/data/) | Text file |
| [FERMI GBM summary](https://fermi.gsfc.nasa.gov/ssc/data/access/ ) | FITS |
| GOES XRS | FITS, netCDF |
| PROBA-2 LYRA ligthcurve | FITS |
| [NOAA solar cycle monthly indices](https://www.swpc.noaa.gov/products/solar-cycle-progression) | JSON |
| [NOAA solar cycle predicted indices](https://www.swpc.noaa.gov/products/solar-cycle-progression) | JSON |
| [NoRH radio](https://solar.nro.nao.ac.jp/norh/archive.html) | FITS |
| RHESSI x-ray summary | FITS |

## Evaluating options
Having found possible options, in this section I've evaluated them against the criteria set out above.

### `numpy.ndarray`
| | | |
| -- | -- | -- |
| Time-like index data | 🛑 | Can store datetime64 data, but no support for indexes|
| Different time scales | 🛑 | No support |
| Multi-dimensional data | 🟩 | |
| Physical units | 🛑  | No support |
| Interop with scientific Python | 🟩  | |
| Out of memory | 🛑 | numpy arrays are always in memory |
| Metadata | 🛑 | No support  |
| Observer coordinates |  🛑  |No support |
| Easy data manipulation | 🟩 | |
| I/O | 🟠| Can save to binary .npy format or text file |

### `pandas.DataFrame`
| | | |
| -- | -- | -- |
| Time-like index data | 🟩 | |
| Different time scales | 🛑 | No support |
| Multi-dimensional data | 🟠 | Possible, but [recommended to use xarray instead](https://pandas.pydata.org/docs/getting_started/install.html#computation) |
| Physical units | 🛑  | No native support ([tracking issue](https://github.com/pandas-dev/pandas/issues/10349)), could be possible with [`pint-pands`](https://github.com/hgrecco/pint-pandas) |
| Interop with scientific Python | 🟩  | |
| Out of memory | 🛑 | pandas DataFrames are always in memory |
| Metadata | 🟩  | Possible to [add additional properties](https://pandas.pydata.org/pandas-docs/stable/development/extending.html#define-original-properties) to a DataFrame  |
| Observer coordinates | 🛑 | No support |
| Easy data manipulation | 🟩 | Many built in methods for manipulating time-like data |
| I/O | 🟩  | [Lots of I/O options](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html) |

### `xarray.DataArray`
| | | |
| -- | -- | -- |
| Time-like index data | 🟩 | |
| Different time scales | 🛑 | No support |
| Multi-dimensional data | 🟩 |  |
| Physical units | 🛑  | No native support ([tracking issue](https://github.com/pydata/xarray/issues/525)), could be possible with [`pint-xarray`](https://pint-xarray.readthedocs.io/en/stable/) |
| Interop with scientific Python | 🟩  | |
| Out of memory | 🟩 | Support for [computing using `dask`](https://docs.xarray.dev/en/stable/user-guide/dask.html) |
| Metadata | 🟩  | Possible to [add metadata](https://docs.xarray.dev/en/stable/getting-started-guide/faq.html#what-is-your-approach-to-metadata) to a DataArray  |
| Observer coordinates | 🟠 | Support for adding ["non-dimensional" coordinates](https://docs.xarray.dev/en/stable/user-guide/data-structures.html#coordinates) (e.g. longitude/latitude), but not clear if storing astropy SkyCoord would work |
| Easy data manipulation | 🟩 | Many built in methods for manipulating time-like data |
| I/O | 🟩  | [Lots of I/O options](https://docs.xarray.dev/en/stable/user-guide/io.html) |

### `astropy.timeseries.TimeSeries`
| | | |
| -- | -- | -- |
| Time-like index data | 🟩 | |
| Different time scales | 🟩 | |
| Multi-dimensional data | 🛑 | |
| Physical units | 🟩 | |
| Interop with scientific Python | 🟩 | |
| Out of memory | 🟠 | Apparently there is some support, but this is undocumented. |
| Metadata | 🟩  | Can store on the `.meta` attribute  |
| Observer coordinates | 🟩 |  |
| Easy data manipulation | 🟠 | |
| I/O | 🟩 | I/O is done via `astropy.table.Table` |

### `NDCube`
| | | |
| -- | -- | -- |
| Time-like index data | 🟩 | |
| Different time scales | 🟩 | |
| Multi-dimensional data | 🟩 | |
| Physical units | 🟩 |  |
| Interop with scientific Python | 🟩 | |
| Out of memory | 🟠 | Seems to be supported in theory, but little docs  |
| Metadata | 🟩  | Can store arbitrary FITS metadata |
| Observer coordinates | 🛑 | No support for extra coordinates |
| Easy data manipulation | 🛑 | Very few manipulation methods implemented |
| I/O | 🛑 | |


## Initial recommendations
- `numpy.ndarray` doesn't implement several key features, and these are almost certainly out of scope for future `ndarray` development, so I suggest `ndarray` is discounted.
- `xarray.DataArray` builds on top of `pandas.DataFrame` with additional features that would be useful to us, I suggest `pandas.DataFrame` is discounted.
- `NDCube` is designed specifically to store data that is associated with a FITS world coordinate system (WCS). While some solar timeseries data is already in the FITS format, a large portion is in CDF format which is tabular, which FITS is not primarily designed to represent. So I suggest `NDCube` is discounted.

At a SunPy community meeting there was a consensus agreement that going forward we should consider `astropy.TimeSeries` and `xarray.DataArray` as the two options to consider.

These two options have the following comparison:

| | `astropy.TimeSeries` | `xarray.DataArray`|
| -- | -- | -- |
| Time-like index data | 🟩 | 🟩 |
| Different time scales | 🟩 | 🛑 |
| Multi-dimensional data | 🛑 | 🟩 |
| Physical units | 🟩 | 🛑 |
| Interop with scientific Python | 🟩 | 🟩 |
| Out of memory | 🟠  | 🟩 |
| Metadata | 🟩  | 🟩  |
| Observer coordinates | 🟩 | 🟠 |
| Easy data manipulation | 🟠 | 🟩 |
| I/O | 🟩 | 🟩 |

My initial recommendation would be to adopt `xarray.DataArray`, as the two red items have a strong possibility of being solved with `DataArray`:

- It *should* (I haven't confirmed this) be possible to convert times in different time scales (including ones with leap seconds) to a single timescale that doesn't have leap seconds, and store this in an `xarray.DataArray`.
- Although there is not native support for units in `DataArray` currently, there is interest and ongoing development to support them.

It is unclear to me (because I did not have time to investigate) how hard it would be to implement support for storing rich coordinates (ie. `astropy.SkyCoord`) in the extra_coords part of xarray data structures.

In contrast I think implementing multi-dimensional data in `astropy.TimeSeries`, adding documentation for out of memory datasets, and implementing easy data manipulation methods would take significantly more effor than this.
Finally, `xarray` has a much bigger development community than `astropy.TimeSeries`, so implementing bug fixes and new features would probably be much easier with `xarray`.

## Putting `astropy` objects in `xarray` structures

For the final part of the small development grant, I investigated the changes needed to put `astropy` objects in `xarray` structures.

As a model for doing this, it is currently possible to store unitful data created with `pint` in `xarray` structures.
Support for doing this has two components:
- `xarray` [natively supports storing duck arrays](https://docs.xarray.dev/en/stable/internals/duck-arrays-integration.html)
- `xarray-pint` provides a set of accessors that can be used to serialise and deserialise unitful data so that it can be saved to a file and loaded again.
  It does this by converting the unit data into metadata, with strings representing units.

It is not currently possible to store `astropy.Quantity` objects in `xarray` structures, as they inherit directly from `ndarray`, and get coerced from `Quantity` to `ndarray` during the `xarray` structure initialisation. I think fixing this is (at least initially) a one line change, changing (what was xarray/core/variable.py#L288 on commit hash 51554f2638bc9e4a527492136fe6f54584ffa75d) from
```python
data = np.asarray(data)
```
to
```python
if not isinstance(data, np.array):
    data = np.asarray(data)
```

Before moving forward with this it needs to be possible to run the full unit tests in xarray with `astropy.Quantity`.
I started work on this in these two PRs:
- [https://github.com/pydata/xarray/pull/7799](https://github.com/pydata/xarray/pull/7799)
- [https://github.com/pydata/xarray/pull/7800](https://github.com/pydata/xarray/pull/7800)
