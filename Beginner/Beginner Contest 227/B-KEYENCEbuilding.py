# 4(a + 3/4)(b + 3/4) - 9/4
# 10 = 4(a + 3/4)(b + 3/4) - 9/4
# (10 + 9/4)/4 = (a + 3/4)(b + 3/4)
N = int(input())
L = list(map(int, input().split()))
ans = 0
for l in L:
    flag=False
    for a in range(1001):
        for b in range(1001):
            if 4*a*b+3*a+3*b == l:
                flag=True
    if not flag:
        ans+=1

print(ans)
