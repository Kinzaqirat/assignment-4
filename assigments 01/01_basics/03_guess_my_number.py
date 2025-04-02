import random
def main():
    num:int =random.randint(1,99)
    guess=int(input("Enter a num between 1 to 99  "))

    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    else:
        print("Correct " + num)
if __name__ == '__main__':
    main()