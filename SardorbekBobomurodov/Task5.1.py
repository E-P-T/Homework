if __name__ == "__main__":
    with open(r"C:\Users\Sardor\PycharmProjects\Homework\data\unsorted_names.txt", "r") as nr:
        with open("sorted_names.txt", "w") as snw:
            array_of_names = nr.readlines()
            array_of_names.sort()
            for item in array_of_names:
                snw.write(item)

    with open("sorted_names.txt", "r") as snr:
        print(snr.readlines())
