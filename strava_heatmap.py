''' Script to grab activities from strava and plot with basemap'''    
import matplotlib.pyplot as plt
import os
import numpy as np
from mpl_toolkits.basemap import Basemap
from configparser import SafeConfigParser
import json

with open('outputfile','r') as fin:
	running_data = json.load(fin)


fig = plt.figure(facecolor='0.0')
m = Basemap(projection='merc',llcrnrlat=42.62,urcrnrlat=42.73,\
            llcrnrlon=-73.92,urcrnrlon=-73.71,lat_ts=20,resolution='c')
m.drawparallels(np.arange(-90.,91.,10.))
m.drawmeridians(np.arange(-180.,181.,10.))
m.fillcontinents(color='0.0',lake_color='0.0')


for activity in running_data:
    lat = []
    lon = []
    for point in activity:
        lat.append(point[0])
        lon.append(point[1])
    xpt, ypt =  m(lon, lat)
    _ = m.plot( xpt, ypt, color='deepskyblue', lw=0.2, alpha=0.8)

imgFilename =  'heatmap.png'
plt.savefig(imgFilename,
            facecolor=fig.get_facecolor(),
            bbox_inches='tight',
            pad_inches=0,
            dpi=600)

