#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from matplotlib.colors import LinearSegmentedColormap

import gmplot



#----Process Data ---


data_file = open('/home/map_data/map_data.csv')
lats, lons = [], []
for index, line in enumerate(data_file.readlines()):
        lats.append(float(line.split(',')[0]))
        lons.append(float(line.split(',')[1]))



#----Build Map ---


fig, ax = plt.subplots(figsize=(20,30)) #map size 

m = Basemap(resolution='f', # c, l, i, h, f or None
            projection='merc',
            lat_0=40.1, lon_0=-74.7, #center of map
            llcrnrlon=-76.0913, llcrnrlat= 38.7498, urcrnrlon=-73.0701, urcrnrlat=41.660) #map boundries


#add geo content to map
m.drawcounties(linewidth=0.3, linestyle='solid',antialiased=1, facecolor='none', ax=None, zorder=None, drawbounds=True)
m.drawcoastlines()
m.drawrivers()
m.drawmapboundary()

#overlay type 
#m.shadedrelief() 
#m.bluemarble()
#m.etopo()


x,y = m(lons, lats)
m.plot(x, y, 'ro', markersize=3,zorder=7,markerfacecolor='red',markeredgecolor="none", alpha=0.1)





# declare the center of the map, and how much we want the map zoomed in
gmap = gmplot.GoogleMapPlotter(40.1, -74.7, 8)
# plot heatmap
gmap.heatmap(lats, lons)

# save it to html
gmap.draw("/usr/share/nginx/html/players_heatmap.html")


#plt.gcf().set_size_inches(15,15)
#show map
#plt.show()