# https://qiita.com/drken/items/ecd1a472d3a0e7db8dce#%E5%95%8F%E9%A1%8C-4abc-038-c-%E5%8D%98%E8%AA%BF%E5%A2%97%E5%8A%A0

N = int(input())
A = list(map(int, input().split()))

right = 0
res = 0
temp = {a: False for a in A}
for left in range(N):
    while right < N and not temp[A[right]]:
        temp[A[right]] = True
        right += 1

    res = max(res, right - left)

    if right == left:
        right += 1
    else:
        temp[A[left]] = False


print(res)
