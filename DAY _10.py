import random
import copy
import math
import numpy as np
import pandas as pd
def generate_data(n=15):
    data = []
    for i in range(n):
        data.append({
            "zone": i+1,
            "metrics": {
                "traffic": random.randint(10, 100),
                "pollution": random.randint(10, 100),
                "energy": random.randint(10, 100)
            },
            "history": [random.randint(5, 50) for _ in range(5)]
        })
    return data

def personalize(data, roll):
    return data[::-1] if roll % 2 == 0 else data[3:] + data[:3]

def custom_risk(t, p, e):
    return math.log(t+p+e+1) * (t + 2*p + e) / 100

def mutate(data):
    for d in data:
        d["metrics"]["traffic"] += 5
        d["metrics"]["pollution"] += 3
        d["history"].append(random.randint(1, 20))

        t = d["metrics"]["traffic"]
        p = d["metrics"]["pollution"]
        e = d["metrics"]["energy"]

        d["risk"] = custom_risk(t, p, e)

def manual_corr(x, y):
    mx, my = np.mean(x), np.mean(y)
    return np.sum((x-mx)*(y-my)) / np.sqrt(np.sum((x-mx)**2) * np.sum((y-my)**2))


data = generate_data()

# Step 2
roll_number =24110012124
data = personalize(data, roll_number)
assign = data
shallow = copy.copy(data)
deep = copy.deepcopy(data)
print(" BEFORE:")
print(data[0])
mutate(shallow)

# AFTER
print("\n AFTER :")
print("Original:", data[0])
print("Shallow:", shallow[0])
print("Deep:", deep[0])


rows = []
for d in shallow:
    rows.append({
        "zone": d["zone"],
        "traffic": d["metrics"]["traffic"],
        "pollution": d["metrics"]["pollution"],
        "energy": d["metrics"]["energy"],
        "risk": d["risk"]
    })

df = pd.DataFrame(rows)
print("\n DataFrame :")
print(df)

# Step 6 (Analysis)
mean = np.mean(df["risk"])
var = np.var(df["risk"])
std = np.std(df["risk"])

anomalies = df[df["risk"] > mean + std]

corr = manual_corr(df["traffic"].values, df["pollution"].values)

print("\nMean:", mean)
print("Variance:", var)
print("Correlation:", corr)

print("\nAnomalies :")
print(anomalies)


clusters, temp = [], []
for z in df[df["risk"] > mean]["zone"]:
    if not temp or z == temp[-1] + 1:
        temp.append(z)
    else:
        clusters.append(temp)
        temp = [z]
if temp:
    clusters.append(temp)

print("\nClusters:", clusters)
stability = 1 / (var + 1e-5)
result = (df["risk"].max(), df["risk"].min(), stability)
print("\nTuple:", result)
high_risk = set(df[df["risk"] > mean]["zone"])
print("\nHigh Risk Zones:", high_risk)
print("\nSqrt Energy:", np.sqrt(df["energy"]).values)

if stability > 5:
    print("\nDecision: System Stable")
elif stability > 2:
    print("\nDecision: Moderate Risk")
elif stability > 1:
    print("\nDecision: High Corruption Risk")
else:
    print("\nDecision: Critical Failure")