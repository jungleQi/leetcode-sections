#coding=utf-8

def assignBikes(workers, bikes):
    """
    :type workers: List[List[int]]
    :type bikes: List[List[int]]
    :rtype: List[int]
    """
    pairs = []
    for i, worker in enumerate(workers):
        for j, bike in enumerate(bikes):
            pairs.append((abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]), i, j))
            #三个元素的排列，距离没有放在第一个，会导致后面sort TLE
            #pairs.append((i, j, abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])))

    #pairs.sort(key=lambda x:(x[2],x[1],x[0]))
    pairs.sort()
    ans = [-1] * len(workers)
    bike_taken = set()
    for dist, i, j in pairs:
        # print i,j
        if ans[i] == -1 and j not in bike_taken:
            ans[i] = j
            bike_taken.add(j)
    return ans