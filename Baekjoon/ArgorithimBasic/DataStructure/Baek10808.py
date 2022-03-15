# 10808 : 알파벳 개수
import sys

word = sys.stdin.readline().rstrip()
answer = [0] * 26

for i in word:
    answer[ord(i.lower()) - 97] += 1

print(*answer)