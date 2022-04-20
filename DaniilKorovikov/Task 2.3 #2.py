num = int(input())
lst_divisors = []
for i in range(1, num+1):
    if not num % i:
        lst_divisors.append(i)
print(lst_divisors)