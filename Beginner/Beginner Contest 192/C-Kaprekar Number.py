N, K = map(int, input().split())
g1 = 0
g2 = 0
ans = 0

def carr(num):
    g_b = list(str(num))
    g1_st = sorted(g_b,reverse=True)
    g2_st = sorted(g_b)
    g1_ji = "".join(g1_st)
    g2_ji = "".join(g2_st)
    return int(g1_ji) - int(g2_ji)

for k in range(K):
    if k == 0:
        ans = carr(N)
    else:
        ans = carr(ans)

print(ans)
