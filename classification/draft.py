def monotoneIncreasingDigits(N):
    digStr = list(str(N))
    start = 0
    for i in range(1, len(digStr)):
        if digStr[i]>digStr[i-1]:
            start = i
        elif digStr[i]<digStr[i-1]:
            break

    if start == len(digStr)-1:
        return N
    else:
        if digStr[start] == '1':
            return int('9'*(len(digStr)-start-1))
        else:
            digStr[start] = str(int(digStr[start])-1)
            return int("".join(digStr[:start+1]) + '9'*(len(digStr)-start-1))

# 10  9
# 123 123
# 3306 299

N = 1008
print(monotoneIncreasingDigits(N))