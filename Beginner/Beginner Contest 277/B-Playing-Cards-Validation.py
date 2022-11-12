N = int(input())
S = [input() for _ in range(N)]

base_list = []
for f in ["H", "D", "C", "S"]:
    for s in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
        base_list.append(f + s)

ans = "Yes"
if len(S) != len(set(S)):
    ans = "No"
    print(ans)
    exit()

for v in S:
    if v not in base_list:
        ans = "No"
        break

print(ans)
