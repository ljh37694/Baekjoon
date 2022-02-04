import sys

def gcd(p, q):
    while q > 0:
        p, q = q, p % q
    return p


def lcm(p, q):
    return p * q // gcd(p, q)


n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))