from collections import defaultdict

N = int(input())
S = defaultdict(int)

for _ in range(N):
    S[input()] += 1

S_sorted = sorted(S.items(), key=lambda x: x[1], reverse=True)

ans = []
index = S_sorted[0][1]
for s in S_sorted:
    if index == s[1]:
        ans.append(s[0])

print(*sorted(ans), sep='\n')
