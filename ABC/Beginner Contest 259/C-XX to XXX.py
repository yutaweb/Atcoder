import itertools

S = input()
T = input()


def rle(data):
    # ランレングス圧縮
    return [[key, len(list(group))] for key, group in itertools.groupby(data)]


def judge():
    rls_s = rle(S)
    rls_t = rle(T)

    if len(rls_s) != len(rls_t):
        return False
    for i, v in enumerate(rls_s):
        if v[0] != rls_t[i][0]:
            return False
        if v[1] == 1:
            if rls_t[i][1] != 1:
                return False
        else:
            if rls_t[i][1] < v[1]:
                return False

    return True


if __name__ == '__main__':
    if judge():
        ans = 'Yes'
    else:
        ans = 'No'

    print(ans)
