# ICESat-2 Search, Access, Load Options

## Overview

Three broad steps are used in ICESat-2 workflows; _search_, _access_ and _loading_ or _reading_ the data.  There are also services and tools that allow transformation on
the server side.  

_Search_ - discover data granules for a given product, temporal range and spatial region
_Access_ - Either download granules to a local machine, or stream granule data
_Load_ - load data into a data object; e.g. xarray.Dataset, geopandas.GeoDataFrame
_Transform_ - Includes reformatting, "reprojection", subsetting by time, space and variable.

## List of Featured Tools

[`earthaccess`](): _search_, _access_
[`geopandas`](): _analysis_
[`h5coro`](): _access_, _load_
[`h5py`](): _load_
[`harmony_py`](): _transform_, _access_
[`icepyx`](): _search_, _access_, _transform_
[`SlideRule`](): _search_, _access_, _transform_
[`xarray`](): _load_, _analysis_

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