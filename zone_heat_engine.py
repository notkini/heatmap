import pandas as pd

df = pd.read_csv("zone_log.csv")

zone_counts = (
    df.groupby("zone")
    .size()
    .reset_index(name="violations")
    .sort_values(by="violations", ascending=False)
)

def classify(v):
    if v > 20:
        return "HIGH"
    elif v > 8:
        return "MEDIUM"
    else:
        return "LOW"

zone_counts["risk"] = zone_counts["violations"].apply(classify)

print("\n=== HOTSPOT ANALYSIS ===\n")
print(zone_counts)

zone_counts.to_csv("zone_hotspots.csv", index=False)
