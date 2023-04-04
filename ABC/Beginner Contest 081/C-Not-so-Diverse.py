from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

dic = defaultdict(int)
for a in A:
    dic[a] += 1

vals = [dic[k] for k in dic]
vals.sort()
print(sum(vals[: max(0, len(vals) - K)]))
