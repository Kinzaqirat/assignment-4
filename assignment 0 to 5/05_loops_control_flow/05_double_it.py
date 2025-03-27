def main():
    user=int(input("Enter a num: "))
    if user>100:
        print("Enter value less than 100")
    else:
        for i in range(user+1):
            print(i*2)    

if __name__=="__main__":
    main()