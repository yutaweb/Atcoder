import functools
import math
import copy

N = int(input())
A = []

for i in range(N):
    M = int(input())
    ai = 1
    for j in range(M):
        base, e = map(int, input().split())
        ai *= base**e
    A.append(ai)


def lcm(a, b):
    """最小公倍数
    :param a:
    :param b:
    :return:
    math.gcd(a, b): 最大公約数
    """
    y = a*b / math.gcd(a, b)
    return int(y)


def lcm_2(*values):
    return functools.reduce(lcm, values)


ans = set([])
for k in range(N):
    temp = copy.copy(A)
    temp[k] = 1
    x = lcm_2(*temp)
    ans.add(x)

print(len(ans))
