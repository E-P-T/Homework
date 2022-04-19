string = "Lorem Ipsum is simply dummy text of the printing"
dict = {}
for n in string.lower():
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print(dict)