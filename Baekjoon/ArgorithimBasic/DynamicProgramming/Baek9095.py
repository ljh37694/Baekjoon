import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    dp = [0, 1, 2, 4] + [0] * (num - 3)

    if num < 4:
        print(dp[num])
        continue

    for i in range(1, num + 1):
        if i < 4:
            continue
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[num])