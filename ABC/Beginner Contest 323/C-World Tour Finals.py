N, M = map(int, input().split())
A = list(map(int, input().split()))

Players = [list(input()) for _ in range(N)]

P = [0] * N
A_list = [[0 for _ in range(M)] for _ in range(N)]  # [A] * N のように配列を初期化すると、参照がN行分コピーされるだけなので、意味がない
for i, Player in enumerate(Players):
    for j, judge in enumerate(Player):
        if judge == "o":
            P[i] += A[j]
        else:
            A_list[i][j] += A[j]
    P[i] += (i + 1)

for i, p in enumerate(P):
    A_list[i].sort(reverse=True)
    tmp = p
    ans = 0
    while tmp < max(P):
        tmp += A_list[i][ans]
        ans += 1
    print(ans)
