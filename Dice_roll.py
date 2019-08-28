def dice_roll1():
    import random
    for x in range(2):
        return random.randint(1, sides)


def dice_roll2():
    import random
    for x in range(2):
        return random.randint(1, sides)


def dice_roller_app(roll1, roll2):
    if roll1 == 1 and roll2 == 1:
        return "Snake Eyes"
    elif roll1 and roll2 == 6:
        return "Boxcars"
    else:
        return "No special roll"


choice = "y"

while choice == "y":

    sides = int(input("How many sides do you want your dice to have?"))

    roll1 = dice_roll1()
    roll2 = dice_roll2()

    print(roll1)
    print(roll2)
    print(dice_roller_app(roll1, roll2))

    choice = input("Would you like to roll the dice? Y/N").lower()


print("Thanks for rolling with us!")





