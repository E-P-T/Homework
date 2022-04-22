# Input: 'Oh, it is python' 
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}


string = 'Oh, it is python'

output = {}
tmp_string = string.lower()
for chr in tmp_string:    
    output[chr] = tmp_string.count(chr)
    
print(output)