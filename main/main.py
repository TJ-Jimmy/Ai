from crimemap import crimemap
import os
# matplotlib inline
grid_size = 0.002
threshold = 0.89
cur_dir = os.getcwd()
map_dir = os.path.abspath(os.path.dirname(cur_dir)) + r"\map\crime_dt.shp"

crime_map = crimemap(map_dir)
crime_map.mapshow(grid_size=grid_size)
crime_map.crime_calc(threshold=threshold)