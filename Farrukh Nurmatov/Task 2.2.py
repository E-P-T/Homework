"""Write a Python program to count the number of characters
   (character frequency) in a string (ignore case of letters)."""



def freq_counter(some_str: str):

    """Function takes string in input and returns dictionary of letters and letters frequency in string,
     ignoring case of the letters"""

    some_str = some_str.lower()                        # set all letters in string to lowercase
    counter_dict = dict()
    for char in set(list(some_str)):                   # loop that moves across letters set
        counter_dict[char] = input_str.count(char)     # add letter: letter_frequency to dictionary
    return counter_dict

if __name__ == '__main__':
    input_str = input("Input your string:")
    print(freq_counter(input_str))
