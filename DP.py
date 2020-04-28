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


if __name__ == '__main__':
    print(getMaxBagValue([(2,4), (1,2), (3,3)], 4))