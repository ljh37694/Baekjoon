import sys

word = sys.stdin.readline()[:-1]
n = int(input())

stack1 = list(word)
stack2 = []

for _ in range(n):
    command = sys.stdin.readline()[:-1]

    if command == "L":
        if not stack1:
            continue
        stack2.append(stack1.pop())

    elif command == "D":
        if not stack2:
            continue
        stack1.append(stack2.pop())

    elif command == "B":
        if not stack1:
            continue
        stack1.pop()

    else:
        c, w = command.split()
        stack1.append(w)
print("".join(stack1 + stack2[::-1]))