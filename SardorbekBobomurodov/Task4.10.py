def generate_squares(number) -> dict:
    numbers_dict = {}
    for i in range(number+1):
        numbers_dict[i] = i ** 2
    return numbers_dict


if __name__ == "__main__":
    number = input("Input a number: ")
    generate_squares(5)
    print(generate_squares(int(number)))
