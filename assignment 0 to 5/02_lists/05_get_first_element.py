def get_first_elemet(lst):
    print(lst[0])
  

def get_lst():
    lst=[]
    element:int=input("Enter element to add the list or press enter to stop: ")
    while element !="":
        lst.append(element)
        element = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst=get_lst()
    get_first_elemet(lst)
   


if __name__ == '__main__':
    main()