A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

for y in range(len(A)):
    for x in range(len(A[y])):
        for b in B:
            if A[y][x] == b:
                A[y][x] = 0

ans = \
    A[0][0] + A[0][1] + A[0][2] == 0 or \
    A[1][0] + A[1][1] + A[1][2] == 0 or \
    A[2][0] + A[2][1] + A[2][2] == 0 or \
    A[0][0] + A[1][0] + A[2][0] == 0 or \
    A[0][1] + A[1][1] + A[2][1] == 0 or \
    A[0][2] + A[1][2] + A[2][2] == 0 or \
    A[0][0] + A[1][1] + A[2][2] == 0 or \
    A[0][2] + A[1][1] + A[2][0] == 0

print("Yes") if ans else print("No")
