from numpy import linspace
from math import sqrt, atan2, pi, degrees
import matplotlib.pyplot as plt
import matplotlib.transforms as tr
import matplotlib.patches as patches


c = 1
b = 0.1
P = 1

h = 2 * c
A = b * h

#X = linspace(0.1, 10 * c, 10)
X = linspace(2 * c, 2 * c, 1)
Y = linspace(-c, c, 11)

fig, ax = plt.subplots()

plt.xlim(-60, 60)
plt.ylim(-60, 60)
ax.set_aspect('equal', adjustable='box')
plt.axis('off')

base = plt.gca().transData
rot = tr.Affine2D().rotate_deg_around(20, 20, 45)

rect = patches.Rectangle((0, 0), 40, 40, linewidth=1, edgecolor='r', facecolor='none', transform=rot+base)
arrw = patches.Arrow(40, 20, 20, 0, width=5, transform=rot+base)

ax.add_patch(rect)
ax.add_patch(arrw)

plt.show()

for x in X:

    sm  = 3 * P * x * c / A / c ** 2

    for y in Y:

        sx  = 3 * P * x * y / A / c ** 2















        txy = 3 * P * (1 - y ** 2 / c ** 2) / 2 / A

        sa = sx / 2
        R = sqrt((sx / 2) ** 2 + txy ** 2)
        smax = sa + R
        smin = sa - R

        T = pi / 2
        if sa != 0:
            T = degrees(atan2(txy, sa) / 2)
        
        print(round(smax / sm, 3), T)

