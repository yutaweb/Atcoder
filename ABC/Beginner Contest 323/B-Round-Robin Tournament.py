N = int(input())
S = {i + 1: input().count('o') for i in range(N)}

sorted_S = sorted(S.items(), key=lambda item: item[1], reverse=True)

ans = []
for item in sorted_S:
    ans.append(item[0])

print(*ans)
