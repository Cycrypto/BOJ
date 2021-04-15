# import itertools
# # # def sk(dics, k):
# # #     for i in dics[k]:
# # #         if len(dics[k]) != 0:
# # #             return dics[k]
# # #         else:
# # #             sk()
# # #
# # # def main():
# # #     skill = input().split(' ')
# # #     skill_set = {}
# # #     for i in skill:
# # #         skill_set[i] = list()
# # #     relations = int(input())
# # #
# # #     for i in range (relations):
# # #         n, s = input().split(' ')
# # #         skill_set[n].append(s)
# # #     print(skill_set)
# # #     first = list(skill_set.keys())[0]
# # #     print(sk(skill_set, first))
# #
# # def main():
# #     skill = input().split(' ')
# #     skill_set = {}
# #     for i in skill:
# #         skill_set[i] = list()
# #     relations = int(input())
# #
# #     for i in range (relations):
# #         n, s = input().split(' ')
# #         skill_set[n].append(s)
# #
# #     comb = []
# #     for j in skill_set.values():
# #         if j != []:
# #             comb.append(j)
# #     print(list((itertools.combinations(comb,1))))
# # if __name__ == "__main__":
# #     main()
import itertools
def main():
    p,n,h = input().split(' ')


    com = [[]for _ in range(int(p))]
    for i in range(int(n)):
        inp = input().split()
        com[int(inp[0]) - 1].append(inp[1])

    for u,i in enumerate(com):
        m = 0
        for j in range(1, len(i) + 1):
            for k in list(itertools.combinations(i,j)):
                k = list(map(int, k))
                if sum(k) <= int(h):
                    if sum(k) > m:
                        m = sum(k)
                    else:
                        continue
                else:
                    continue
        print(u+1, m * 1000)


if __name__ == "__main__":
    main()