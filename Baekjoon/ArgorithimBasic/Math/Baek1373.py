# 1373 : 2진수 8진수

"""
num = int(input(), 2)
print(oct(num)[2:])
"""

num = input()[::-1]
num += '0' * (3 - len(num) % 3) if len(num) % 3 != 0 else num
answer = ""

for i in range(0, len(num), 3):
    cnt = 0
    for j in range(3):
        if num[i + j] == '1':
            cnt += 2 ** j
    answer = str(cnt) + answer

print(answer)