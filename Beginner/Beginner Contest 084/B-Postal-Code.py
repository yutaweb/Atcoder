A, B = map(int, input().split())
S = input()


def is_ac(s):
    if len(s) != A+B+1:
        return False

    if s[A] != '-':
        return False

    if s[:A].isnumeric() is False or s[A+1:].isnumeric() is False:
        return False

    return True


print('Yes' if is_ac(S) else 'No')
