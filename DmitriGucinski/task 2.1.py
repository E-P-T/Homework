string = 'Find length of this string'

length = 0
for chr in string:
    length += 1
    
print(length)
print('result: {} == string len {} '.format(length, len(string)))