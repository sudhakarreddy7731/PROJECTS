n = int(input("Enter no of packages: "))

package = []
very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []

for i in range(n):
    package.append(int(input("Enter package weight: ")))

for w in package:
    if w < 0:
        invalid_entries.append(w)
    elif w <= 5:
        very_light.append(w)
    elif w <= 25:
        normal_load.append(w)
    elif w <= 60:
        heavy_load.append(w)
    else:
        overload.append(w)

# ---- Name and PLI ----
NAME = input("Enter full name: ")
L = 0
for ch in NAME:
    if ch != " ":
        L += 1

PLI = L % 3

print("L =", L)
print("PLI =", PLI)

Total_valid_counts=len(very_light)+len(normal_load)+len(heavy_load)+len(overload)

affected = 0

if PLI == 0:
    print("Applied Rule A")
    affected =len(overload)
    invalid_entries=invalid_entries+overload
    overload.clear()

elif PLI == 1:
    print("Applied Rule B")
    affected=len(very_light)
    very_light.clear()

else:
    print("Applied Rule C")
    affected=len(very_light)+len(overload)
    very_light.clear()
    overload.clear()

print("Total valid weights:", Total_valid_counts)
print("Affected items due to PLI:", affected)
print("Very Light:", very_light)
print("Normal Load:", normal_load)
print("Heavy Load:", heavy_load)
print("Overload:", overload)
print("Invalid Entries:", invalid_entries)
