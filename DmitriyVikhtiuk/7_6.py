import sympy
class CustomClass(BaseException):
    pass

flag =True


def prime_for_even(number):
    final_list = []
    prime_nums = [elem for elem in sympy.primerange(0, number)]
    for elem in sympy.primerange(0, number):
        sub = number - elem
        if sub in prime_nums:
            final_list.append(elem)
            final_list.append(sub)
            break
    return final_list

def prime_for_noteven(number):
    final_list = []
    prime_nums = [elem for elem in sympy.primerange(0, number)]
    for elem in sympy.primerange(0, number):
        sub = number - elem
        if sub not in prime_nums:
            final_list.append(elem)
            not_even = final_list + prime_for_even(sub)
            break
    return not_even

def foo(number):
    if number % 2 == 0:
        print(prime_for_even(number))
    else:
        print(prime_for_noteven(number))

while flag:
    try:
        inp = input("For exit tap 'q'. Num =  ")
        if inp == "q" or inp == "Q":
            flag = False
            break
        else:
            numb = int(inp)
    except Exception:
        print("Invalid type of num. try again")
    else:
        if numb >= 4:
            try:
                foo(numb)
            except UnboundLocalError:
                print("for not even value must be >=7")
            finally:
                t = input("Do you want to repeat? Press something for repeat or 'n' for exit: ")
                if t == 'n':
                    flag = False
        else:
            print("for not even value must be >=7, for even >=4")









