N = int(input())

if abs(N) < 2**31 or N == -2**31:
    print("Yes")
else:
    print("No")
