import sys

a, b = map(int, sys.stdin.readline().split())

answer = []

for i in range(a, b + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        answer.append(i)

for i in answer:
    print(i)