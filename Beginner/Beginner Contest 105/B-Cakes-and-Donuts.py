N = int(input())

for i in range(100):
    for j in range(100):
        if 4 * i + j * 7 == N:
            exit(print("Yes"))

print("No")
g