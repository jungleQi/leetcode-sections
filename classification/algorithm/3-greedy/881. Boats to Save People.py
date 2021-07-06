'''
The i person has weight people[i], and each boat can carry a maximum weight of limit.
Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
'''

# people[0, 1, ... k-1, k]，体重按升序排列。
# 结论一：如果people[k]都能将people[i]带走，那么people[j]更能将people[i]带走，所以将people[i]留给比people[k]体重小的带走，其中(i < j < k)
# 推论二：逆序遍历，每走一个就带一个当前最轻的走

def numRescueBoats(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    ans = 0
    while i <= j:
        ans += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return ans

people =[3]
limit = 4
print(numRescueBoats(people, limit))