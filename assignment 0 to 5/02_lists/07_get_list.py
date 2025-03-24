def main():
    lst=[]
    value=input("Enter value: ")
    while value:
        lst.append(value)
        value=input("Enter value: ")
    print("The list:" ,"", lst)    


if __name__=="__main__":
    main()