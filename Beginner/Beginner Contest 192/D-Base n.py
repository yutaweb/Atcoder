# X = input()
# M = int(input())
# Max = int(max(list(X)))
# count = 0
# ans = 0
# flag = True
# expo = Max + 1
# reverse = X[::-1]
# while flag:
#     for i, x in enumerate(reverse):
#         box = int(x)*(expo**i)
#         ans += box
#     if ans <= M:
#         count += 1
#         expo += 1
#         ans = 0
#     else:
#         flag = False
#
#
# print(count)