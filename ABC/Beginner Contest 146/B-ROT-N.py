import string

N = int(input())
S = input()

alphabet = string.ascii_uppercase
ans = ''

for s in S:
    i = alphabet.index(s)
    ans += alphabet[(i + 1 + N) % len(alphabet) - 1]


print(ans)
