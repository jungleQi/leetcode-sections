'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first 5-string's permutations is the substring of the second 5-string.
'''

#count in sliding window

from collections import Counter

def checkInclusion(s1, s2):
    M, N = len(s1), len(s2)
    if M > N: return False

    counter1 = Counter(s1)
    win_counter = Counter(s2[:M])
    if counter1 == win_counter: return True

    left,right = 0,M
    while right < N:
        win_counter[s2[left]] -= 1
        if win_counter[s2[left]] == 0:
            del win_counter[s2[left]]
        win_counter[s2[right]] += 1
        if counter1 == win_counter: return True

        left += 1
        right += 1

    return False

s1 = "a"
s2 = "ss"
print(checkInclusion(s1, s2))