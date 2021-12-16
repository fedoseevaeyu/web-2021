class Unique:
    def __init__(self, data, **kwargs):
        self.data = data
        self.type = type(data)
        self.index = 0
        self.unique_values = set()
        self.ignore_case = kwargs['ignore_case'] if kwargs.get('ignore_case') is not None else False

    def __iter__(self):
        return self

    def check_elem(self, elem):
        if self.ignore_case:
            elem = elem.lower()
        if elem not in self.unique_values:
            self.unique_values.add(elem)
            return True
        return False

    def __next__(self):
        if self.type == list:
            while self.index < len(self.data):
                elem = self.data[self.index]
                self.index += 1
                if self.check_elem(elem):
                    return elem
        else:
            for elem in self.data:
                if self.check_elem(elem):
                    return elem
        raise StopIteration


if __name__ == '__main__':
    data1 = [1, 1, 2, 2, 3, 4, 1, 0]
    data2 = ['a', 'b', 'A', 'a', 'B', 'b']
    data3 = (i for i in data2)
    for i in Unique(data1):
        print(i)
    print()
    for i in Unique(data2):
        print(i)
    print()
    for i in Unique(data3, ignore_case=True):
        print(i)
