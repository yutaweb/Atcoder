N = int(input())

for i in range(1, 10):
    result = divmod(N, i)
    if 1 <= result[0] <= 9 and result[1] == 0:
        exit(print("Yes"))

print("No")
