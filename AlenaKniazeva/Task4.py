"""This program sorts a dictionary by key"""

def sort_dict(dic):
    sorted_dict = {}
    list_key = list(dic.keys())
    list_key.sort()
    for i in list_key:
        sorted_dict[i] = dic[i]
    return sorted_dict

if __name__ == "__main__":
    dic = {}
    s = True
    while s:
        s = input("Enter key:value ")
        if s:
            ls = s.split(":")
            dic[ls[0]] = ls[1]
    print("Sorted dictionary: {}".format(sort_dict(dic)))