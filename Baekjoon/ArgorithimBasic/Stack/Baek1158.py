import sys

n, k = map(int, sys.stdin.readline().strip().split())

lst = list(range(1, n + 1))
cnt = k - 1
result = []

while len(lst):
    if cnt >= len(lst):
        cnt = cnt % len(lst)
    else:
        result.append(str(lst.pop(cnt)))
        cnt += k - 1

print("<" + ", ".join(result) + ">")