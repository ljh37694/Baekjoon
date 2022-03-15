# 11053 : 가장 긴 증가하는 부분 수열

import sys

n = int(sys.stdin.readline())
numbers = [-1] + list(map(int, sys.stdin.readline().split()))


dp = [1] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))