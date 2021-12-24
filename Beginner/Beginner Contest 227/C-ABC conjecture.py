import itertools

count = 0
N = int(input())
L = list(itertools.combinations(range(N), 3))
for val in L:
    if N <= sum(val):
        count += 1

print(count)

#  方針①
#  1.全通りの組み合わせを考える
#  2.1の中から条件に合致するpatternを抽出する