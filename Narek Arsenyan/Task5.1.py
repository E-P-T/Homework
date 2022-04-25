def sortNames():
  names = list()
  f = open("../data/unsorted_names.txt", "r")
  for x in f.readlines():
    names.append(x)
  f.close()
  names.sort()
  f = open("sorted_names.txt", "w")
  for i in names:
    f.write(i)
  f.close()
