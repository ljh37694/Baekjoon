import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().rstrip().split()))

stack = []
answer = [-1] * n
cnt_num = {}
for i in seq:
    if i in cnt_num:
        cnt_num[i] += 1
    else:
        cnt_num[i] = 1

for i in range(n):
    while stack and cnt_num[seq[i]] > cnt_num[stack[-1][0]]:
        num, idx = stack.pop()
        answer[idx] = seq[i]
    stack.append((seq[i], i))

print(*answer)