

import random


dice = 6

def roll_dice():
 
    diec1: int = random.randint(1, dice)
    diec2: int = random.randint(1, dice)
    total: int = diec1 + diec2
    print("Total of two dice:", total)

def main():
    dice1: int = 10
    print("die1 in main() starts as: " + str(dice1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(dice1))

if __name__ == '__main__':
    main()