N, D = map(int, input().split())

XD = [list(map(int, input().split())) for _ in range(N)]


def calc(a, b):
    r = 0
    for d in range(D):
        r += (XD[a][d] - XD[b][d]) ** 2
    return r ** 0.5


counter = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if calc(i, j) % 1 == 0:
            counter += 1

print(counter)
