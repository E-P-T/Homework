k = input("Your string: ")

def char_frequency(st):
    dc = {}
    for a in st.lower():
        keys = dc.keys()
        if a in keys:
            dc[a] += 1
        else:
            dc[a] = 1
    return dc

print(char_frequency(k))