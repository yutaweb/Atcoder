K = int(input())
A, B = map(int, input().split())


def k_to_10digit(k, num):
    num_to_str = str(num)
    val = 0
    for i, v in enumerate(num_to_str[::-1]):
        val += k**i*int(v)

    return val


ans = k_to_10digit(K, A) * k_to_10digit(K, B)

print(ans)
# print(k_to_10digit(K, A))
# print(k_to_10digit(K, B))
