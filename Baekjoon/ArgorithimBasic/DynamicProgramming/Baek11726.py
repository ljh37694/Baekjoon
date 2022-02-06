import sys

n = int(sys.stdin.readline())

num = [1, 2, 3]
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i in num:
        dp[i] = i
        continue
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n] % 10_007)
"""
import sys

num = int(sys.stdin.readline())

# 조합을 반환하는 함수
def combination(n, r):
    result = 1
    if r == 0:
        return result

    for j in range(r):
        result *= n - j
    for j in range(r):
        result //= (j + 1)
    return result

one_x_two = num # 1x2 타일의 개수
two_x_one = 0 # 2x1 타일의 개수

answer = 1
while True:
    two_x_one += 1
    one_x_two -= 2
    if one_x_two < 0:
        break
    answer += combination(one_x_two + two_x_one, one_x_two)

print(answer % 10_007)
"""
