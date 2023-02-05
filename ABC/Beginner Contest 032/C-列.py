"""
S内の要素の積がK以下
→ 尺取り法で求める
"""

N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
    exit(print(N))

right = 0
temp = 1
res = 0
for left in range(N):
    while right < N and temp * S[right] <= K:
        temp *= S[right]
        right += 1
    res = max(res, right - left)
    if right == left:
        right += 1
    else:
        temp /= S[left]
