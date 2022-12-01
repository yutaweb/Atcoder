A, B = map(int, input().split())
X = int(pow(A/(2*B), 2/3))
Y = X + 1
if X == 0:
    X = 1

print(min(B*(X-1)+A/pow(X, 1/2), B*(Y-1)+A/pow(Y, 1/2)))
