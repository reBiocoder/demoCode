
def isMatched(s: str) -> bool:
    def isExited(p: str) -> str:
        if p == '}': return '{'
        if p == ')': return '('
        else: return '['

    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            if len(stack) != 0 and stack.pop() == isExited(i):
                continue
            else:
                return False
    return True


if __name__ == '__main__':
    print(isMatched('[{(})]'))