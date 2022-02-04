import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
answer = []
cnt = 0

for i in lst:
    if i == 1:
        continue

    for j in range(2, i):
        if i % j == 0:
            break
    else:
        answer.append(i)

print(len(answer))