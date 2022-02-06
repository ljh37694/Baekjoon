import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

def count_two(num):
    result = 0
    while num != 0:
        num //= 2
        result += num
    return result

def count_five(num):
    result = 0
    while num != 0:
        num //= 5
        result += num
    return result


cnt_two = count_two(n) - count_two(n - m) - count_two(m)
cnt_five = count_five(n) - count_five(n - m) - count_five(m)

print(min(cnt_two, cnt_five))