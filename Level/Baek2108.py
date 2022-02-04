import sys
from collections import Counter

n = int(sys.stdin.readline())

lst = [0] * 8001
numbers = []
result = {"average" : 0, "middle" : 0, "frequent" : 0, "range" : 0}

for _ in range(n):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers.sort()
set_numbers = set(numbers)

result["average"] = round(sum(numbers) / len(numbers))
result["middle"] = numbers[(len(numbers) - 1) // 2]
result["range"] = numbers[-1] - numbers[0]

frequent = Counter(numbers).most_common()

if len(frequent) == 1:
    result["frequent"] = frequent[0][0]
elif frequent[0][1] == frequent[1][1]:
    result["frequent"] = frequent[1][0]
else:
    result["frequent"] = frequent[0][0]

for i in result:
    print(result[i])