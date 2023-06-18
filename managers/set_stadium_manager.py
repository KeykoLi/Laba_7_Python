

class SetManager:

    def __init__(self, manager_object):
        self.manager_object = manager_object
        self.index = 0

    def __iter__(self):
        self.iter_list = [sport_complex.set_facilities for sport_complex in self.manager_object]
        return self

    def __len__(self):
        return sum(len(sport_complex.set_facilities)
                   for sport_complex in self.manager_object)

    def __getitem__(self, item):
        for sport_complex in self.manager_object.sport_complex_list:
            if not isinstance(item, int):
                raise TypeError("wrong index type")
            if item < len(sport_complex.set_facilities):
                return self.iter_list[item]
            raise IndexError("wrong index")

    def __next__(self):
        if len(self.iter_list) > self.index:
            raise StopIteration()
        item = self.iter_list[self.index]
        self.index += 1
        return item
