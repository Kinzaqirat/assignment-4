import random

dice_num=6


def main():
    dice1=random.randint(1,dice_num)
    dice2=random.randint(1,dice_num)
    total=dice1+dice2

    print(f"Number of dice {dice_num}")
    print(f"Dice 1 has {dice1} num")   
    print(f"Dice 2 has {dice2} num")
    print( f"Total is {total}")

if __name__ == '__main__':
    main()