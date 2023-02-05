# import math
#
# N = int(input())
#
# ans = 0
#
# if N > 999:
#     for i in range(1000, N+1):
#         ans += math.floor(len(str(i))/3)
#
# print(ans)

n=int(input())
ans=0
if n>=1000: ans+=n-999
if n>=1000000: ans+=n-999999
if n>=1000000000: ans+=n-999999999
if n>=1000000000000: ans+=n-999999999999
if n>=1000000000000000: ans+=n-999999999999999
print(ans)