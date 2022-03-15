import sys

n = int(sys.stdin.readline())

stack = []
result = []
cnt = 1
check = 0

for _ in range(n):
    num = int(sys.stdin.readline())

    while cnt <= num:
        stack.append(cnt)
        result.append("+")
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        check = True
else:
    if check:
        print("NO")
    else:
        for i in result:
            print(i)