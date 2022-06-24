N = int(input())

num_a = 0
num_b = 1000000


def calc(a, b):
    calc_num = a*a*a + a*a*b + a*b*b + b*b*b
    return calc_num


'''
1. b=0固定でaを増加させていく
2. 一致せずにNの値を超過したらbを1増やしてa=0から始める
'''
x = 8e18
while num_a <= num_b:
    ans = calc(num_a, num_b)
    if ans > N:
        x = min(x, ans)
        num_b -= 1
    else:
        num_a += 1

print(x)
