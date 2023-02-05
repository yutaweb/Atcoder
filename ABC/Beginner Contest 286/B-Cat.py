N = int(input())
S = input()

ans = ''
i = 0
while True:
    if i > len(S) - 1:
        break

    if S[i:i+2] == 'na':
        ans += 'nya'
        i += 2
    else:
        ans += S[i]
        i += 1

print(ans)
