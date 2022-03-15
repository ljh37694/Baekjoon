# 왠지 모르겠는데 틀림
"""
import sys

n = int(sys.stdin.readline())
lst = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
dp = [(0.00, 0)] * (n + 1)

for i in range(1, n + 1):
    dp[i] = (lst[i] / i, i)

sorted_dp = sorted(dp, reverse=True)

cnt = 0
answer = 0
while True:
    idx = sorted_dp[cnt][1]
    num = lst[idx]
    if n - idx >= 0:
        n -= idx
        answer += num
    else:
        cnt += 1

    if n == 0:
        break

print(answer)
"""

import sys

n = int(sys.stdin.readline())
card = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * (n + 1)
dp[1] = card[1]
dp[2] = max(card[1] * 2, card[2])

for i in range(3, n + 1):
    dp[i] = card[i]
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[n])