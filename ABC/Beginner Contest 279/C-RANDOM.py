import collections

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]

S = collections.Counter(zip(*S))
T = collections.Counter(zip(*T))
if S == T:
    print("Yes")
else:
    print("No")
