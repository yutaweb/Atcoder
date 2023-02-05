A, B = map(int, input().split())

# collection_A = set()
# collection_B = set()
#
# i = 0
# for i in range(10):
#     price_A = (A*100 + i*10) / 8
#     if int(price_A) == price_A:
#         collection_A.add(price_A)
#
#     price_B = (B * 100 + i * 10) / 10
#     if int(price_B) == price_B:
#         collection_B.add(price_B)
#
# temp = collection_A.intersection(collection_B)
# print(int(min(temp)) if len(temp) != 0 else -1)

ans = -1
for i in range(1001):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        ans = i
        break

print(ans)
