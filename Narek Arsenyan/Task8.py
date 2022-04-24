list = input("Set list: ")

def getPair(a = list):
    if len(a) == 1:
        return None
    else:
        pairs = []
        for i in range(0, len(a)-1):
            b = ()
            b += (a[i],)
            b += (a[i+1],)
            pairs.append(b)
        return pairs
print(getPair())
