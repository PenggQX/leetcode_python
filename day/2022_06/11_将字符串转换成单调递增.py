class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ilen = len(s)
        dp = [[0, 0] for _ in range(ilen)]

        # 初值
        if s[0] == '0':
            dp[0][1] = 1
        else:
            dp[0][0] = 1

        for i in range(1, ilen):
            if s[i] == '0':
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = 1 + min(dp[i - 1][0], dp[i - 1][1])
            else:
                dp[i][0] = 1 + dp[i - 1][0]
                dp[i][1] = min(dp[i - 1][0], dp[i - 1][1])

        return min(dp[-1][0], dp[-1][1])
