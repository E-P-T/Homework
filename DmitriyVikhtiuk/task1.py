with open("unsorted_names.txt") as file:
    names = file.readlines()
    list_of_names = [name.rstrip() for name in names]
list_of_names.sort()
print(list_of_names)
with open("sorted_names.txt", mode="w") as f:
    for name in list_of_names:
        f.write(f"{name}\n")

