# N, K = map(int, input().split())
# g1 = 0
# g2 = 0
#
# def carr(num):
#     g_b = list(str(num))
#     g1_st = sorted(g_b,reverse=True)
#     g2_st = sorted(g_b)
#     g1_ji = "".join(g1_st)
#     g2_ji = "".join(g2_st)
#     return int(g1_ji) - int(g2_ji)
#
# for k in range(K):
#     N = carr(N)
#
# print(N)
#

def g1(n):
    return int("".join(sorted(str(n), reverse=True)))


def g2(n):
    return int("".join(sorted(str(n))))


def f(n):
    return g1(n)-g2(n)


N, K = map(int, input().split())
for _ in range(N):
    N = f(N)

print(N)