def rand7():
    return 1

def rand10():
    idx = 400
    while idx > 40:
        row = rand7()
        col = rand7()
        idx = col + (row - 1) * 7
    return 1 + (idx - 1) % 10