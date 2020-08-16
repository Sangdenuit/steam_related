# 3 is the minimum card float value I have seen to date.
x = 3
a = 0
b = 0

while True:
    # y = Total card credits divided by total card float value.
    y = float(input())
    # z = Total card credits divided by total card lifetime average value.
    z = float(input())
    # The list will increase until the max credit value of 25 is reached.
    while (a <= 25) and (b <= 25):
        a, b = round((x * y), 2), round((x * z), 2)
        print(f"{x}. {a}, {b}")
        x += 1