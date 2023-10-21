N = int(input())

while N % 2 == 0:
    tmp = divmod(N, 2)
    N = tmp[0]

while N % 3 == 0:
    tmp = divmod(N, 3)
    N = tmp[0]

if N == 1:
    print("Yes")
else:
    print("No")
