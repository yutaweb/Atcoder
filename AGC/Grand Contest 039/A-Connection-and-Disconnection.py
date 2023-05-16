"""
S：入力文字列
K：Sを繰り返す回数
T：SをK買い繰り返して出来る文字列
境界値が
①異なる
　→ 特に考慮する事項なし
②同じ
　→ （K - 1）* 隣接要素の除去 - (K * Sの最初の文字列の隣接要素の除去 + K * Sの後半~）
"""
S = input()
K = int(input())

N = len(S)

i = 0
ans = 0
while i < N:
    j = i
    while j < N and S[i] == S[j]:
        j += 1
        if i == 0:
            start = j
        elif j == N:
            finish = (j - i)
    ans += (j - i) // 2
    i = j

if start == N:
    exit(print(N * K // 2))
else:
    ans *= K
    # 境界値が同じ&1文字で構成されていない場合
    if S[0] == S[-1] and start != N:
        ans += (K - 1) * ((start + finish) // 2 - start // 2 - finish // 2)

print(ans)
