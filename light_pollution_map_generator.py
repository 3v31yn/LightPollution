import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter
import matplotlib.ticker as ticker


def save_pollution_map(img, lons, lats, values, extent, title, filename):
    fig, ax = plt.subplots(figsize=(12, 10))
    grid_lon = np.linspace(extent[0], extent[1], 800)
    grid_lat = np.linspace(extent[2], extent[3], 800)
    grid_x, grid_y = np.meshgrid(grid_lon, grid_lat)
    grid_values = griddata((lons, lats), values, (grid_x, grid_y), method='linear')
    grid_values_smoothed = gaussian_filter(grid_values, sigma=5)
    ax.imshow(img, extent=extent, alpha=1)


    heatmap = ax.imshow(grid_values_smoothed, extent=extent, origin='lower',
                        cmap='magma', alpha=0.5)
    ax.set_title(title, fontsize=16, pad=20)

    cbar = fig.colorbar(heatmap, ax=ax, orientation='vertical', shrink=0.8, pad=0.03)
    cbar.set_label('Megvilágítás (lux)', rotation=90, labelpad=15)
    v_min = np.nanmin(grid_values_smoothed)
    v_max = np.nanmax(grid_values_smoothed)
    tick_values = np.linspace(v_min, v_max, 10)
    cbar.set_ticks(tick_values)
    cbar.ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))

    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Successfully saved: {filename}")
    plt.close(fig)


city_map_path = 'city_map.png'
data_path = 'late_night_coordinates_data.txt'
values_path = 'late_night_lux_data.txt'
extent = (21.142808242, 21.314133693, 45.697748109, 45.803073185)

plt.style.use('default')

try:
    city_img = Image.open(city_map_path)
    data = np.loadtxt(data_path)
    values = np.loadtxt(values_path)
except Exception as e:
    print(f"Error: {e}")
    exit()


lats_odd, lons_odd = data[::2, 0], data[::2, 1]
vals_odd = values[::2]
lats_even, lons_even = data[1::2, 0], data[1::2, 1]
vals_even = values[1::2]


save_pollution_map(city_img, lons_odd, lats_odd, vals_odd, extent,
                   "Késő esti fényszennyezési térkép zenit szerint", "late_zenit_map_magma.png")
save_pollution_map(city_img, lons_even, lats_even, vals_even, extent,
                   "Késő esti fényszennyezési térkép Polaris szerint", "late_polaris_map_magma.png")