# 2480 : 주사위 세개

dice = list(map(int, input().split()))

set_dice = set(dice)

max_num = 0
num = 0

for i in set_dice:
    cnt = dice.count(i)
    if cnt > 1:
        max_num = cnt
        num = i
        break
else:
    num = max(dice)

if max_num == 3:
    print(10000 + num * 1000)
elif max_num == 2:
    print(1000 + num * 100)
else:
    print(num * 100)