#Smart Playlist Intelligence System`
n = int(input("Enter number of songs that you want to insert into your playlist: "))
durations = []
invalid_found = False
#takes input to durations list
for i in range(n):
    value = int(input("Enter duration in seconds: "))

    if value <= 0:
        invalid_found = True
    else:
        durations.append(value)

# Validation Check
if invalid_found:
    print("\nInvalid Playlist: Contains invalid duration (<= 0)")
else:
    totalDuration = sum(durations)
    songCount = len(durations)
    minDuration = min(durations)
    maxDuration = max(durations)
    repetitive = False
    for i in range(len(durations)):
        for j in range(i + 1, len(durations)):
            if durations[i] == durations[j]:
                repetitive = True

    variation = maxDuration - minDuration
    if totalDuration < 300:
        category = "Too Short Playlist"
        recommendation = "Add  few more songs to increase engagement."

    elif totalDuration > 3600:
        category = "Too Long Playlist"
        recommendation = "You should break your playlist into few more playlists"

    elif repetitive:
        category = "Repetitive Playlist"
        recommendation = "Add variety songs"

    elif variation > 30:
        category = "Balanced Playlist"
        recommendation = "Good listening session"

    else:
        category = "Irregular Playlist"
        recommendation = "Adjust durations for better balance"

    print("Total Duration of PlayList:", totalDuration, "seconds")
    print("Songs count in playList:", songCount)
    print("Category of PlayList:", category)
    print("Recommendation :", recommendation)