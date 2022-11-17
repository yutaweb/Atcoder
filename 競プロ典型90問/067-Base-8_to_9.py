N, K = map(int, input().split())


def eight_to_ten_digit(num):
    num_to_str = str(num)
    val = 0
    for i, v in enumerate(num_to_str[::-1]):
        val += 8**i*int(v)

    return val


def ten_to_nine_digit(num):
    nine_digit_list = list()
    while num > 0:
        nine_digit_list.append(num % 9)
        num = num // 9

    val = ''.join(map(str, nine_digit_list[::-1]))

    return val


def change_eight_to_five(num):
    num_to_str = str(num)
    lists = [*num_to_str]
    for i in range(len(lists)):
        if lists[i] == '8':
            lists[i] = '5'

    val = ''.join(map(str, lists))

    return val


for _ in range(K):
    ten_digit = eight_to_ten_digit(N)
    nine_digit = ten_to_nine_digit(ten_digit)
    change_num = change_eight_to_five(ten_to_nine_digit(ten_digit))
    N = change_num

print(change_num)
