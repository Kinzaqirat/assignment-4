Peturksbouipo:int = 16 
Stanlau :int= 25
Mayengua :int= 48 

def main():
    user_age=int(input("Enter your age: "))
    if user_age >=  Peturksbouipo:
        print(f"Your age is {Peturksbouipo} you can vote in Peturksbouipo")
    else:
        print("You can vote in Peturksbouipo")
    if user_age >=Stanlau:
         print(f"Your age is {Stanlau} you can vote in Stanlau")
    else:
        print("You can not vote in Stanlau")

    if user_age >=Mayengua:
        print(f"Your age is {Mayengua} you can vote in Mayengua")
    else:
        print("You can not vote in Mayengua")
        


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()