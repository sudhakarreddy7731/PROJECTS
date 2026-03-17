# Energy readings list (example input)
readings = []
n=int(input("enter the number of readings: "))
for i in range(n):
    readings.append(int(input("enter the reading : ")))


# Dictionary for classification
usage = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}

# Classification using loop and conditions
for e in readings:
    if e < 0:
        usage["invalid"].append(e)
    elif 0 <= e <= 50:
        usage["efficient"].append(e)
    elif 51 <= e <= 150:
        usage["moderate"].append(e)
    else:
        usage["high"].append(e)

# List comprehension (used to ignore invalid values for total)
valid_readings = [e for e in readings if e >= 0]

# Statistics
total_consumption = sum(valid_readings)
num_buildings = len(valid_readings)

# Tuple summary
summary = (total_consumption, num_buildings)

# Efficiency analysis
high_count = len(usage["high"])
efficient_count = len(usage["efficient"])
moderate_count = len(usage["moderate"])

if high_count > 3:
    result = "Overconsumption"

elif abs(efficient_count - moderate_count) <= 1:
    result = "Balanced Usage"

elif total_consumption > 600:
    result = "Energy Waste Detected"

elif high_count == 0:
    result = "Efficient Campus"

else:
    result = "Moderate Usage"

# Final Report
print("Energy Usage Categories:")
for key, value in usage.items():
    print(key, ":", value)

print("Summary : Total Consumption, Number of Buildings :", summary)

print("Efficiency Result:", result)