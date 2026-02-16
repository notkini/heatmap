from flask import Flask, request, jsonify
import time
import geohash2
import pandas as pd
from flask import send_from_directory


app = Flask(__name__)

LOG_FILE = "zone_log.csv"

def log_violation(lat, lon):

    zone = geohash2.encode(lat, lon, precision=6)

    with open(LOG_FILE, "a") as f:
        f.write(f"phone,no_helmet,{lat},{lon},{zone},{time.time()}\n")

    print("Logged:", lat, lon)

@app.route("/")
def home():
    return send_from_directory(".", "phone.html")


@app.route("/gps", methods=["POST"])
def receive_gps():

    data = request.json
    lat = float(data["lat"])
    lon = float(data["lon"])

    log_violation(lat, lon)

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
