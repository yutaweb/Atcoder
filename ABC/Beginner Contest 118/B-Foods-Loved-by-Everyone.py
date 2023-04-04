from collections import defaultdict

N, M = map(int, input().split())

KA = [list(map(int, input().split())) for _ in range(N)]
if N == 1:
    exit(print(KA[0][0]))

duplicate = defaultdict(int)
for ka in KA:
    for i in range(1, ka[0] + 1):
        duplicate[ka[i]] += 1

ans = 0
for d in duplicate:
    if duplicate[d] == N:
        ans += 1

print(ans)
