import itertools

N, M = map(int, input().split())
cond = [tuple(map(int, input().split())) for i in range(N)]
K = int(input())
choice = [tuple(map(int, input().split())) for i in range(K)]
ans = 0
for num in itertools.product(*choice):
    num = set(num)
    cnt = sum(A in num and B in num for A, B in cond)
    if ans < cnt:
        ans = cnt

print(cnt)