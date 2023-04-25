# 連長圧縮（ランレングス圧縮）
s = input()

ans = ""
i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
        j += 1

    ans += s[i] + str(j-i)
    i = j

print(ans)
