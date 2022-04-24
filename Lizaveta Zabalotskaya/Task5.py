list_of_dictionaries = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
set_of_values = set()

for dc in list_of_dictionaries:
    for value in dc.values():
        set_of_values.add(value)

print(set_of_values)