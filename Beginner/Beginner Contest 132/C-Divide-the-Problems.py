N = int(input())
D = list(map(int, input().split()))

D.sort()

first_medium_num = int(N/2-1)
last_medium_num = int(N/2)

first_medium = D[first_medium_num]
last_medium = D[last_medium_num]

ans = 0
if first_medium != last_medium:
    while last_medium - first_medium > 0:
        ans += 1
        last_medium -= 1
else:
    ans = 0

print(ans)
