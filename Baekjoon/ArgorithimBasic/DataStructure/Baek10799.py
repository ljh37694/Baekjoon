import sys

stick = sys.stdin.readline().rstrip()
"""
answer = 0
left = 0

for i in range(len(stick)):
    if stick[i] == "(":
        left += 1; answer += 1
    elif stick[i] == ")" and stick[i - 1] == "(":
        left -= 1; answer -= 1
        answer += left
    elif stick[i] == ")":
        left -= 1
else:
    print(answer)
"""

stack = []
answer = 0
for i in range(len(stick)):
    if stick[i] == "(":
        stack.append(stick[i])
    else:
        if stick[i - 1] == "(":
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
else:
    print(answer)