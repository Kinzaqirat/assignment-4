def main():
    curr_value=int(input("Enter a num: "))
    while curr_value < 100:
        curr_value= curr_value*100
        print(curr_value,end=" ")

if __name__ == '__main__':
    main()