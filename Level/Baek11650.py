n = int(input())

lst = []

for i in range(n):
    x, y = map(int, input().split())

    lst += [(x, y)]

for i in sorted(lst):
    print(i[0], i[1])