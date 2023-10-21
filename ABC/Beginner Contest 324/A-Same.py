N = int(input())
A = map(int, input().split())

if len(set(A)) == 1:
    print("Yes")
else:
    print("No")
