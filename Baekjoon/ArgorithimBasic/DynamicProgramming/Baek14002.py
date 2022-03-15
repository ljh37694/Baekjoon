# 14002 : 가장 긴 증가하는 부분 수열 4

import sys

n = int(sys.stdin.readline())
arr = [-1] + list(map(int, sys.stdin.readline().split()))

dp = [[1, [arr[i]]] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if arr[i] > arr[j]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = dp[j][1] + [arr[i]]

idx = dp.index(max(dp))
print(dp[idx][0])
print(*dp[idx][1])