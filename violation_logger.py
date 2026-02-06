import time
from gps_simulator import get_random_india_gps
from spatial_hash import get_zone_hash

LOG_FILE = "zone_log.csv"

def log_violation(v_type, photo_name):

    lat, lon = get_random_india_gps()
    zone = get_zone_hash(lat, lon)

    with open(LOG_FILE, "a") as f:
        f.write(f"{photo_name},{v_type},{lat},{lon},{zone},{time.time()}\n")

    print(f"[LOGGED] {photo_name} → {v_type} → zone {zone}")
