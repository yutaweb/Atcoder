# N = input()
# length = len(N)
# before_num = N[0:int(length/2)]
# after_num = N[int(length/2):length]
# if int(after_num) == 0:
#     ans = int(before_num) - 1
# elif int(before_num) > int(after_num):
#     ans = int(after_num)
# else:
#     ans = int(before_num)
#
# print(ans)

N = int(input())
for i in range(1, 1000001):
    if int(str(i) * 2) > N:
        print(i - 1)
        exit()