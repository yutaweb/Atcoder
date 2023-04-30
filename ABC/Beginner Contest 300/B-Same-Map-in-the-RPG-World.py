import numpy as np

H, W = map(int, input().split())

A = []
B = []

for _ in range(H):
    A.append(list(input()))

for _ in range(H):
    B.append(list(input()))

A = np.array(A)
B = np.array(B)

ans = ""
for _ in range(H):
    # 縦方向の操作
    A = np.insert(A, H, A[0], axis=0)
    A = np.delete(A, 0, axis=0)
    for _ in range(W):
        # 横方向の操作
        A = A.T
        A = np.insert(A, W, A[0], axis=0)
        A = np.delete(A, 0, axis=0)
        A = A.T

        # # A, B比較
        if np.all(A == B):
            exit(print("Yes"))

print("No")
