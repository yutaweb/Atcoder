# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import itertools


def dec2bin(target):
    amari = []

    while target != 0:
        amari.append(target % 2)
        target = target // 2

    amari.reverse()
    return amari


def calc(data):
    base = int(data[0])
    ans = 1
    for i in range(1, len(data)):
        ans = bin(base & int(data[i]))

    return ans


def solution(A):
    # write your code in Python 3.6
    digits_change_from10to2 = []
    for i in A:
        change_digits = i
        digits_change_from10to2.append(change_digits)

    result = []
    ans_lists = []
    for n in range(1, len(digits_change_from10to2) + 1):
        for combination in itertools.combinations(digits_change_from10to2, n):
            result.append(calc(list(combination)))
            ans_lists.append(len(combination))

    for i, v in reversed(list(enumerate(result))):
        if v != 1:
            if int(v[2:]) == 0:
                ans = ans_lists[len(ans_lists) - 1 - i]
                return ans

    return 1


if __name__ == "__main__":
    A = [13, 8, 2, 8]
    print(solution(A))
