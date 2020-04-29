
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


def n_queen(nums: int):
    res = []

    def isValid(exit_seq: str, index: int) -> bool:
        exit_len = len(exit_seq)
        for i in range(exit_len):
            if abs(index - int(exit_seq[i])) in (0, exit_len - i):
                return True
        return False

    def backup(exit_seq: str, select_list: list):
        if len(exit_seq) == nums:
            res.append(exit_seq)
            return
        else:
            for i in select_list:
                tmp_res = isValid(exit_seq, i)
                if tmp_res is False:
                    backup(exit_seq+str(i), select_list)
    backup('', [i for i in range(1,9)])
    return res


if __name__ == '__main__':
    print(len(n_queen(8)))
