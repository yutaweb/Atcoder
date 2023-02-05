N = int(input())
#
# if N % 3 == 0 and N % 5 == 0:
#     ans = 'FizzBuzz'
# elif N % 3 == 0:
#     ans = 'Fizz'
# elif N % 5 == 0:
#     ans = 'Buzz'
# else:
#     ans = N

ans = 0
for i in range(1, N + 1):
    if i % 3 != 0 and i % 5 != 0:
        ans += i

print(ans)
