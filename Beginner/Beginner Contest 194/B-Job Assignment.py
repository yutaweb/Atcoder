N = int(input())
lists = []
A = []
B = []

for i in range(N):
    # lists.append(list(map(int, input().split())))
    # lists.append()
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A_min_val = min(A)
B_min_val = min(B)
A_min_index = A.index(A_min_val)
B_min_index = B.index(B_min_val)
Ans = 0
# A_index = 0
# B_index = 0

if A_min_index == B_min_index:
    Ans = A_min_val + B_min_val
    A.pop(A_min_index)
    B.pop(B_min_index)
    A_pop_min_val = min(A)
    B_pop_min_val = min(B)
    if (Ans >= B_pop_min_val) and (B_pop_min_val >= A_min_val):
        Ans = B_pop_min_val
    elif (Ans >= A_pop_min_val) and (A_pop_min_val >= B_min_val):
        Ans = A_pop_min_val
else:
    if A_min_val >= B_min_val:
        Ans = A_min_val
    else:
        Ans = B_min_val

print(Ans)

# lists.sort()
