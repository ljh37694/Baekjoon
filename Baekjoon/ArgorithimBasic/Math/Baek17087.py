# 17087 : 숨바꼭질 6
import sys

# 좀 더럽게 푼 듯
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n, s = map(int, sys.stdin.readline().split())
position = list(map(int, sys.stdin.readline().split()))
answer = []

for i in range(len(position)):
    position[i] = abs(position[i] - s)

min_num = min(position)
for i in position:
    answer.append(gcd(min_num, i))

print(min(answer))