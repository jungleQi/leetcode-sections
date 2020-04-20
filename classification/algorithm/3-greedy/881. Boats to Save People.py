def numRescueBoats(people, limit):
    people = sorted(people, reverse=True)

    boats = 0
    headIdx, rearIdx = 0, len(people)-1
    while headIdx <= rearIdx:
        if people[headIdx]+people[rearIdx] <= limit:
            headIdx += 1
            rearIdx -= 1
        else:
            headIdx += 1
        boats += 1

    return boats

people =[3]
limit = 4
print numRescueBoats(people, limit)