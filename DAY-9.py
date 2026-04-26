import copy
def generate_data():
    users = [
        {
            "id": 1,
            "data": {"files": ["a.txt", "b.txt"], "usage": 500}
        },
        {
            "id": 2,
            "data": {"files": ["c.txt"], "usage": 300}
        }
    ]
    return users

def replicate_data(original):
    assigned = original
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    return assigned, shallow, deep

def modify_data(data, roll_number):
    for user in data:
        # EVEN → add file
        if roll_number % 2 == 0:
            user["data"]["files"].append("new_file.txt")
        # ODD → remove file
        else:
            if user["data"]["files"]:
                user["data"]["files"].pop()


        user["data"]["usage"] += 100


def check_integrity(original, shallow, deep):
    leakage_count = 0
    safe_count = 0
    overlap_count = 0

    for i in range(len(original)):
        original_files = set(original[i]["data"]["files"])
        shallow_files = set(shallow[i]["data"]["files"])
        deep_files = set(deep[i]["data"]["files"])


        # if original == shallow → means shallow changed original
        if original_files == shallow_files:
            leakage_count += 1


        # deep copy should be independent
        if original_files != deep_files:
            safe_count += 1
        overlap = original_files.intersection(shallow_files)
        overlap_count += len(overlap)

    return leakage_count, safe_count, overlap_count



def main():
    roll_number = 24110012124
    original = generate_data()
    print("\nBEFORE MODIFICATION :")
    print("Original:", original)

    # Replication
    assigned, shallow, deep = replicate_data(original)

    #  Modify copies
    modify_data(shallow, roll_number)
    modify_data(deep, roll_number)

    print("\nAFTER MODIFICATION :")
    print("Original:", original)
    print("Shallow Copy:", shallow)
    print("Deep Copy:", deep)
    result = check_integrity(original, shallow, deep)

    print("\n INTEGRITY REPORT :")
    print("leakage_count, safe_count, overlap_count  respectively ", result)


# Run
main()