def ex6(some_list):
    new_list = []
    for item in some_list:
        for key in item.keys():
            new_list.append(item[key])

    print(set(new_list))


if __name__ == '__main__':
    dic_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                {"VIII": "S007"}]
    ex6(dic_list)
