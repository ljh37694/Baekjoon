import sys

cnt = int(sys.stdin.readline())

max_num = 100_000

dp = [[0] * 4 for _ in range(max_num + 1)]

dp[1][1] = 1; dp[2][2] = 1; dp[3] = [0, 1, 1, 1]

for i in range(4, max_num + 1):
    dp[i][1] = dp[i - 1][2] + dp[i - 1][3]
    dp[i][2] = dp[i - 2][1] + dp[i - 2][3]
    dp[i][3] = dp[i - 3][1] + dp[i - 3][2]

    for j in range(1, 4):
        dp[i][j] %= 1_000_000_009

for _ in range(cnt):
    n = int(sys.stdin.readline())

    print(sum(dp[n]) % 1_000_000_009)