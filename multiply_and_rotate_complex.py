import numpy as np


def multiply_complex(z1, z2):
    a1, b1 = z1
    a2, b2 = z2
    a = a1 * a2 - b1 * b2
    b = a1 * b2 + b1 * a2
    return np.array([a, b])

def from_polar(theta, r=1):
    return np.array([r * np.cos(theta), r * np.sin(theta)])

def rotate(z, theta):
    return multiply_complex(z, from_polar(theta))


# print(rotate(np.array([7.5, 1.1]), np.pi/12))