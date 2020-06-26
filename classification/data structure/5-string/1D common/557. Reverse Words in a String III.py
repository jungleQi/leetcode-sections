def reverseWords(s):
    return " ".join([i[::-1] for i in s.split()])

s = "ad sc"
print reverseWords(s)