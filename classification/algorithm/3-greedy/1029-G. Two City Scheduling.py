'''
A company is planning to interview 2n people.
 Given the array costs where costs[i] = [aCost_i, bCost_i],
 the cost of flying the i_th person to city a is aCost_i,
 and the cost of flying the i_th person to city b is bCost_i.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
'''

def twoCitySchedCost(costs):
    costs.sort(key=lambda x: x[0] - x[1])

    total = 0
    n = len(costs) // 2
    # To optimize the company expenses,
    # send the first n persons to the city A
    # and the others to the city B
    for i in range(n):
        total += costs[i][0] + costs[i + n][1]
    return total

costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
print(twoCitySchedCost(costs))