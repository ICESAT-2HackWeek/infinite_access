# Speed Timing Results

## Overview

This notebook provides a summary of a set of fast speed timing results from reading ATL06 data from a variety of python tools locally and in the cloud. For a file of this size (120 MB; ~5 MB of data read) accessing the data directly with h5py was the fastest streaming method.

## Methods

5 different patterns for accessing ATL06 Icesat-2 data were tested on Cryocloud (AWS us-west-2 based Jupyter Hub) an locally. One beam of data (`gt2l`) and four variables (`delta_time`, `latitude`, `longitude`, and `h_li`) were read. Times shown are the mean time of 5 independent reads. No times were dropped, so any cold time that may be present is included in the average.

Local data was read on different computer architectures. Network speed ranged dramatically from 200-400 Mbps speed (download and upload).

"Read time" is defined as the time it takes to go from a url to bytes of ATL06 data. Query times were not included (except where otherwise noted). Time to create the file opener was included. All data was loaded into memory before the read was completed (ex. using `DataArray.load()` for xarray).

The file chosen was a 120 MB file over the Byrd glacier of Antarctica. It was captured on December 2nd, 2019.

| | |
| --- | --- |
| Granule ID | `ATL06_20191202203649_10220511_006_01.h5` |
| s3 url | `s3://nsidc-cumulus-prod-protected/ATLAS/ATL06/006/2019/12/02/ATL06_20191202203649_10220511_006_01.h5` |
| https url | `https://data.nsidc.earthdatacloud.nasa.gov/nsidc-cumulus-prod-protected/ATLAS/ATL06/006/2019/12/02/ATL06_20191202203649_10220511_006_01.h5` |


When evoking fsspec directly the paramters below were always used in the fsspec open() method. Past work has shown these parameters to significantly improve read times. ([Lopez](https://nsidc.github.io/cloud-optimized-icesat2/), [this gist](https://gist.github.com/rwegener2/ffbea2c4903f1528dbc5541f3f96e238))
```
{
  "cache_type": "blockcache", 
  "block_size": 8*1024*1024
  }
```

The high level effects of these parameters is:
- cache_type (fsspec): Download and cache data chunks from the file for caching (not, for example, the whole file)
- block_size (fsspec): How much data to request at once for buffering

The following versions of the libraries were used:
| Library | Version |
| --- | --- |
| SlideRule  | 4.18.1 |
| `icepyx` | 2.0.0 |
| `h5coro` (cloud)| 0.8.0 |
| `h5coro` (local) | 1.0.0 |
| `h5py` (cloud) | 3.13.0 |
| `h5py` (local) | 3.12.1 |
| `earthaccess` (local) | 0.14.0 |
| `earthaccess` (cloud) | 0.10.0 |

The code used for all the timing runs can be found in the notebooks/speed_timing folder of this repository.

## Results


| Access Pattern | Cloud (streaming) | Local (streaming) | Local (Download) |
|--- | --- | --- | --- |
| SlideRule | 2.1s | 2.3s | not tested |
| `icepyx` | >2 minutes | x[^1] | not tested |
| `h5py` + `fsspec` | 780 ms +/ 20ms (3.2 MB) | 6.1s (3.2 MB) | 5.1s[^3] |
| `h5py` + `xarray` + `fsspec` | 1.0s +/ 10ms | 7.2s (5.1 MB) | 5.1s[^3] |
| `h5coro` + `xarray` | 1.4s +/ 300ms | 15s +/ 3s (4.6 MB) | 5.1s[^3] |
| `earthaccess` + `xarray` (`h5py`)[^2] | 21s | | 1.25s[^4] |
| `earthacces` + `xarray` (`h5coro`)[^2] | 2.5s +/ 560ms | | 1.25s[^4] |

[^1]: icepyx has recently undergone a major version release. Bugs were found in icepyx as part of this process, but issues have been submitted.

[^2]: earthaccess times include the time to query, return the file opener, and open the data.

[^3]: the time to download the entire file. File was downloaded using the requests library and saved as an hdf file.

[^4]: download time is the time to directly download the data from earthaccess using `.download()` and open the file into xarray

