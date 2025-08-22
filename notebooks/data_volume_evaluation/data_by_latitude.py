"""Helper functions for data_by_latitude"""
from shapely.geometry import Polygon, box

from pyproj import CRS, Transformer
from affine import Affine
import numpy as np

class GridCell():

    def __init__(self, x0, y0, width, height, crs=None):
        """Create GridCell Object as shapely.geometry.box"""
        self.crs = crs
        self.geometry = box(x0, y0, x0+width, y0+width)

    @property
    def region(self):
        return [{"lon": lo, "lat": la} for lo, la in self.xy]

    def to_crs(self, crs, from_crs=None):
        """Return transformed points"""
        if (not self.crs) & (not from_crs):
            raise ValueError("Expects either self.crs or from_crs to be set, both are None")

        if self.crs:
            from_crs = self.crs

        xy = transformer(from_crs, crs).transform(*self.geometry.exterior.xy)
        self.crs = crs
        self.geometry = Polygon([(xp, yp) for xp, yp in zip(*xy)])
        return 

    @property
    def xy(self):
        """Returns vertices of grid cell"""
        return [(x, y) for x, y in zip(*self.geometry.exterior.xy)]
        
    
def transformer(from_crs, to_crs):
    """Returns instatiated pyproj.Transformer"""
    return Transformer.from_crs(
        CRS.from_user_input(from_crs), 
        CRS.from_user_input(to_crs)
    )

def get_global_grid_size(ellipsoid, nominal_cell_size=1.):
    """Returns exact width and height for a nominal cell size"""
    scale = {
        1: 40000.,
        10: 4000.,
        100: 400.,
    }
    length_of_equator = (2 * ellipsoid.semi_major_metre * np.pi)
    dx = dy = length_of_equator / scale[nominal_cell_size]
    return dx, dy


class Grid():

    def __init__(self, name, width, height, x0, y0, nx, ny, crs):
        self.name = name
        self.width = width
        self.height = height
        self.x0 = x0
        self.y0 = y0
        self.nx = nx
        self.ny = ny
        self.crs = CRS.from_user_input(crs)
        self.transform = Affine.from_gdal(*(x0, width, 0., y0, 0.0, height))

    def get_coords(self):
        x, _ = self.transform * (np.arange(self.nx), 0)

    def get_grid_cell_bounds(r, c):
        pass

    @property
    def grid_bounds(self):
        """Returns the bounds of the grid
        (xmin, ymin, xmax, ymax)
        """
        xmin, ymax = self.transform * (0,0)
        xmax, ymin = self.transform * (self.nx, self.ny)
        return (xmin, ymin, xmax, ymax)


# EASEGridGlobal1km = Grid(
#     "EASEGridGlobal1km", 
#     10018.754171394621, 
#     -10018.754171394621, 
#     -20037508.342789244,
#     7341101.823941151,
#     4000,
#     732,
#     6933
# )

# EASEGridGlobal10km = Grid(
#     "EASEGridGlobal10km", 
#     100187.54171394621, 
#     -100187.54171394621, 
#     -20037508.342789244,
#     7341101.823941151,
#     4000,
#     730,
#     6933
# )

EASEGridGlobal100km = Grid(
    "EASEGridGlobal100km", 
    100390.34939399637, 
    -100390.34939399637, 
    -17367530.445161372,
    7228105.156367739,
    346,
    146,
    6933
)

