#!/usr/bin/python
import math

w = 400
h = 400
zoom = 16
lat = 53.4055429
lng = -2.9976502

def getPointLatLng(x, y):
        parallelMultiplier = math.cos(lat * math.pi / 180)
        degreesPerPixelX = 360 / math.pow(2, zoom + 8)
        degreesPerPixelY = 360 / math.pow(2, zoom + 8) * parallelMultiplier
        pointLat = lat - degreesPerPixelY * ( y - h / 2)
        pointLng = lng + degreesPerPixelX * ( x  - w / 2)

        return (pointLat, pointLng)

print 'NE: ', getPointLatLng(w, 0)
print 'SW: ', getPointLatLng(0, h)
print 'NW: ', getPointLatLng(0, 0)
print 'SE: ', getPointLatLng(w, h)
