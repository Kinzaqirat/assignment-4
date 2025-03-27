def main():
    num:int=7
    num=subract_seven(num)
    print("this should be zero: ", num)


def subract_seven(num):
    num=num-7
    return num


if __name__ == '__main__':
    main()