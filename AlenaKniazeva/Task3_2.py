"""This program asks the user for a number and then prints out
a list of all the divisors of that number"""

def divisor(num):
    divis = {i for i in range(1,num+1) if num % i == 0}
    return divis

if __name__ == "__main__":
    input_num = int(input("Enter a number: "))
    print("Divisors of the entered number are: {}".format(divisor(input_num)))