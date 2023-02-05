N, A, B = map(int, input().split())


def calc_sum_digit(n):
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n = n // 10

    return sum_digit


result = 0
for i in range(1, N + 1):
    if A <= calc_sum_digit(i) <= B:
        result += i

print(result)
