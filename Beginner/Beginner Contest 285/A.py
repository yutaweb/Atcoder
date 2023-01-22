a, b = map(int, input().split())

if a == 1 and (b == 2 or b == 3):
    ans = "Yes"
elif a == 2 and (b == 4 or b == 5):
    ans = "Yes"
elif a == 4 and (b == 8 or b == 9):
    ans = "Yes"
elif a == 5 and (b == 10 or b == 11):
    ans = "Yes"
elif a == 3 and (b == 6 or b == 7):
    ans = "Yes"
elif a == 6 and (b == 12 or b == 13):
    ans = "Yes"
elif a == 7 and (b == 14 or b == 15):
    ans = "Yes"
elif b == 1 and (a == 2 or a == 3):
    ans = "Yes"
elif b == 2 and (a == 4 or a == 5):
    ans = "Yes"
elif b == 4 and (a == 8 or a == 9):
    ans = "Yes"
elif b == 5 and (a == 10 or a == 11):
    ans = "Yes"
elif b == 3 and (a == 6 or a == 7):
    ans = "Yes"
elif b == 6 and (a == 12 or a == 13):
    ans = "Yes"
elif b == 7 and (a == 14 or a == 15):
    ans = "Yes"
else:
    ans = "No"

print(ans)
