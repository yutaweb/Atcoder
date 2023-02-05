N = int(input())
A = list(map(int, input().split()))

right = 0
res = 0
s = 0
for left in range(N):
    while right < N and (s ^ A[right] == s + A[right]):
        s += A[right]
        right += 1

    res += right - left

    if right == left:
        right += 1
    else:
        s -= A[left]

print(res)
