import sys

n = int(input())

result = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline()) # input()의 효율이 별로이기 때문에 input() 대신 사용

    result[num] += 1

for i in range(10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)