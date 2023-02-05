S, T = map(int, input().split())

counter = 0
for a in range(101):
    for b in range(101):
        for c in range(101):
            # if a + b + c > S:
            #     continue

            if a + b + c <= S and a * b * c <= T:
                counter += 1

print(counter)
