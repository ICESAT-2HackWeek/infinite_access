# ICESat-2 Search, Access, Load Options

## Overview

Three broad steps are used in ICESat-2 workflows; _search_, _access_ and _loading_ or _reading_ the data.  There are also services and tools that allow transformation on
the server side.  

_Search_ - discover data granules for a given product, temporal range and spatial region
_Access_ - Either download granules to a local machine, or stream granule data
_Load_ - load data into a data object; e.g. xarray.Dataset, geopandas.GeoDataFrame
_Transform_ - Includes reformatting, "reprojection", subsetting by time, space and variable.

## List of Featured Tools

[`earthaccess`](https://github.com/nsidc/earthaccess): |_search_|, _access_, Search for, and download or stream NASA Earth science data with just a few lines of code  
[`geopandas`](https://geopandas.org/en/stable/): _analysis_,  GeoPandas extends the datatypes used by pandas to make working with geospatial data in python easier  
[`h5coro`](https://github.com/SlideRuleEarth/h5coro): _access_, _load_, A cloud optimized Python package for reading HDF5 data stored in S3  
[`h5py`](https://github.com/h5py/h5py): _load_, A thin, pythonic wrapper around HDF5, which runs on Python 3 (3.10+)  
[`harmony_py`](https://github.com/nasa/harmony-py): _transform_, _access_, A Python library for integrating with NASA's Harmony Services.  
[`icepyx`](https://github.com/icesat2py/icepyx): _search_, _access_, _transform_, Python tools for obtaining and working with ICESat-2 data.  
[`SlideRule`](https://github.com/SlideRuleEarth/sliderule): _search_, _access_, _transform_  
[`xarray`](): _load_, _analysis_  

[`pointCollection`](https://github.com/SmithB/pointCollection): _analysis_, Utilities for organizing and manipulating point data
[`pointAdvection`](https://github.com/tsutterley/pointAdvection): _analysis_, Utilities for advecting point data for use in a Lagrangian reference frame


## Matrix of tools

:name: data-search-and-access-overview-table

| | `icepyx` | `earthaccess` | Sliderule | `h5coro`[^1] | `harmony_py` |
|:--- |:---:|:---:|:---:|:---:|:---:|
| Filter Spatially using:                     |   |   |   |   |   |
|    Interactive map widget                   |   |   | x |   |   |
|    Bounding Box                             | x | x | x |   |   |
|    Polygon                                  | x | x | x |   |   |
|    GeoJSON or Shapefile                     | x |   | x |   |   |
| Filter by time and date                     | x | x | x |   |   |
| Filter by variable                          |   |   |   |   |   |
| Preview data                                | x | x |   |   |   |
| ~~Download data from DAAC~~[^2]             | ~~x~~ | ~~x~~ |   |   |   |
| Access cloud-hosted data                    | x | x | x |   |   |
| All ICESat-2 data                           | x | x |   |   |   |
| Subset:                                     |   |   |   |   |   |
|    Spatially                                | x |   | x |   |   |
|    Temporally                               | x |   | x |   |   |
|    By variable                              | x |   | x |   |   |
| Load data by direct-access                  | x | x | x |   |   |
| Process and analyze data                    |   |   | x |   |   |
| Plot data with built-in methods             | x |   | x |   |   |

## References

[^1]: [`h5coro`]() is a C library to access selected ICESat-2 products.  It also
  requires lower-level coding.
[^2]: All ICESat-2 data are now hosted on NASA Earthdata Cloud