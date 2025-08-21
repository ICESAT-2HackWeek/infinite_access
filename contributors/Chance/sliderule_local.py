#!/usr/bin/env python3

from sliderule import icesat2
import earthaccess as ea
import time
import sys
import numpy as np
from datetime import datetime
import os
from matplotlib import pyplot as plt
### One Granule
def get_size(gdf):
    return gdf.memory_usage(deep=True).sum() / (1024**2)

def print_result(test_tuple, speed, size):
    row = "{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}"
    t = test_tuple
    g = t[0]
    parallel= t[1]
    method = t[2]
    note = t[-1]
    size = str(np.round(size, 4))
    speed = str(np.round(speed, 2))
    line = row.format(g, parallel, method, speed, size, note)
    print(line)
    return


def main():
  granule_path = 'https://data.nsidc.earthdatacloud.nasa.gov/nsidc-cumulus-prod-protected/ATLAS/ATL06/006/2019/12/02/ATL06_20191202203649_10220511_006_01.h5'
  granule = os.path.basename(granule_path)

  dt = datetime.strptime(granule.split('_')[1][0:8], "%Y%m%d")
  dt_str = datetime.strftime(dt, "%Y-%m-%dT%H:%M:%SZ")

  ## output formatting

  header = "{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}"
  print(header.format("Granules", "Function", "Method", "Speed (s)", "Size (MB)", "Notes"))

  #### One granule, One beam, Subsetted
  parms_bbox = {
      "poly": [
      {
      "lon": 152.84367053387408,
      "lat": -81.2185940279265
      },
      {
      "lon": 157.30604049933277,
      "lat": -80.7324891420691
      },
      {
      "lon": 158.0479504202403,
      "lat": -80.55684138323734
      },
      {
      "lon": 157.09874213907918,
      "lat": -80.39247953410985
      },
      {
      "lon": 151.34894025204565,
      "lat": -80.9204126913049
      },
      {
      "lon": 152.84367053387408,
      "lat": -81.2185940279265
      }
      ],
      "beams": 'gt2l',
      "cycle": 5,
      }


  tic = time.time()
  D6 = icesat2.atl06sp(parm=parms_bbox)
  toc = time.time()
  test_tup = ('1', 'sp', 'bbox', 'gt2l')
  print_result(test_tuple=test_tup, speed=toc-tic, size=get_size(D6))


  ##### One Granule, One beam, No subsetting
  tic = time.time()
  D6 = icesat2.atl06sp(parm={
    "beams": 'gt2l',
    }, 
    resources=['ATL06_20191202203649_10220511_006_01.h5'])
  toc = time.time()
  test_tup = ('1', 'sp', 'granule', 'gt2l')
  print_result(test_tuple=test_tup, speed=toc-tic, size=get_size(D6))


  ### 9 granules
  # bigger bounding box (greenland) (don use these thos)


  parms_bbox= {
    "poly" : [
      {"lon": -45.4, "lat": 62.63},    # lower left
      {"lon": -44.6, "lat": 62.63},    # lower right
      {"lon": -44.6, "lat": 63.0},     # upper right
      {"lon": -45.4, "lat": 63.0},     # upper left
      {"lon": -45.4, "lat": 62.63}     # close polygon
    ],
    "cycle": 25,
  }


  results = ea.search_data(
      short_name='ATL06',
      cloud_hosted=True,
      bounding_box=(-45.4, 62.63, -44.6, 63.0),   
      granule_name="ATL06_*_????25??_*_*.h5",
  )
  granules = [os.path.basename(g.data_links()[0]) for g in results]

  #### 9 Granules, Subsetted
  ## 

  tic = time.time()
  D6_bbox = icesat2.atl06sp(parm=parms_bbox, resources=granules)
  toc = time.time()
  test_tup = ('9', 'sp', 'bbox', 'cycle 25')
  print_result(test_tuple=test_tup, speed=toc-tic, size=get_size(D6_bbox))

  #### 9 Granules, No subsetting, resources
  tic = time.time()
  D6 = icesat2.atl06sp(parm={}, resources=granules)
  toc = time.time()
  test_tup = ('9', 'sp', 'granules', 'cycle 25')
  print_result(test_tuple=test_tup, speed=toc-tic, size=get_size(D6))

  #### 9 granules, no subsetting
  tic = time.time()
  D6_resources_bbox = icesat2.atl06sp(parm=parms_bbox, resources=granules)
  toc = time.time()
  test_tup = ('9', 'sp', 'gran/bbox', 'cycle 25')
  print_result(test_tuple=test_tup, speed=toc-tic, size=get_size(D6_resources_bbox))


  tic = time.time()
  D6_bbox = icesat2.atl06sp(parm=parms_bbox)
  toc = time.time()
  test_tup = ('9', 'sp', 'bbox', 'cycle 25')
  print_result(test_tuple=test_tup, speed=toc-tic, size=get_size(D6_bbox))

  return

if __name__=="__main__":
    main()