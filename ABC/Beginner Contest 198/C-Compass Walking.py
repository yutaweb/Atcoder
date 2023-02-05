import math

R, X, Y = map(int, input().split())
D = math.sqrt(X*X+Y*Y)

if D == R:
    print(1)
elif D <= R+R:
    print(2)
else:
    print(math.ceil(D/R))
