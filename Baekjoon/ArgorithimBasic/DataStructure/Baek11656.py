# 11656 : 접미사 배열

# 이것도 파이썬으로 풀기 쉽다
answer = []

text = input()

for i in range(len(text)):
    answer.append(text[i:])

for i in sorted(answer):
    print(i)