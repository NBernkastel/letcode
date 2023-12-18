asteroids = [-2, -1, 1, 2]


def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
        else:
            while stack and stack[-1] > 0:
                top = stack.pop()
                if top == -asteroid:
                    break
                elif top > -asteroid:
                    stack.append(top)
                    break
            stack.append(asteroid)
    return stack


print(asteroidCollision(asteroids))
