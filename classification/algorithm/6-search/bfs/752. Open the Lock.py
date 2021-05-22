'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it is impossible.


Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
'''

import collections
def openLock_SLOW(deadends, target):
    visitor = set("0000")
    q = collections.deque([["0000", 0]])
    while q:
        item, l = q.popleft()
        if item == target: return l

        for i,c in enumerate(item):
            if c == '0':
                cur = item[:i] + "1" + item[i+1:]
                if cur not in visitor and cur not in deadends:
                    q.append([cur, l+1])
                    visitor.add(cur)
                cur = item[:i] + "9" + item[i+1:]
                if cur not in visitor and cur not in deadends:
                    q.append([cur, l+1])
                    visitor.add(cur)
            else:
                cur =  item[:i] + str(int(c)-1) + item[i+1:]
                if cur not in visitor and cur not in deadends:
                    q.append([cur, l + 1])
                    visitor.add(cur)
                if c == '9':
                    cur = item[:i] + '0' + item[i+1:]
                    if cur not in visitor and cur not in deadends:
                        q.append([cur, l + 1])
                        visitor.add(cur)
                else:
                    cur = item[:i] + str(int(c) + 1) + item[i + 1:]
                    if cur not in visitor and cur not in deadends:
                        q.append([cur, l + 1])
                        visitor.add(cur)
    return -1


def openLock_fast(deadends, target):
    begin = {'0000'}
    end = {target}
    deads = set(deadends)
    level = 0
    begin -= deads
    while begin and end:
        tmp = set()
        for s in begin:
            if s in end:
                return level
            deads.add(s)
            for i, c in enumerate(s):
                a = s[:i] + str((int(c) + 1) % 10) + s[i + 1:]
                if a not in deads:
                    tmp.add(a)

                b = s[:i] + str((int(c) - 1) % 10) + s[i + 1:]
                if b not in deads:
                    tmp.add(b)
        level += 1
        begin = end
        end = tmp
    return -1

deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
print(openLock_fast(deadends, target))