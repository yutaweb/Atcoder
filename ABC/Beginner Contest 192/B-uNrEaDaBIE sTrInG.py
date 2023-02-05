S = input()
lower = 0
upper = 0
count = 0
for i, s in enumerate(S):
    if i % 2 == 0 and s.islower() == True:
        lower += 1
    elif i % 2 == 1 and s.isupper() == True:
        upper += 1
    count += 1

if count == (lower + upper):
    print("Yes")
else:
    print("No")