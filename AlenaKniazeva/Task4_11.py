"""This program contains a function, that receives changeable number of 
dictionaries (keys - letters, values - numbers) and combines them into 
one dictionary. Dict values ​​are summarized in case of identical keys"""

def combine_dicts(*args):
    res = {}
    for i in range(len(args)):
        for key, value in args[i].items():
            if key not in res: 
                res[key] = value
            else:
                res[key] += value
    return res

if __name__ == "__main__":
    dic_list = []
    while True:
        try:
            s = input("Enter a dictionary: ")
            dic = {}
            l_s = s.strip('{}').split(', ')
            for i in l_s:
                dic[i.split(': ')[0].strip("'")] = int(i.split(': ')[1])
            dic_list.append(dic)
        except:
            break
    print("Result dictionary: {}".format(combine_dicts(*dic_list)))
