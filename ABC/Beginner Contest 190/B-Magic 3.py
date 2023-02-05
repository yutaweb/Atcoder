N, S, D = map(int, input().split())
result = ""
success = ""
for i in range(N):
    X, Y = map(int, input().split())
    if ((S - X) > 0) and ((D - Y) < 0):
        success = 1

if success:
    print("Yes")
else:
    print("No")