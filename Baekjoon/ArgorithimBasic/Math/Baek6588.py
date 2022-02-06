"""
import sys

lst = [2] # 짝수를 배제하기 떄문에 짝수인 2만 넣음
# 효율성을 위해 범위 내의 소수를 구함
for i in range(3, 1_000_001, 2):
    for j in lst:
        if i % j == 0: # 소수인지 아닌지 판별
            break

        elif (i ** 0.5) < j: # 약수를 구할 때 그 수의 제곱근까지만 확인하면 됨
            lst.append(i)
            break

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    check = False
    for i in range(len(lst)):
        for j in lst[i + 1:]:
            num = n - lst[i]
            if num == j:
                print("{} = {} + {}".format(n, lst[i], num))
                check = True
                break
            elif j > num:
                break
        if check:
            break
"""
import sys

# 에라토스테네스의 체를 이용
lst = [True] * 1_000_001

# 2부터 시작해 특정 수의 배수에 해당하는 모든 수를 False
for i in range(2, 1001):
    if lst[i]:
        for j in range(i + i, 1_000_001, i): # i를 제외한 모든 i의 배수를 False
            lst[j] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    for i in range(3, n - 2): # i가 n보다 크면 안되기 때문에 (3, n - 2)
        if lst[i] and lst[n - i]: # i와 n - i가 소수일 때 해당 값 출력
            print(n, '=', i, '+', n - i)
            break