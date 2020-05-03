def canJump(nums: list) -> bool:
    seq_len = len(nums)
    ret = 0  # 初始索引为0
    for i in range(seq_len):
        if ret >= i:  # 当前能够达到的最远距离必须要大于循环到的索引
            ret = max(ret, i + nums[i])
        else:
            return False
    return True


def canMinJump(nums: list) -> int:
    seq_len = len(nums)
    ret, end = 0, 0
    step = 0
    for i in range(seq_len-1):
        if ret >= i:
            ret = max(ret, i+nums[i])
            if i == end:
                step += 1
                end = ret
        else:
            return - 1
    return step


def eraseOverlapIntervals(interval: list):
    interval.sort(key=lambda x: x[1])
    count = 1
    x_end = interval[0][1]
    for i in range(1, len(interval)):
        if interval[i][0] > x_end:
            count += 1
            x_end = interval[i][1]
    return count


def merge(intervals: list) -> list:
    intervals.sort(key=lambda x: x[0])  # 按照左端点来进行排序
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        last = res[-1]
        if last[1] >= intervals[i][0]:
            last[1] = max(last[1], intervals[i][1])
        else:
            res.append(intervals[i])

    return res


def intervalSection(A:list, B:list) -> list:
    i, j = 0, 0
    res = []
    while i < len(A) and j < len(B):
        a1, a2 = A[i][0], A[i][1]
        b1, b2 = B[j][0], B[j][1]
        if b2 >= a1 and a2 >= b1:
            res.append([max(a1, b1), min(a2, b2)])
        if b2 < a2:
            j += 1
        else:
            i += 1
    return res


if __name__ == '__main__':
    print(intervalSection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]))
