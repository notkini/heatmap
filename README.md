# 🚁 Drone Traffic Violation Detection & Heatmap (Demo Version)

This project detects traffic violations from images using a YOLO model and plots violation hotspots on a map of Mumbai.

It simulates a drone-based monitoring system but works completely on a normal laptop.

NO drone required
NO GPS module required
Works at home using fake coordinates

---

# 🧠 What This Project Does

1. Detects violations from an image
2. Tags violations with location (GPS or simulated)
3. Stores violations in CSV
4. Aggregates hotspots
5. Generates a heatmap map

---

# ⚙️ Requirements

Install dependencies:

```
pip install ultralytics opencv-python folium flask pandas numpy
```

Make sure Python 3.9+ is installed.

---

# 📁 Project Files Overview

Important files you will run:

```
photo_violation_detector.py   → Detect violations from image
gps_simulator.py              → Fake GPS generator (HOME DEMO)
zone_heat_engine.py           → Build hotspot data
mumbai_heatmap.py             → Generate map
model.pt                      → Trained YOLO model
```

Output files:

```
zone_log.csv
zone_hotspots.csv
mumbai_violation_heatmap.html
```

---

# 🚀 HOW TO RUN (START HERE)

## ✅ STEP 1 — Detect Violations from Image

Put your test image inside the project folder
(or use the provided one).

Open:

```
photo_violation_detector.py
```

Change the image path if needed.

Run:

```
python photo_violation_detector.py
```

👉 This will:

* Load model.pt
* Detect helmet / no-helmet / rider / plate
* Log violations to zone_log.csv

---

## ✅ STEP 2 — Add Location (HOME DEMO METHOD)

Since you don't have GPS hardware, use fake coordinates.

Open:

```
gps_simulator.py
```

Edit coordinates if desired:

Example Mumbai location:

```
latitude = 19.0760
longitude = 72.8777
```

Run:

```
python gps_simulator.py
```

👉 This attaches location data to violations.

---

## ✅ STEP 3 — Generate Hotspots

Run:

```
python zone_heat_engine.py
```

👉 Creates:

```
zone_hotspots.csv
```

---

## ✅ STEP 4 — Generate Mumbai Heatmap

Run:

```
python mumbai_heatmap.py
```

👉 Creates:

```
mumbai_violation_heatmap.html
```

---

## ✅ STEP 5 — View the Map

Open:

```
mumbai_violation_heatmap.html
```

in your browser.

You will see violation hotspots on the Mumbai map.

---

# 📍 Demo Coordinates You Can Use

Paste any of these into gps_simulator.py

### Bandra

```
19.0596, 72.8295
```

### Andheri

```
19.1136, 72.8697
```

### Dadar

```
19.0176, 72.8562
```

### Powai

```
19.1176, 72.9060
```

### Colaba

```
18.9067, 72.8147
```

---

# 📱 OPTIONAL — Use Phone as GPS

If you want real phone location:

Run server:

```
python phone_gps_server.py
```

Open on phone (same Wi-Fi):

```
http://YOUR_LAPTOP_IP:5000
```

Send location from phone.

---

# 🤖 Model Classes

The YOLO model detects:

* Helmet
* No Helmet
* Rider
* Number Plate

---

# 🛰️ Real Drone Use (Future)

In actual deployment:

Drone Camera → Detection → GPS Module → Logging → Live Heatmap

---

# 🧪 Important Notes

✔ Current version works on images only
✔ No hardware required
✔ Fully offline demo possible
✔ Heatmap updates when more violations are logged

---

# 👨‍💻 Use Case

Smart traffic monitoring system for:

* Police surveillance
* Smart city projects
* Drone-based enforcement
* Research demonstrations

---

# ⭐ Done!

Follow Steps 1 → 5 in order to reproduce results.
