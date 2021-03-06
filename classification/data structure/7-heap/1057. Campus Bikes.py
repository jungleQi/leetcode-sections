'''
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M.
Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker.
Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other,
and assign the bike to that worker.
(If there are multiple (worker, bike) pairs with the same shortest Manhattan distance,
we choose the pair with the smallest worker index;
if there are multiple ways to do that,
we choose the pair with the smallest bike index).
We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

Example 1
Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation:
Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].
'''

from heapq import *

def assignBikes(workers, bikes):
    """
    :type workers: List[List[int]]
    :type bikes: List[List[int]]
    :rtype: List[int]
    """

    def closest_bike(w_row, w_col):
        min_distance = 2001
        min_b_id = None

        for b_id, (b_row, b_col) in bikes.items():
            distance = abs(w_row - b_row) + abs(w_col - b_col)

            if distance < min_distance:
                min_distance = distance
                min_b_id = b_id

        return min_distance, min_b_id

    bikes = dict(enumerate(bikes))
    seen = set()
    assignment = [None] * len(workers)
    heap = []

    for w_id, (w_row, w_col) in enumerate(workers):
        distance, b_id = closest_bike(w_row, w_col)
        heappush(heap, (distance, w_id, b_id))

    while len(seen) < len(workers):
        _, w_id, b_id = heappop(heap)

        if b_id in seen:
            w_row, w_col = workers[w_id]
            distance, b_id = closest_bike(w_row, w_col)
            heappush(heap, (distance, w_id, b_id))

        else:
            assignment[w_id] = b_id
            seen.add(b_id)
            del bikes[b_id]

    return assignment