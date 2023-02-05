A = int(input())  # 500
B = int(input())  # 100
C = int(input())  # 50
X = int(input())


counter = 0
for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):
            if a * 500 + b * 100 + c * 50 == X:
                counter += 1

print(counter)
