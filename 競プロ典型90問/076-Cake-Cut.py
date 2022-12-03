# https://qiita.com/drken/items/ecd1a472d3a0e7db8dce
# https://nashidos.hatenablog.com/entry/2020/02/02/165319

N = int(input())
A = list(map(int, input().split()))

all_num = sum(A)

if all_num % 10 != 0:
    exit(print('No'))

A += A
now, j = all_num, 0
all_num //= 10
for i in range(N, N*2):
    now += A[i]
    while now > all_num:
        now -= A[j]
        j += 1
    if now == all_num:
        exit(print("Yes"))

print("No")

