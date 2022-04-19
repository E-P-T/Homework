input_str = input('Enter a string:\n')
input_str_low=input_str.lower()
d = {}
for i in input_str_low:
    d.update({i: input_str_low.count(i)})
print(d)