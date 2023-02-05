import numpy as np


N, X = map(int, input().split())

counter = 0
M = []
for _ in range(N):
    m = int(input())
    M.append(m)

M.sort()

if X - np.sum(M) > 0:
    X -= np.sum(M)
    counter += len(M)

counter += X // M[0]

print(counter)

