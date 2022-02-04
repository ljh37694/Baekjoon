import sys

n = int(sys.stdin.readline())
deque = []

for _ in range(n):
    cmd = sys.stdin.readline().strip()

    if "push_front" in cmd:
        c, n = cmd.split()
        deque.insert(0, n)
    elif "push_back" in cmd:
        c, n = cmd.split()
        deque.append(n)
    elif cmd == "pop_front":
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif cmd == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(deque))
    elif cmd == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif cmd == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)