"""This progtam counts the number of characters (character frequency)
in a string (ignores case of letters)"""

def freq_count(s):
    s=s.lower()
    res={}
    for i in s:
        if i not in res: res[i]=s.count(i)
    return res

if __name__ == '__main__':
    input_string = input("Enter the string: ")
    print("The character frequency is:\n", freq_count(input_string))