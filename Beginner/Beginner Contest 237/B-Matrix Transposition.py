import numpy as np

H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

answers = np.array(A).T

for ans in answers:
    print(*ans)