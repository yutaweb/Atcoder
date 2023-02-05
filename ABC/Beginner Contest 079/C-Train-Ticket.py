nums = list(map(int, input()))
PM = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 0],
]

for pm in PM:
    ans = nums[0]
    if pm[0] == 0:
        pm[0] = '-'
        ans -= nums[1]
    else:
        pm[0] = '+'
        ans += nums[1]

    if pm[1] == 0:
        pm[1] = '-'
        ans -= nums[2]
    else:
        pm[1] = '+'
        ans += nums[2]

    if pm[2] == 0:
        pm[2] = '-'
        ans -= nums[3]
    else:
        pm[2] = '+'
        ans += nums[3]

    if ans == 7:
        print(*[nums[0], pm[0], nums[1], pm[1], nums[2], pm[2], nums[3], '=7'], sep='')
        exit()
