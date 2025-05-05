import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter  # for smoothing

# === File paths ===

#you need to choose a background for the map that is an image of the city map
city_map_path = 'city_map_2.png'
#this file contains the coordinates of your data
data_path = 'skydata_real_coordinates.txt'
#this file contains the equivalent exposure time of the images you captured
values_path = 'sky_data_real_eet_data.txt'

# === Load city map ===
city_img = Image.open(city_map_path)

# === Load pollution data ===
#uploading data from the text files
data = np.loadtxt(data_path)
lats = data[:, 0]
lons = data[:, 1]
values = np.loadtxt(values_path)

# === Define geographic extent of the map ===
#you need to know the coordinates of your background map's border
#           left      right     bottom    top
extent = (21.16292, 21.29054, 45.71217, 45.78172)

# === High-resolution interpolation grid ===
#creates a grid for your map to be able to visualize data
grid_lon = np.linspace(extent[0], extent[1], 600)
grid_lat = np.linspace(extent[2], extent[3], 600)
grid_x, grid_y = np.meshgrid(grid_lon, grid_lat)

# === Interpolate using 'linear' method ===
#interpolating data to fill in empty spaces on map
#linear interpolation creates a gradient between 2 data values
grid_values = griddata((lons, lats), values, (grid_x, grid_y), method='linear')

# === Apply Gaussian smoothing ===
#a blur is applied on the overlay map to smooth out data and make the map visually pleasing (it doesn't affect data)
grid_values = gaussian_filter(grid_values, sigma=2)

# === Plotting ===
fig, ax = plt.subplots(figsize=(10, 10))

#background city map
ax.imshow(city_img, extent=extent, alpha=1)

# Heatmap overlay
heatmap = ax.imshow(grid_values, extent=extent, origin='lower',
                    cmap='hot', alpha=0.5)

#colorbar
cbar = plt.colorbar(heatmap, ax=ax, label='Fényszennyés (EEI)')
cbar.ax.tick_params(labelrotation=90)

plt.savefig('light_pollution_heatmap_good_edges_all2.png', dpi=1500)
plt.show()