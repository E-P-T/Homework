input_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
              {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
out_list = []
for i in range(len(input_list)):
    app_str = "".join(list(input_list[i].values()))
    if app_str not in out_list:
        out_list.append(app_str)
print(out_list)
