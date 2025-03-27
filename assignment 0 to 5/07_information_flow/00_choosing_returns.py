adult_age=18
def is_age(age:int):
    if age >= adult_age:
        return True
    else:
        return False


def main():
    age : str = int(input("How old is this person?: "))
    print(is_age(age))
    

if __name__ == "__main__":
    main()