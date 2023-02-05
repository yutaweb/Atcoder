N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

Alice = 0
Bob = 0
while len(A) > 0:
    Alice += A.pop(0)
    if len(A) > 0:
        Bob += A.pop(0)

print(Alice - Bob)
# Alice : start
# Bob : end

