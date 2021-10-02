import numpy as np

def Ellipsoid(u, v, a=1, b=1, c=1):
    # x**2/a**2 + y**2/b**2 + z**2/c**2 = 1
    # u_range = [0, 2*PI], v_range=[0, PI]
    return np.array([a * np.cos(u) * np.sin(v),
                     b * np.sin(u) * np.sin(v),
                     c * np.cos(v)])

def Cone(u, v, a=1, b=1, c=1):
    # z**2/c**2 = x**2/a**2 + y**2/b**2
    return np.array([a * v * np.cos(u),
                     b * v * np.sin(u),
                     c * v])

def EllipticParaboloid(u, v, a=1, b=1, c=1):
    # z/c = x**2/a**2 + y**2/b**2
    # u_range = [0, height], v_range = [0, 2*PI]
    return np.array([a * np.sqrt(u) * np.cos(v),
                     b * np.sqrt(u) * np.sin(v),
                     c * u])