S = input()

# if S[0].isupper() and S[0] == 'A':
#     if 'C' in S[2:-1]:
#         c_index = S[2:-1].index('C')
#         S_list = list(S)
#         S_list.pop(c_index + 2)
#         S_list.pop(0)
#         if ''.join(S_list).islower():
#             exit(print("AC"))
#
# print("WA")
#


def is_ac(s):
    if s[0] != 'A':
        return False

    if s[2:-1].count('C') != 1:
        return False

    if sum(map(str.isupper, s)) != 2:
        return False

    return True


print('AC' if is_ac(S) else 'WA')
