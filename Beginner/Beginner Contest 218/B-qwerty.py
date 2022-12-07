import string


P = list(map(int, input().split()))
alphabet = string.ascii_lowercase

ans = ''
for i in P:
    ans += alphabet[i - 1]

print(ans)
