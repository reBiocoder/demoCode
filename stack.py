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


def getAllCol(n: int) -> list:
    res = []

    def backTracks(exit_seq: str, select_list: list):
        if len(exit_seq) == n:
            res.append(exit_seq)
            return
        else:
            for i in select_list:
                if exit_seq.find(str(i)) == -1:
                    backTracks(exit_seq + str(i), select_list)
    backTracks('', [i for i in range(1, n+1)])
    return res


def n_queen(nums: int) -> int:
    res = []

    def isValid(exit_seq: str, index: int) -> bool:
        exit_len = len(exit_seq)
        for i in range(exit_len):
            if abs(index - int(exit_seq[i])) in (0, exit_len - i):
                return True
        return False

    def backTracks(exit_seq: str, select_list: list):
        if len(exit_seq) == nums:
            res.append(exit_seq)
            return
        else:
            for i in select_list:
                tmp_res = isValid(exit_seq, i)
                if tmp_res is False:
                    backTracks(exit_seq+str(i), select_list)

    backTracks('', [i for i in range(1, nums+1)])
    return len(res)


def getAllSubSet(nums: list):
    res = []

    def backTracks(exit_list: list, index: int):
        if len(exit_list) <= len(nums):
            res.append(exit_list)

        for i in range(index, len(nums)):
            backTracks(exit_list+[nums[i]], i+1)

    backTracks([], 0)
    return res


def getCombine(nums: list, k: int):
    res = []

    def backTracks(exit_list: list, index: int):
        if len(exit_list) == k:
            res.append(exit_list)
            return
        else:
            for i in range(index, len(nums)):
                backTracks(exit_list+[nums[i]], i+1)

    backTracks([], 0)
    return res


if __name__ == '__main__':
    print(getAllSubSet([1,2,3]))
    print(getCombine([1,2,3,4,], 2))
