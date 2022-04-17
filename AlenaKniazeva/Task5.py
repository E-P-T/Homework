"""This program prints all unique values of of all dictionaries in a list"""

def unique(list_dic):
    res = set()
    for i in list_dic:
        res.add((i.split(':')[1]).strip(" [{}]\""))
    return res

if __name__ == "__main__":
    s = input("Enter a list of dictionaries: ")
    list_dic = s.split(',')
    print("Unique values: {}".format(unique(list_dic)))