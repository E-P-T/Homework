
# str.split Resembling function

def mysplit(source, separators = None, maxsplit = None):
    splits = 0
    cleanup = False
    index = 0
    result = [""]

    if maxsplit == None:
        maxsplit = len(source) + 1

    if separators == None:
        separators = " \n\t"
        cleanup = True

    for c in source:
        
        if splits >= maxsplit:
            break
        
        if c in separators:
            result.append("")
            index += 1
        else:
            result[index] += c
    
    if cleanup:
        result = [el for el in result if el != ""]

    return result

test_str = "abobaaa abob "

print(mysplit(test_str, "a"))
print(test_str.split("a"))