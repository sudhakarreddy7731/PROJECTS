import random
import pandas as  pd
import numpy as  np
import math
def generate_data(n):
    data = []
    for i in range(n):
        record = {
            "zone": i+1,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        }
        data.append(record)
    return data

def classify_zone(record):
    if record["air_quality"] > 200 or record["traffic"] > 80:
        return "High Risk"
    elif record["energy"] > 400:
        return "Energy Critical"
    elif record["traffic"] < 30 and record["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"


# STEP 3: CUSTOM RISK SCORE
def calculate_risk(record):
    return (record["traffic"] * 0.7 +
            record["air_quality"] * 0.6 +
            record["energy"] * 0.3)

def custom_sort(data, key):
    return sorted(data, key=lambda x: x[key], reverse=True)
# checking stability
def detect_stability(traffic_list):
    return np.var(traffic_list) < 200
# CLUSTER
def detect_clusters(data):
    clusters = []
    temp = []
    for d in data:
        if d["risk_score"] > 5:   # adjusted for log scale
            temp.append(d["zone"])
        else:
            if len(temp) >= 2:
                clusters.append(temp)
            temp = []
    if len(temp) >= 2:
        clusters.append(temp)
    return clusters
#main
roll_number = 24110012124
n=int(input("Enter the number of zones: "))
data = generate_data(n)


# LOG-TRANSFORMATION
for d in data:
    d["category"] = classify_zone(d)

    raw_score = calculate_risk(d)
    d["risk_score"] = math.log(raw_score + 1)   # transformation applied


if roll_number % 3 == 0:# since my number is divisible by 3
    random.shuffle(data)
else:
    data = custom_sort(data, "traffic")

# DataFrame
df = pd.DataFrame(data)

# NumPy analysis
arr = df[["traffic", "air_quality", "energy"]].values
mean_vals = np.mean(arr, axis=0)

# Top 3 zones
sorted_data = custom_sort(data, "risk_score")
top3 = sorted_data[:3]
# Risk tuple
risks = [d["risk_score"] for d in data]#list comprehentionm

risk_tuple = (max(risks), np.mean(risks), min(risks))
stability = detect_stability(df["traffic"].tolist())
clusters = detect_clusters(sorted_data)
# Final decision
avg_risk = risk_tuple[1]
if avg_risk < 3:
    decision = "City Stable"
elif avg_risk < 4:
    decision = "Moderate Risk"
elif avg_risk < 5:
    decision = "High Alert"
else:
    decision = "Critical Emergency"
# OUTPUT
print("\nDataFrame:\n", df)
print("Mean values of traffic, AQI, energy:")
print(mean_vals)
print("Top 3 risk zones:")
for z in top3:
    print(z)
print("risk tuple max, avg, min:")
print(risk_tuple)
print("stability:", "stable" if stability else "unstable")
print("critical clusters:", clusters)
print("final decision :", decision)
print("what is smart city??\n")
print("A smart city maintains balanced traffic, low pollution, and efficient energy use while minimizing risk clusters.")