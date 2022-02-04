import sys

column, row = map(int, sys.stdin.readline().split())

chess = []
lst = []

for _ in range(column):
    colors = sys.stdin.readline()
    chess.append(colors)

for c in range(column - 7):
    for r in range(row - 7):
        cnt1 = 0
        cnt2 = 0
        for i in range(c, c + 8):
            for j in range(r, r + 8):
                if (i + j) % 2 == 0:
                    if chess[i][j] != "W":
                        cnt1 += 1
                    if chess[i][j] != "B":
                        cnt2 += 1
                else:
                    if chess[i][j] != "B":
                        cnt1 += 1
                    if chess[i][j] != "W":
                        cnt2 += 1
        lst += [cnt1, cnt2]

print(min(lst))