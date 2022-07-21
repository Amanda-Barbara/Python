import numpy as np
from matplotlib import pyplot
from shapely.geometry import Point, Polygon, LineString, MultiLineString
from descartes import PolygonPatch

BLUE = 'blue'
GRAY = 'gray'

fig = pyplot.figure()

# [[141, 46], [140, 47], [142, 47], [142, 46]]缺陷区域
# 144.96774291992188 52.54838943481445 6.36 圆心半径
# a = Point(144.968, 52.548).buffer(6.66)
# b = Polygon([[138.5, 49], [141, 46], [140, 47], [142, 50], [142, 46]])
# b = Point(1.5, 1).buffer(1.5)
a = Point(1, 1).buffer(1)
b = Polygon([[1, 2], [1.2, 1.8], [1.6, 1.9], [1.9, 1.6], [1.7, 0.9],
             [1.9, 0.7], [2.6, 1], [2.5, 1.7], [1.9, 2.5], [1.2, 2.5]])

#3
ax = fig.add_subplot(111)

patch1 = PolygonPatch(a, fc=GRAY, ec=GRAY, alpha=0.2, zorder=1)
ax.add_patch(patch1)
patch2 = PolygonPatch(b, fc=GRAY, ec=GRAY, alpha=0.2, zorder=1)
ax.add_patch(patch2)
d = a.intersection(b)
d = a.boundary.intersection(b.boundary)
# d = a.intersection(b)
# patchd = PolygonPatch(d, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
# ax.add_patch(patchd)
# print(d.length)
x = []
y = []
for point in d:
    x.append(point.x)
    y.append(point.y)
pyplot.plot(x, y, color="red", linewidth=0.5, linestyle="-", label="circle")
# ax.set_title('a.intersection(b)')
ax.set_title('a.boundary.intersection(b.boundary)')
pyplot.xlim([-1, 3])
pyplot.ylim([-1, 3])
ax.set_aspect(1)
ax.invert_yaxis()  #y轴反向

# show all figures
pyplot.show()
