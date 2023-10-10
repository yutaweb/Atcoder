S = input()

count = 0
for i in range(1, len(S) + 1, 2):
    if S[i] == "1":
        exit(print("No"))

print("Yes")
