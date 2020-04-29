def getMinCoins(coins: list, value: int) -> int:
    res = [float('INF')] * (value + 1)
    res[0] = 0
    def dp(i):
        if i == 0: return 0
        if i < 0: return -1
        for coin in coins:
            if dp(i-coin) < 0: continue
            res[i] = min(res[i], dp(i-coin)+1)
        return res[i]
    return dp(value)


def getMaxSeq(raw_seq: list) -> int:
    dp = [1] * len(raw_seq)
    for i, v in enumerate(raw_seq):
        for j, v1 in enumerate(raw_seq[0:i+1]):
            if v > v1:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


def getMaxBagValue(goods: list, wt: int) -> int:
    dp = [[0 for m in range(wt+1)]for k in range(len(goods)+1)]
    for i in range(1,len(goods)+1):
        for j in range(1, wt+1):
            if (j-goods[i-1][0]) < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-goods[i-1][0]] + goods[i-1][1])
    return dp[len(goods)][wt]


def getMaxSubSeq(seq: list):
    dp = [0] * (len(seq) + 1)
    dp[1] = seq[0]
    for i in range(2, len(seq)+1):
        if dp[i-1] >= 0:
            dp[i] = dp[i-1] + seq[i-1]
        else:
            dp[i] = seq[i-1]
    return max(dp)


def getEditDistance(s1: str, s2: str):
    dp = [[0 for _ in range(len(s2)+1)] for __ in range(len(s1)+1)]
    for i in range(len(s1)+1):
        dp[i][0] = i
    for j in range(len(s2)+1):
        dp[0][j] = j
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    return dp[len(s1)][len(s2)]


if __name__ == '__main__':
    print(getEditDistance('rad', 'apple'))