s = "3[a2[c]]"
re = "accaccacc"


def decodeString(s: str) -> str:
    stack = []
    for char in s:
        if char == "]":
            val = stack.pop()
            item = ""
            while stack and not str(val).isnumeric():
                item = val + item if val != "[" else item
                val = stack.pop()
            number = val
            while stack and str(stack[-1]).isnumeric():
                number = stack.pop() + number
            [stack.append(item) for _ in range(int(number))]
        else:
            stack.append(char)
    return "".join(stack)


print(decodeString(s))
s.isdigit()