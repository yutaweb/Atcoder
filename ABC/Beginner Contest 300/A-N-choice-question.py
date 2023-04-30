N, A, B = map(int, input().split())
C = list(map(int, input().split()))

add = A + B
ans = C.index(add) + 1

print(ans)
