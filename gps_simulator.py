import random

MIN_LAT = 18.85
MAX_LAT = 19.35
MIN_LON = 72.75
MAX_LON = 73.05

def get_random_india_gps():
    lat = random.uniform(MIN_LAT, MAX_LAT)
    lon = random.uniform(MIN_LON, MAX_LON)
    return round(lat, 6), round(lon, 6)
