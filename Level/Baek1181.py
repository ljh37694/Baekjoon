n = int(input())

dic = {}

for i in range(n):
    word = input()
    if len(word) not in dic:
        dic[len(word)] = [word]
    else:
        dic[len(word)] += [word]


sorted_dic = dict(sorted(dic.items()))



for k, v in sorted_dic.items():
    if len(v) > 1:
        sorted_dic[k] = sorted(set(v))

for i in sorted_dic:
    for j in sorted_dic[i]:
        print(j)