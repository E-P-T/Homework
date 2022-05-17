class MyNumberCollection():
    def __init__(self, start, end=None, step=None):
        self.start = start
        self.end = end
        self.step = step
        self.coll = []
        self.create_list()

    def create_list(self):
        if type(self.start) == tuple:
            for elem in self.start:
                if type(elem) != int:
                    raise TypeError("MyNumberCollection supports only numbers!")
                else:
                    self.coll = [elem for elem in self.start]
            return self.coll
        else:
            for i in range(self.start, self.end + 1, self.step):
                self.coll.append(i)
            if self.end % self.step != 0:
                self.coll.append(self.end)
            else:
                pass
            return self.coll

    def append(self,  num):
        try:
            self.coll.append(num)
        except TypeError:
            raise TypeError("'string' - object is not a number!")

    def __str__(self):
        return f"{self.coll}"

    def __add__(self, other):
        return self.coll + other.coll

    def __getitem__(self, item):
        return self.coll[item] ** 2

    def __iter__(self):
        return iter(self.coll)


col1 = MyNumberCollection(0, 5, 2)
col1.append(7)
print(col1)
col2 = MyNumberCollection((1, 2, 3, 4, 5))
print(col2)
print(col1 + col2)
print(col2[4])
for item in col2:
    print(item)