def main ():
    numbers=[1,2,3,4,5]
    for i in range(len(numbers)):
        index_num=numbers[i]
        numbers[i]=index_num*2

        print(numbers)

if __name__=="__main__":
    main()