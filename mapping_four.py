import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter  # for smoothing

# === File paths ===
city_map_path = 'city_map_2.png'
data_path = 'skydata_real_coordinates.txt'
values_path = 'sky_data_real_eet_data.txt'

# === Load city map ===
city_img = Image.open(city_map_path)

# === Load pollution data ===
data = np.loadtxt(data_path)
lats = data[:, 0]
lons = data[:, 1]
values = np.loadtxt(values_path)

# === Define geographic extent of the map ===
extent = (21.16292, 21.29054, 45.71217, 45.78172)

# === High-resolution interpolation grid ===
grid_lon = np.linspace(extent[0], extent[1], 600)  # higher resolution
grid_lat = np.linspace(extent[2], extent[3], 600)
grid_x, grid_y = np.meshgrid(grid_lon, grid_lat)

# === Interpolate using 'linear' method ===
grid_values = griddata((lons, lats), values, (grid_x, grid_y), method='linear')

# === Apply Gaussian smoothing ===
grid_values = gaussian_filter(grid_values, sigma=2)  # smooth the result

# === Plotting ===
fig, ax = plt.subplots(figsize=(10, 10))

# Background city map
ax.imshow(city_img, extent=extent, alpha=1)

# Heatmap overlay
heatmap = ax.imshow(grid_values, extent=extent, origin='lower',
                    cmap='hot', alpha=0.5)

# Colorbar
cbar = plt.colorbar(heatmap, ax=ax, label='Fényszennyés (EEI)')
cbar.ax.tick_params(labelrotation=90)
plt.savefig('light_pollution_heatmap_good_edges_all1.png', dpi=1200)
plt.show()