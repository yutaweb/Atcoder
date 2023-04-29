# ->< ←規約の問題でファイル名に反映できなかった

S = input()
N = len(S) + 1

tmp = [0] * N

for i in range(N-1):
    if S[i] == "<":
        tmp[i+1] = tmp[i] + 1

j = 1
for i in reversed(range(N-1)):
    if S[i] == ">":
        tmp[i] = max(tmp[i], j)
        j += 1
    else:
        j = 1

ans = sum(tmp)
print(ans)
