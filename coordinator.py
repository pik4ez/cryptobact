#!/bin/env python3

from random import random

# generates random coordinates for infection map
def gen_coords():
    coeff = 10
    radius = 0.0001

    # {x,y,weight}
    pest_holes = [
            (55.029633,82.913559,10),
            (55.029738,82.915791,2),
            (55.029978,82.916831,6),
            (55.029978,82.916831,4),
            (55.029104,82.908098,8)
            ]

    result = []
    for ph in pest_holes:
        for i in range(ph[2] * coeff):
            x = ph[0] + (0.5 - random()) * radius
            y = ph[1] + (0.5 - random()) * radius
            result.append((x,y))
    return result


if __name__ == '__main__':
    coords = gen_coords()
    for p in coords:
        # {location: new google.maps.LatLng(55.837106,37.481588), weight: 10},
        print("{location: new google.maps.LatLng(%2.6f,%2.6f), weight: nskWeight}," % p)
