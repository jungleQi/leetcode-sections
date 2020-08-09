'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:
1.If there exists a solution, it is guaranteed to be unique.
2.Both input arrays are non-empty and have the same length.
3.Each element in the input arrays is a non-negative integer.

Example 1:
Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3
'''

def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    curr_gas = total_gas = 0
    start_idx = 0
    for i in range(len(gas)):
        curr_gas += gas[i] - cost[i]
        total_gas += gas[i] - cost[i]
        if curr_gas < 0:
            start_idx = i + 1
            curr_gas = 0
    return start_idx if total_gas >= 0 else -1