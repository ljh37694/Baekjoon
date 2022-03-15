n = int(input())

lst = []

for i in range(n):
    x, y = map(int, input().split())

    lst += [(y, x)]

for i in sorted(lst):
    print(i[1], i[0])