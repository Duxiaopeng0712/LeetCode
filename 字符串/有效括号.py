def isValid(self, s: str) -> bool:
    kuohao = {')': '(', '}': '{', ']': '['}
    stack = []

    for i in s:
        if i not in kuohao:
            stack.append(i)
        elif len(stack) == 0 or kuohao[i] != stack.pop():
            return False

    return len(stack) == 0
