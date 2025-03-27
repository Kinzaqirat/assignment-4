def get_add(value:int):
    remain=value % 2
    return remain ==1

def main():
    for i in range(20):
        if get_add(i):
            print(i," is odd "  )
        else:
            print(i," is even")    

if __name__=="__main__":
    main()            