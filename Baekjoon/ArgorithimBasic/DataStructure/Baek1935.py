import sys

n = int(sys.stdin.readline())

formula = sys.stdin.readline().rstrip()
op = []
numbers = [int(sys.stdin.readline()) for i in range(n)]
stack = []

def calc(operator, a, b):
    if operator == "+":
        a += b
    elif operator == "-":
        a -= b
    elif operator == "*":
        a *= b
    else:
        a /= b
    return a

for i in formula:
    if i.isupper():
        stack.append(numbers[ord(i) - ord("A")])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(calc(i, num1, num2))

print("{:.2f}".format(stack[-1]))