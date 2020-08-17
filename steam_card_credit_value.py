while True:
    total_credit = float(input("Enter total credit value: "))
    total_float = float(input("Enter total float value: "))
    total_steam = float(input("Enter total steam value: "))

    y = total_credit / (100 * total_float)
    z = total_credit / (100 * total_steam)
    # 3 is the minimum card float value I have seen to date.
    x = 3
    a = 0
    b = 0   
    # The list will increase until the max credit value of 25 is reached.
    while (a <= 25) and (b <= 25):
        a, b = round((x * y), 2), round((x * z), 2)
        print(f"{x}. {a}, {b}")
        x += 1