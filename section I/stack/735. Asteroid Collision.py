def asteroidCollision(asteroids):
    stack = []
    for val in asteroids:
        if not stack or val > 0:
            stack += val,
            continue

        while stack and stack[-1]>0:
            if stack[-1] == -val:
                stack.pop()
                val = 0
                break
            elif stack[-1] < -val:
                stack.pop()
            else:
                val = 0
                break

        if val != 0:
            stack += val,

    return stack

asteroids = [2,-1,-2,3,-2,-1,5,-9]
print asteroidCollision(asteroids)

