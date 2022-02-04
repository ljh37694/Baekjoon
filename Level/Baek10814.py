n = int(input())

dic = {}

for i in range(n):
    age, name = map(str, input().split())

    if int(age) not in dic:
        dic[int(age)] = [(name, i)]
    else:
        dic[int(age)] += [(name, i)]

dic = dict(sorted(dic.items()))

for k, v in dic.items():
    if len(v) > 1:
        dic[k] = sorted(v, key=lambda x:x[1])

for k, v in dic.items():
    for i in v:
        print(k, i[0])