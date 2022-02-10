# 1699 : 제곱수의 합
import sys

n = int(sys.stdin.readline())

dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if i < (j * j):
            break

        if dp[i] > dp[i - (j * j)] + 1:
            dp[i] = dp[i - (j * j)] + 1

print(dp[n])

""" 뭐가 틀린지 모르겠다
import sys
from math import sqrt

n = int(sys.stdin.readline())

dp = [0] * (n + 1)
num = 0

for i in range(1, n + 1):
    # 특정 수의 제곱근의 자연수 여부 판단
    c = sqrt(i)
    if c == int(c):
        dp[i] = 1
        num = i
    else:
        dp[i] = dp[i - num] + 1

print(dp[n])
"""