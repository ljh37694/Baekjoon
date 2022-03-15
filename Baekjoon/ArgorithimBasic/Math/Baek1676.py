import sys

n = int(sys.stdin.readline())

def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)

cnt = 0
for i in str(factorial(n))[::-1]:
    if i == '0':
        cnt += 1
    else:
        print(cnt)
        break