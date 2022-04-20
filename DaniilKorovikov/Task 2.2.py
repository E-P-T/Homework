s = input().lower()
d = {}
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1
print(d)