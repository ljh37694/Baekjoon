def combination(n, r):
    result = 1
    for j in range(r):
        result *= n - j
    for j in range(r):
        result //= (j + 1)
    return result

print(combination(9, 2))