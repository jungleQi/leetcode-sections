class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        def operation(op, second, first):
            if op == "+":
                return first + second
            elif op == "-":
                return first - second
            elif op == "*":
                return first * second
            elif op == "/":  # integer division
                return first // second

        def precedence(current_op, op_from_ops):
            if op_from_ops == "(" or op_from_ops == ")":
                return False
            if (current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
                return False
            return True

        if not s:
            return 0
        # define two stack: nums to store the numbers and ops to store the operators
        nums, ops = [], []
        i = 0
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
                continue
            elif c.isdigit():
                num = int(c)
                while i < len(s) - 1 and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                nums.append(num)
            elif c == "(":
                ops.append(c)
            elif c == ")":
                # do the math when we encounter a ')' until '('
                while ops[-1] != "(":
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()
            elif c in ["+", "-", "*", "/"]:
                while len(ops) != 0 and precedence(c, ops[-1]):
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.append(c)
            i += 1

        while len(ops) > 0:
            nums.append(operation(ops.pop(), nums.pop(), nums.pop()))

        return nums.pop()