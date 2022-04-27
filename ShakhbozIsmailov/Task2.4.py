cin = int(input("Enter the number: "))
divisors = [i for i in range(1, cin+1) if cin%i==0]
print(divisors)
