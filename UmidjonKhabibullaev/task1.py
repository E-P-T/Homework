def sort_names_file(file_path: str):
    """ Funtion that receives a file containing unsorted names.
        Sorts the names and writes them to a new file.
    """
    ### Read and store data from file ###
    with open(file_path, "r") as f:
        names = [name for name in f.readlines()]

    ### Sort a list of names ###    
    names.sort()
    
    ### Write the sorted list to a new file ###
    with open("sorted_names.txt", "w") as f:
        [f.write(name) for name in names]



if __name__ == "__main__":
    file = "../data/unsorted_names.txt"
    sort_names_file(file)