#coding=utf-8

'''
You are driving a vehicle that has capacity empty seats initially available for passengers.
The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip:
 the number of passengers that must be picked up, and the locations to pick them up and drop them off.
 The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.

Example 1
trips = [[4,5,6],[6,4,7],[4,3,5],[2,3,5]]
capacity = 13
Output: True
'''

def carPooling(trips, capacity):
    pairs = []
    for trip in trips:
        pairs += [trip[1],trip[0]],
        pairs += [trip[2], -trip[0]],
    #x:(x[0],x[1]) 很关键，对x[0]比较，还要对x[1]比较，防止在同一地点既有上又有下的情况
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