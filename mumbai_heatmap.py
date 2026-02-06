import pandas as pd
import folium
from folium.plugins import HeatMap

# Load violation log
df = pd.read_csv("zone_log.csv")

# Mumbai center coordinates
MUMBAI_CENTER = [19.0760, 72.8777]

# Create base map
m = folium.Map(
    location=MUMBAI_CENTER,
    zoom_start=12,
    tiles="OpenStreetMap"
)

# Prepare heatmap data
heat_data = df[["lat", "lon"]].values.tolist()

# Add heat layer
HeatMap(
    heat_data,
    radius=18,
    blur=25,
    min_opacity=0.4
).add_to(m)

# Save map
m.save("mumbai_violation_heatmap.html")

print("\ Heatmap created: mumbai_violation_heatmap.html")
