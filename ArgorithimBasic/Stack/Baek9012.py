n = int(input())

lst = []

for _ in range(n):
    ps = input()
    lst.append(ps)

for i in lst:
    cnt = 0
    for j in i:
        if j == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            print("NO")
            break
    else:
        if cnt == 0:
            print("YES")
        else:
            print("NO")
