# -*- coding: utf-8 -*-
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

myMap = Basemap(projection='cyl')
myMap.drawmapboundary()
myMap.drawstates()
myMap.drawcoastlines()
myMap.drawcountries()
parallels = np.arange(-90, 90, 10.)
myMap.drawparallels(parallels, labels=[1, 0, 0, 0], fontsize=10)  # 绘制纬线
meridians = np.arange(-180., 180., 60.)
myMap.drawmeridians(meridians, labels=[0, 0, 0, 1], fontsize=10)  # 绘制经线

posi = pd.read_csv('directory.csv')
lat = np.array(posi["Latitude"])        # 获取维度之维度值
lon = np.array(posi["Longitude"])
x, y = myMap(lon, lat)
myMap.scatter(x, y)     # 也可以使用Basemap的methord本身的scatter

storeNumber = np.array(posi["Store Number"])
length = len(np.array(posi["Brand"]))
for i in range(1000):
    plt.text(x[i], y[i], 'Store Number: %s' % storeNumber[i])

plt.title('Starbucks')
plt.show()
