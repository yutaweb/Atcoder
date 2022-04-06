V, T, S, D = map(int, input().split())
if D < V*T or D > V*S:
    print("Yes")
else:
    print("No")