def total_divided_by():
    y, z = (total_credit / (100 * total_float)), (total_credit / (100 * total_steam))
    return y, z


while True:
    total_credit = float(input("Enter total credit value: "))
    total_float = float(input("Enter total float value: "))
    total_steam = float(input("Enter total steam value: "))

    y, z = total_divided_by()

    if (y <= 1.6) and (z <= 1.6):
        # 3 is the minimum card value I have seen to date.
        card_price = 3
        float_credit = 0
        steam_credit = 0   
        # The list will increase until the max credit value of 25 is reached.
        while (float_credit <= 24.99) and (steam_credit <= 24.99):
            float_credit, steam_credit = round((card_price * y), 2), round((card_price * z), 2)
            print(f"{card_price}. {float_credit}, {steam_credit}")
            card_price += 1
        
        profit = 1
        while (y < 1.6) and (z < 1.6):
            total_credit += 1
            y, z = total_divided_by()
            profit += 1

        print(f"Expected profit is at least {profit} credits")

    else:
        print(f"{round(y, 2), round(z, 2)} \nDon't bother")