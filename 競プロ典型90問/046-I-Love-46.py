# 計算量：O(N)には収められる
from collections import Counter


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(N):
    A[i] = A[i] % 46
    B[i] = B[i] % 46
    C[i] = C[i] % 46

cnt_A = Counter(A)
cnt_B = Counter(B)
cnt_C = Counter(C)

ans = 0
for item_a in cnt_A.items():
    for item_b in cnt_B.items():
        for item_c in cnt_C.items():
            if (item_a[0] + item_b[0] + item_c[0]) % 46 == 0:
                ans += item_a[1] * item_b[1] * item_c[1]

print(ans)
