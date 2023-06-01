"""" """
from managers.stadium_manager import StadiumManager


class SetManager:
    """" """
    manager_object = StadiumManager()
    index = 0
    iter_list = []

    def __init__(self, manager_object=None):
        self.manager_object = manager_object

    def __iter__(self):
        self.iter_list = [sport_complex.set_facilities for sport_complex in self.manager_object]
        return iter(self.iter_list)

    def __len__(self):
        return sum(len(sport_complex.set_facilities)
                   for sport_complex in self.manager_object)

    def __getitem__(self, item):
        for sport_complex in self.manager_object.sport_complex_list:
            if not isinstance(item, int):
                raise TypeError("wrong index type")
            if item < len(sport_complex.set_facilities):
                return self.iter_list[item]
            item -= len(sport_complex.set_facilities)
        raise IndexError("wrong index")

    def __next__(self):
        if self.index < len(self.iter_list):
            item = self.iter_list[self.index]
            self.index += 1
            return item
        raise StopIteration()
