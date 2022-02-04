n = input()
lst = []

for i in n:
    lst.append(i)

result = sorted(lst)
num = 0

for i in range(len(result)):
    num += int(result[i]) * (10 ** i)

print(num)