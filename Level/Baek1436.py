n = int(input())

cnt = 0
check = 666

while True:
    if "666" in str(check):
        cnt += 1

    if n == cnt:
        print(check)
        break

    check += 1