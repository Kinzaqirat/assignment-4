def get_num():
    user_numbers=[]
    while True:
        user_input=input("Enter a num: ")
        if user_input=="":
            break
        num=int(user_input)
        user_numbers.append(num)
    return user_numbers

def count_num(num_lst):
    num_dict={}
    for num in num_lst:
        if num not in num_lst:
            num_dict[num]=1
        else:
            num_dict[num]= +1
    return num_dict


def print_conts(num_dict):

    for num in num_dict:
        print(str(num) + "appears" + str(num_dict[num]) + "times")

def main():
    user_numbers=get_num()
    num_dict=count_num(user_numbers)
    print(num_dict)        


if __name__ == '__main__':
    main()