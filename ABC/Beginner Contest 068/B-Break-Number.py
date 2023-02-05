N = int(input())

i = 1
while N >= 2**i:
    i = i + 1

ans = 2**(i-1)
print(ans)
