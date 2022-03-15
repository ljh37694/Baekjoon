import sys

n = int(sys.stdin.readline())

dic = {}

lst = list(map(int, sys.stdin.readline().split()))

check = list(sorted(set(lst)))

for i in range(len(check)):
    dic[check[i]] = i

result = []

for i in lst:
    result.append(str(dic[i]))

print(" ".join(result))