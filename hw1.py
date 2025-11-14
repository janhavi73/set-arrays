import random
def dice_game():
    min_val = 1
    max_val = 6
    roll_again = "yes"

    print("Welcome to the Dice Rolling Simulator!")
    while roll_again.lower() == "yes" or roll_again.lower() == "y":

        dice_roll = random.randint(min_val, max_val)
        print(f"\nYou rolled a **{dice_roll}**")

    
        roll_again = input("Roll again? (yes/no): ")

    print("Goodbye.")

