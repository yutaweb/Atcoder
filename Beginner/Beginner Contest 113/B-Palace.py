import numpy as np


N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

temp = []
for h in H:
    temp.append(np.abs(A - (T - h * 0.006)))

ans = temp.index(min(temp))
print(ans + 1)
