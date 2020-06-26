def validPalindrome(s):
    l,r = 0,len(s)-1
    while l<r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            s1 = s[:l]+s[l+1:]
            s2 = s[:r]+s[r+1:]

            return s1 == s1[::-1] or s2 == s2[::-1]

    return True

s = "ad"
print(validPalindrome(s))