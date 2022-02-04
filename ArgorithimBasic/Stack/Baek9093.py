n = int(input())

lst = []

for _ in range(n):
    sentence = input()
    lst.append(sentence.split())

for i in lst:
    for j in range(len(i)):
        i[j] = i[j][::-1]
    print(" ".join(i))