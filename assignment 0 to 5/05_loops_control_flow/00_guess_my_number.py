import random

def main():
    print("I thinking a numbr between 1 to 100....")
    secret_num=random.randint(1,100)
    user_input=int(input("Enter a num:"))
    while user_input != secret_num:
        if user_input < secret_num:
            print("TOO LOW")
        else:
            print("TOO HIGH")

        print()
        user_input=int(input("Enter a num: "))    

    print("Congrats! The num was: " + str(secret_num))        
if __name__ == '__main__':
    main()