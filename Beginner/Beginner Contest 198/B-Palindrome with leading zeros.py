N = input()
for i in range(10):
    T = "0"*i + N
    if T == T[::-1]:
        print("Yes")
        exit()

print("No")