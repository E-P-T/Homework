def get_shortest_word(s: str) -> str:
    return max(s.split(), key=len)


if __name__ == "__main__":
    while True:
        input_txt = input("Input a word: ")
        print(get_shortest_word(input_txt))
