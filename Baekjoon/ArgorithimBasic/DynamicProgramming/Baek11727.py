import sys

n = int(sys.stdin.readline())

num = [1, 2]
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        dp[i] = 1
        continue
    elif i == 2:
        dp[i] = 3
        continue
    dp[i] = dp[i - 2] * 2 + dp[i - 1]

print(dp[n] % 10_007)