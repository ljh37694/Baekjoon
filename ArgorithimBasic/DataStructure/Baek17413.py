import sys

string = sys.stdin.readline().rstrip()

check = False
word = ''
result = ''

for s in string:
    if s == "<":
        result += word + s
        word = ""
        check = True
    elif s == ">":
        result += s
        check = False
    elif s == " ":
        result += word + s
        word = ""
    else:
        if check:
            result += s
        else:
            word = s + word
else:
    result += word

print(result)