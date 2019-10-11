import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np


class crimemap:
    def __init__(self, map_dir):
        self.shapefile0 = gpd.read_file(map_dir)
        self.shapefile0.plot(figsize=(10, 10))

    def mapshow(self, x_min=-73.59, x_max=-73.55, y_min=45.49, y_max=45.53, grid_size=0.002):
        self.extent = [x_min, x_max, y_min, y_max]
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        self.x_sticks = np.arange(x_min, x_max + grid_size/2, grid_size)
        self.y_sticks = np.arange(y_min, y_max + grid_size/2, grid_size)
        plt.xticks(self.x_sticks)
        plt.yticks(self.y_sticks)
        plt.grid()
        plt.show()

    def crime_calc(self, threshold=0.5):
        series_x = self.shapefile0.geometry.x
        series_y = self.shapefile0.geometry.y
        crime_hist, _, _ = np.histogram2d(series_y, series_x, bins=[self.y_sticks, self.x_sticks])
        crime_array = crime_hist.flatten()
        threshold_value = np.percentile(crime_array, threshold*100)
        crime_hist_cp = np.copy(crime_hist)
        crime_hist_cp[crime_hist_cp <= threshold_value] = 0
        crime_hist_cp[crime_hist_cp > threshold_value] = 1
        mean_ = np.mean(crime_hist)
        std_dev_ = np.std(crime_hist)
        print("Mean: {0:.4f}".format(mean_))
        print("Standard deviation: {0:.4f}".format(std_dev_))
        print("Threshold value: {0:.4f}".format(threshold_value))
        plt.imshow(crime_hist_cp, origin='lower', extent=self.extent, interpolation='nearest', aspect='auto')
        plt.show()