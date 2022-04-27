# Implement a function split_by_index(s: str, indexes: List[int]) ->
# List[str] which splits the s string by indexes specified in indexes. Wrong indexes must be ignored. Examples:
#
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
#
# >>> split_by_index("no luck", [42])
# ["no luck"]


def split_by_index(line: str, indexes: [int]) -> [str]:
    result_line = []
    indexes = sorted(indexes)
    try:
        result_line.append(line[0:indexes[1] - 2])
        for index in range(0, len(indexes)-1):
            if indexes[index]<=0 or indexes[index]>len(line) or indexes[index+1]>len(line):
                raise Exception
            result_line.append(line[indexes[index]:indexes[index + 1]])
        result_line.append(line[indexes[-1]:-1])
        return result_line
    except Exception:
        result_line.clear()
        result_line.append(line)
        return result_line


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 40]))
