A, B, C = map(int, input().split())
result = A - B
if C == 0:
    if result > 0:
        print("Takahashi")
    else:
        print("Aoki")
else:
    if result < 0:
        print("Aoki")
    else:
        print("Takahashi")
