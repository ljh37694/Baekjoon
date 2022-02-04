import math
import sys

a, b = map(int, sys.stdin.readline().split())

"""
m, n = a, b
i, j = a, b

while b != 0:
    if b > a:
        a, b = b, a

    a, b = b, a % b
print(a)

while True:
    if m > n:
        n += j
    elif m < n:
        m += i
    else:
        break

print(m)
"""

def gcd(p, q):
    while q > 0:
        p, q = q, p % q
    return p


def lcm(p, q):
    return p * q // gcd(p, q)

print(gcd(a, b))
print(lcm(a, b))
print(math.gcd(a, b))
print(math.lcm(a, b))