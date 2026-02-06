import geohash2

def get_zone_hash(lat, lon, precision=6):
    return geohash2.encode(lat, lon, precision)
