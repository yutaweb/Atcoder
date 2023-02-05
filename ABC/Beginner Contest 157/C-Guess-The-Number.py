# 上手に全探索する
N, M = map(int, input().split())
ans = [0]*N


for _ in range(M):
    s, c = map(int, input().split())
    if s == 1 and c == 0:
        if N == 1:
            print(0)
        else:
            print(-1)
        exit()

    if ans[s-1] != 0 and ans[s-1] != c:
        print(-1)
        exit()

    if ans[s-1] > c or ans[s-1] == 0:
        ans[s-1] = c


if M == 0:
    if N == 1:
        ans[0] = 0
    else:
        ans[0] = 1
else:
    if ans[0] == 0:
        ans[0] = 1

print(*ans, sep='')
