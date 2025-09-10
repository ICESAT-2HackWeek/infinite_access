import h5py
import os
from tqdm import tqdm
import pickle

point_sizes = {}

def download_data(cycle, datapath):
    for f in tqdm(os.listdir(os.path.join(datapath, cycle))):
        try:
            with h5py.File(os.path.join(datapath, cycle, f), 'r') as hdf:
                for group in list(hdf.keys())[:-1]:
                    if group not in point_sizes:
                        point_sizes[group] = hdf[group + '/' + list(hdf[group].keys())[0]].size
                    else:
                        point_sizes[group] += hdf[group + '/' + list(hdf[group].keys())[0]].size
        except:
            print("Could not open h5 file: ", str(os.path.join(datapath, cycle, f)))
                
    return point_sizes

##### Antarctic Data #####
ant_datapath = '/Volumes/ice1/ben/ATL06/tiles/Antarctic/006/'
ant_icesat2dir = os.listdir(ant_datapath)

for cycle in os.listdir(ant_datapath):
    try:
        points = download_data(cycle, ant_datapath)
    except:
        print("Something went wrong in Antarctic " + str(cycle) + " during data download.")
    try:
        with open("./" + str(cycle)+'antarctic.pickle', 'wb') as handle:
            pickle.dump(points, handle, protocol=pickle.HIGHEST_PROTOCOL)
    except:
        print("Something went wrong in Antarctic " + str(cycle) + " during data saving.")

##### Arctic data #####
arc_datapath = '/Volumes/ice1/ben/ATL06/tiles/Arctic/006/'
arc_icesat2dir = os.listdir(arc_datapath)

for cycle in os.listdir(arc_datapath):
    try:
        points = download_data(cycle, arc_datapath)
    except:
        print("Something went wrong in Arctic " + str(cycle) + " during data download.")
    try:
        with open("./" + str(cycle)+'arctic.pickle', 'wb') as handle:
            pickle.dump(points, handle, protocol=pickle.HIGHEST_PROTOCOL)
    except:
        print("Something went wrong in Arctic " + str(cycle) + " during data saving.")