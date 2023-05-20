import itertools
import numpy as np

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

S = np.array(S)
tmp = [i for i in range(N)]

for ies in itertools.permutations(tmp, N):
    cnt = 0
    for i, v in enumerate(ies):
        if i == N - 1:
            continue
        judge = (S[v] == S[i + 1])
        if list(judge).count(True) == (M - 1):
            cnt += 1

    if cnt == N - 1:
        exit(print("Yes"))

print("No")
g