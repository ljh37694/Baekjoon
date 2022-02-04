import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

def combination(num1, num2):
    answer = 1
    for s in range(num2):
        answer *= num1 - s

    for s in range(num2):
        answer //= num2 - s
    return answer

num2 = 0
num5 = 0

for i in range(n - m):
    if (n - i) % 2 == 0:
        num2 += 1
    elif (n - i) % 5 == 0:
        num5 += 1

for i in range(m):
    if (m - i) % 2 == 0:
        num2 -= 1
    elif (m - i) % 5 == 0:
        num5 -= 1

print(num2, num5)

if num2 > num5:
    print(num5)
else:
    print(num2)