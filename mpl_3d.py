'''
Plot example data for debugging my functions
'''

# import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cart2sphere import cart2sphere, sphere2cart
from math import pi

fig = plt.figure()
ax = fig.gca(projection='3d')


# Create a sphere
x_vals = []
y_vals = []
z_vals = []

for phi in range(90):
    for theta in range(90):
        x, y, z = sphere2cart(1, theta * pi/180, phi * pi/180)
        x_vals.append(x)
        y_vals.append(y)
        z_vals.append(z)

ax.plot(x_vals, y_vals, z_vals)

plt.show()