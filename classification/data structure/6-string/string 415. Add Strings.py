def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    list1, list2 = list(num1), list(num2)

    out = c = 0
    while list1:
        out += (ord(list1.pop()) - ord('0')) * (10 ** c)
        c += 1

    c = 0
    while list2:
        out += (ord(list2.pop()) - ord('0')) * (10 ** c)
        c += 1

    return str(out)