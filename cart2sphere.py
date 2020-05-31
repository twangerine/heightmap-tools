# Cartesian to Spherical Co-ordinates function

from math import acos, asin, atan, atan2
from math import sin, cos, tan
from math import pi, sqrt

def cart2sphere(x,y,z):
    r = sqrt(x*x+y*y+z*z)
    theta = atan2(y, x)
    phi = acos(z/r)
    return r, theta, phi

def sphere2cart(r,theta,phi):
    x = r * sin(phi) * cos(theta)
    y = r * sin(phi) * sin(theta)
    z = r * cos(phi)
    return x, y, z

