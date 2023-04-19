N = int(input())
S = [input() for _ in range(N)]

a = [50]*26
ans = ""
for i in range(26):
    c = chr(i + ord('a'))
    for j in range(N):
        a[i] = min(a[i], S[j].count(c))
    ans += c*a[i]

# 最小値を出力
print("".join(sorted(list(ans))))
