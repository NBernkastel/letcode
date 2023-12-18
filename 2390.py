import cProfile

s = "leet**cod*e"


def removeStars(s: str) -> str:
    res = []
    for c in s:
        if c == '*':
            res.pop()
        else:
            res.append(c)
    return ''.join(res)


print(cProfile.run('removeStars(s)'))
print(removeStars(s))
