"""
import sys

n = int(sys.stdin.readline())

answer = 0
for i in range(10 ** (n - 1), 10 ** n):
    num = str(i)
    if len(num) == 0:
        answer += 1
        continue

    for j in range(len(num) - 1):
        if abs(int(num[j]) - int(num[j + 1])) != 1:
            break
    else:
        answer += 1

print(answer % 1_000_000_000)
"""
import sys

num = int(sys.stdin.readline())

# 2차원 배열 dp[i][j]에서 i는 숫자의 자리, j는 0~9
dp = [[0] * 10 for _ in range(num + 1)]

# 한 자리일 때, 숫자가 한개만 사용되기 때문에 모두 1
# 0으로 시작하는 것은 계단수가 아니므로 제외
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, num + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j - 1]

print(sum(dp[num]) % 1_000_000_000)