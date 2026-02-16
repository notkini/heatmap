# gps_simulator.py

import random

# Mumbai demo locations
POINTS = [
    (18.9220, 72.8347),  # Gateway
    (19.0176, 72.8562),  # Dadar
    (19.0466, 72.8195),  # Bandra
    (19.1075, 72.8263),  # Juhu
    (19.1136, 72.8697),  # Andheri
    (19.0850, 72.9080),  # Ghatkopar
]

index = 0

def get_gps():
    global index

    lat, lon = POINTS[index]

    # optional jitter for realism
    lat += random.uniform(-0.001, 0.001)
    lon += random.uniform(-0.001, 0.001)

    index = (index + 1) % len(POINTS)

    return lat, lon
