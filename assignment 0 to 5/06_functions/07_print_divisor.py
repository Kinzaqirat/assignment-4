def divisor(num:int):
    print("Here is the divisor of: ", num)
    for i in range(num):
        curr_num=i + 1
        if num % curr_num==0:
            print(curr_num)

def main():
    num=int(input("Enter a num: "))
    divisor(num)


if __name__ == '__main__':
    main()