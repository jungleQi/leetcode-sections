def reconstructQueue(people):
    res = []
    sortPeople = sorted(people, key=lambda x:(-x[0],x[1]))
    for item in sortPeople:
        res.insert(item[1], item)
    return res

people = [[7,0]]
print reconstructQueue(people)