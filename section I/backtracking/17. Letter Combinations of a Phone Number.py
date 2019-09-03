def letterCombinations(digits):
    combinations = []
    phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

    def backtracking(digits, combination):
        if not digits:
            combinations.append(combination)
            return

        for c in phone[digits[0]]:
            backtracking(digits[1:], combination+c)

    if not digits:
        return combinations
    backtracking(digits, "")
    return combinations

print(letterCombinations("2"))