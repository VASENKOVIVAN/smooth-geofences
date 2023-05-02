""" 
Thanks: https://wiki.openstreetmap.org/wiki/Mercator#Python/
"""
import math

R = 6378137.0


def y2lat(y_mercator):
    """ docstring """
    return math.degrees(2 * math.atan(math.exp(y_mercator / R)) - math.pi / 2.0)


def lat2y(lat):
    """ docstring """
    return math.log(math.tan(math.pi / 4 + math.radians(lat) / 2)) * R


def x2lng(x_mercator):
    """ docstring """
    return math.degrees(x_mercator / R)


def lon2x(lon):
    """ docstring """
    return math.radians(lon) * R


def wgs84_to_mercator(arr_with_wgs84):
    """ docstring """
    return [[lon2x(coord[1]), lat2y(coord[0])] for coord in arr_with_wgs84]


def mercator_to_wgs84(arr_with_mercator):
    """ docstring """
    return [[x2lng(coord[1]), y2lat(coord[0])] for coord in arr_with_mercator]
