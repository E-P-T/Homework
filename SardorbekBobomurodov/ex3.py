def ex3(text):
    words = [n for n in text.split(",")]
    print(",".join(sorted(list(set(words)))))


if __name__ == '__main__':
    while True:
        text = input("Enter comma separated text: ")
        ex3(text)
