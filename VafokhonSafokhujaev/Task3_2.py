number = int(input())
divisors = set()

for i in range(1, number+1):
    if number % i == 0:
        divisors.add(i)

print(divisors)