## Data Access Considerations
The best way to access ICESat-2 data depends on your desired use case. Below, we outline some considerations and recommended data access pathways. 

**Data Product** Select an ICESat-2 [data product](https://icesat-2.gsfc.nasa.gov/science/data-products) that aligns with your goals. We recommend starting from a higher level data product and working down if necessary.

**Data Volume** Select a *local download* computing environment if you have enough memory to store and proccess the data you or using; otherwise select a *cloud streaming* environment.

**Access Method** All access methods support programmatic access, but some also provide *GUIs*. We recommend using a GUI only for testing small amounts of data and programatically accessing data in your workflows.

**Data Use Case** Choose if you require *subsetting* (choosing specific regions or variables to download) or *interoperability* by downloading additional data from different sources using the same access method.

|Access Consideration   	|[SlideRule](https://slideruleearth.io/web/rtd/) 	|[Earthaccess](https://earthaccess.readthedocs.io/en/stable/)   	|[icepyx](https://icepyx.readthedocs.io/en/latest/)   	|
|---	|---	|---	|---	|
|Data Product <br> *Which ICESat-2 data product do you want?*   	|ATL3, 6, 8, 13, and 24 only   	|Any product available at [NASA Earthdata](https://www.earthdata.nasa.gov/)  	|Any product available at the [NSIDC](https://nsidc.org/data/icesat-2/data)|
|Cloud Streaming <br> *You need compute beyond your local machine*  	|:heavy_check_mark: 	|:heavy_check_mark:[^1]   	|:large_orange_diamond:   	|
|Local Download <br> *You have enough memory to store and process data locally*   	|:x:|:heavy_check_mark:   	|:heavy_check_mark:   	|
|GUI    	|[SlideRule Web Client](https://client.slideruleearth.io/)   	|[NASA Earthdata Search](https://search.earthdata.nasa.gov/) 	|   	|
|Subsetting   	|Spatial, Temporal, Variables   	|Spatial, Temporal  	|Spatial, Temporal   	|
|Interoperability   	|GEDI   	|Any product available at [NASA Earthdata](https://www.earthdata.nasa.gov/)    	|   	|
   
[^1]: Using xarray's `h5coro` backend is much faster than the default `h5py` backend for opening ICESat-2 granules. We recommend the following workflow when using Earthaccess in the cloud. Note this requires h5coro>=0.0.8.
    ```python
    import earthaccess
    import xarray as xr
    
    auth = earthaccess.login()
    creds = auth.get_s3_credentials(daac='NSIDC')
    results = earthaccess.search_data(short_name=<short_name>, granule_name=<granule_name>)
    url = results[0].data_links(access="direct")[0][3:] # Remove 's3:' from the beginning of the url
    ds = xr.open_dataset(url, engine='h5coro', group=<group>, credentials=creds)
    ```

## Reccommendations and Future Work
[ ] Ensure `earthaccess` has sufficient documentation
[ ] Create documentation for `h5coro`
[ ] Create issue in `xarray` to automatically remove `s3:` from url passed to open_dataset
