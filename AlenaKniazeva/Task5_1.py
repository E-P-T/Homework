"""This program opens file `data/unsorted_names.txt` in data folder.
Then it sorts the names and write them to a new file called `sorted_names.txt`"""

if __name__ == "__main__":
    with open ('data/unsorted_names.txt', 'r') as f1, open('sorted_names.txt', 'w') as f2:
        load_s = f1.readlines()
        load_s.sort()
        for s in load_s:
            f2.write(s)