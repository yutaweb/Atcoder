N = int(input())
A = list(map(int, input().split()))


counter = 0
while True:
    can_do = True
    for i in range(N):
        if A[i] % 2 == 1:
            can_do = False

    if not can_do:
        break

    for i in range(N):
        A[i] //= 2

    counter += 1

print(counter)
