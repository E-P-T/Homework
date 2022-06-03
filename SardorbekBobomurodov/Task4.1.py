def reverse_string(text):
    indices_arr = [i for i, item in enumerate(text) if item == "'"]
    result = list(text.replace("\"", "'"))
    for j in indices_arr:
        result[j] = "\""
    result = "".join(result)
    print(result[::-1])


if __name__ == '__main__':
    while True:
        text = input("Input a string: ")
        reverse_string(text)
