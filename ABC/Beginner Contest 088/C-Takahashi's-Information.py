C = [list(map(int, input().split())) for _ in range(3)]

B = [0]*3
A2 = [0]*3
A3 = [0]*3
for A1 in range(101):
    B[0] = C[0][0] - A1  # b1
    B[1] = C[0][1] - A1  # b2
    B[2] = C[0][2] - A1  # b3

    A2[0] = C[1][0] - B[0]
    A2[1] = C[1][1] - B[1]
    A2[2] = C[1][2] - B[2]

    if len(set(A2)) != 1:
        continue

    A3[0] = C[2][0] - B[0]
    A3[1] = C[2][1] - B[1]
    A3[2] = C[2][2] - B[2]

    if len(set(A3)) != 1:
        continue

    if len(set(A2)) == 1 and len(set(A3)) == 1:
        print("Yes")
        exit()

print("No")
