max_num=500

def main():
    num1=0
    num2=1
    while num1 <=  max_num:
        print(num1)
        sum = num1 + num2
        num1=num2
        num2=sum


if __name__=="__main__":
    main()