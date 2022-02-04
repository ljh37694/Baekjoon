import sys

n = int(sys.stdin.readline())

lst = []

for _ in range(n):
    command = sys.stdin.readline().strip()

    if "push" in command:
        c, n = command.split()
        lst.append(int(n))
    elif command == "pop":
        if lst:
            print(lst.pop(0))
        else:
            print(-1)
    elif command == "size":
        print(len(lst))
    elif command == "empty":
        if lst:
            print(0)
        else:
            print(1)
    elif command == "front":
        if lst:
            print(lst[0])
        else:
            print(-1)
    elif command == "back":
        if lst:
            print(lst[-1])
        else:
            print(-1)
    # print(lst)