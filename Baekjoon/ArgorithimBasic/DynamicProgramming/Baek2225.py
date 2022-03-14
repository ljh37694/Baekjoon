# 2225 : 합분해
import sys

n, k = map(int, sys.stdin.readline().split())

dp = [1] + [0] * n

for _ in range(1, k + 1):
    for i in range(1, n + 1):
        dp[i] = (dp[i] + dp[i - 1]) % 1_000_000_000

print(dp[n])
"""
dp = [[0] * (n + 1) for _ in range(k + 1)] # dp[k][n]

for i in range(n + 1):
    dp[1][i] = 1
    dp[2][i] = i + 1

for i in range(2, k + 1):
    for j in range(2, n + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1_000_000_000

print(dp[k][n])
"""