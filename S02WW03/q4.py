lsms = [[4,9,2],[3,5,7],[8,1,6]]


def check_lsms():
    while True:
        try:
            get_input = int(input("enter your number: "))
            for list in lsms:
                if get_input in list:
                    return "True"
                else:
                    return "False"
        except ValueError:
            print("enter a valid number please!")
        


print(check_lsms())