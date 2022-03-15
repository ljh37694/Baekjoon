# 10820 : 문자열 분석
import sys

check = True

while check:
    lower, upper, num, blank = 0, 0, 0, 0
    text = sys.stdin.readline().rstrip("\n")

    if not text:
        check = False
        break

    # 아스키 코드를 이용할 수 있음
    for i in text:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            num += 1
        else:
            blank += 1

    print(lower, upper, num, blank)