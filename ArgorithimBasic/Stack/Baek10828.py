import sys

n = int(sys.stdin.readline())

lst = []
stack = []

for _ in range(n):
    command = input()
    lst.append(command)

for c in lst:
    if "push" in c:
        p, n = c.split()
        stack.append(n)
    elif c == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif c == "size":
        print(len(stack))
    elif c == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif c == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)