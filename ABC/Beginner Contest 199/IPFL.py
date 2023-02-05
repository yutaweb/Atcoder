N = int(input())
S = input()
S_list = list(S)
Q = int(input())
query = []
stash = ''
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        stash = S_list[query[1] - 1]
        S_list[query[1] - 1] = S_list[query[2] - 1]
        S_list[query[2] - 1] = stash
    elif query[0] == 2:
        stash = S_list[N:]
        S_list[N:] = S_list[:N]
        S_list[:N] = stash

ans = ''.join(S_list)
print(ans)

