input_number = input("Enter a number:\n")
divisors_list=[]
for i in range(1, int(input_number)+1):
    if int(input_number)/i == int(input_number)//i:
        divisors_list.append(i)
print(divisors_list)