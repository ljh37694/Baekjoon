# 1918 : 후위 표기식

import sys

formula = sys.stdin.readline().rstrip()
result = ""
op = ""
a = ""
check = False

for i in formula:
    if check:
        pass
    if i == ("+" or "-"):
        op += i
    elif i == ("*" or "/"):
        result += i + op
        op = ""
    elif i == "(":
        pass
    else:
        result += i