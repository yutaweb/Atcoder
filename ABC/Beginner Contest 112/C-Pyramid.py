N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
D.sort(reverse=True, key=lambda d: d[2])

for Cx in range(101):
    for Cy in range(101):
        flag = False
        for x, y, h in D:
            if h > 0:
                if flag is False:
                    H = abs(x - Cx) + abs(y - Cy) + h
                    flag = True
                else:
                    if H != abs(x - Cx) + abs(y - Cy) + h:
                        break
            else:
                if flag is True:
                    if H > abs(Cx - x) + abs(Cy - y):
                        break
        else:
            if flag is True:
                print(Cx, Cy, H)
