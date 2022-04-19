list = []
inputList = ["Lorem", "Ipsum", "is", "simply", "Lorem", "Ipsum", "text"]
for n in inputList:
    if n not in list:
        list.append(n)
list.sort()
print(list)