# 2525 : 오븐 시계

hour, minute = map(int, input().split())
time = int(input())

minute += time

if minute >= 60:
    hour += minute // 60
    minute %= 60

    if hour >= 24:
        hour -= 24

print("{} {}".format(hour, minute))