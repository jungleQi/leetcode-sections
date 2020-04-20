def carPooling(trips, capacity):
    pairs = []
    for trip in trips:
        pairs += [trip[1],trip[0]],
        pairs += [trip[2], -trip[0]],
    pairs = sorted(pairs, key=lambda x:(x[0],x[1]))

    total = 0
    for item in pairs:
        total += item[1]
        if total > capacity:
            return False

    return total == 0

trips = [[4,5,6],[6,4,7],[4,3,5],[2,3,5]]
capacity = 13
print carPooling(trips, capacity)