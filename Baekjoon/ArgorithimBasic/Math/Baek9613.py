# 9613 : GCD 합
import sys

n = int(sys.stdin.readline())

# 유클리드 호제법
# b와 a % b의 최대공약수가 a와 b의 최대공약수가 같음
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(n):
    numbers = list(map(int, sys.stdin.readline().split()))
    answer = 0

    for i in range(1, numbers[0]):
        for j in range(i + 1, numbers[0] + 1):
            num1, num2 = numbers[i], numbers[j]
            answer += gcd(num1, num2) if num1 > num2 else gcd(num2, num1)
    print(answer)