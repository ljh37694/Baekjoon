def get_stars(n):
    matrix = []

    for i in range(len(n) * 3):
        if i //len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)

    return matrix

stars = ["***", "* *", "***"]

n = int(input())
count = 0

while n != 3:
    n //= 3
    count += 1

for _ in range(count):
    stars = get_stars(stars)

for j in stars:
    print(j)