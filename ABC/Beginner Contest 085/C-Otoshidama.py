N, Y = map(int, input().split())

# O(N**3)に比例するので、全探索だと良くない
ares, bres, cres = -1, -1, -1

for a in range(N + 1):
    for b in range(N + 1):
        c = N - a - b

        if c < 0 or c > N:
            continue

        if 9000 * a + 4000 * b == Y - 1000 * N:
            ares, bres, cres = a, b, c

print(ares, bres, cres)
