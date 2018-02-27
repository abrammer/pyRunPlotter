'''
 Stupid script to plot all activities from built json 
    n.b. Adding lines to list and setting data for animation allows blit to be used
        This speeds things up tremendously. 
        
'''

from os import listdir
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from mpl_toolkits.basemap import Basemap
import json


print("Reading")
with open('outputfile','r') as fin:
	running_data = json.load(fin)


print("Plotting")
fig = plt.figure(facecolor='0.0',edgecolor='0.0',frameon=False)
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
m = Basemap(projection='merc', llcrnrlat=42.62, urcrnrlat=42.73,\
            llcrnrlon=-73.92, urcrnrlon=-73.71, lat_ts=20, resolution='c', ax=ax)
m.fillcontinents(color='0.0', lake_color='0.0')

maxtracklength = 0
lines = []
latlist,lonlist = [],[]
for runId,runData in running_data.items():
    lat,lon = [list(i) for i in zip(*runData)]
    maxtracklength = max(maxtracklength, len(lat))
    x1,y1 = m( lon, lat)
    latlist.append(y1)
    lonlist.append(x1)
    lobj = m.plot([],[],lw=0.2,color='deepskyblue', alpha=0.8)[0]
    lines.append(lobj)

def init():
    ''' set lines to blank '''
    for line in lines:
        line.set_data([],[])
    return lines

def animate(i):
    ''' Add data to line with iterating frame number '''
    for lnum,line in enumerate(lines):
        line.set_data(lonlist[lnum][:i*5], latlist[lnum][:i*5]) # set data for each line separately.     
    return lines

print("Rendering")
anim = animation.FuncAnimation(plt.gcf(), animate,init_func=init,blit=True,
                           frames=int(maxtracklength/5)+15, interval=10)


anim.save('basic_animation.mp4', fps=60, dpi=300,
     extra_args=['-vcodec', 'libx264'])
