def main(text):
    if text == text[::-1]:
        print("Inputted string is polindrome!")
    else:
        print("Not polindrome!")


if __name__ == "__main__":
    while True:
        input_str = input("Input a string: ")
        main(input_str)
