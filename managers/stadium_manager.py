"""Module that stores and filters objects"""

from decorators.decorators import method_name_decorator, pylint_decorator


class StadiumManager:
    """Class representing a manager of stadiums"""
    sport_complex_list = []

    def add_complex(self, sport_complex):
        """Function  add new complex to list of sport complex"""
        self.sport_complex_list.append(sport_complex)

    def find_all_current_attendance_less_than(self, current_attendance):
        """Function  add find all complex wint current attendance less than the resulting number"""
        filter_list = filter(lambda complexes: complexes.current_attendance < current_attendance,
                             self.sport_complex_list)
        return filter_list

    def find_all_more_capacity_than(self, capacity):
        """Function  add find all complex wint more capacity than the resulting number"""
        filter_list = filter(lambda complexes: complexes.capacity > capacity,
                             self.sport_complex_list)
        return filter_list


    def __len__(self):
        return len(self.sport_complex_list)

    def __getitem__(self, item):
        default = "wrong index"
        if not isinstance(item, int):
            raise TypeError("wrong index type")

        if 0 <= item < len(self.sport_complex_list):
            return self.sport_complex_list[item]
        raise IndexError(default)

    def __iter__(self):
        return iter(self.sport_complex_list)

    @method_name_decorator
    def get_result_abstract_method(self):
        """" Gets the results of the abstract method in all objects of the list and returns this """
        result = [sport_complex.get_supported_sports()
                  for sport_complex in self.sport_complex_list]
        return result

    @pylint_decorator
    def get_enumerated_objects(self):
        """Returns a concatenation of each object with its index in the list"""
        result = [f"Index => {index}   value => {sport_complex}"
                  for index, sport_complex in enumerate(self.sport_complex_list)]
        return result

    @method_name_decorator
    def get_zipping(self):
        """Returns the concatenation of each object with its corresponding result
         from get_result_abstract_method"""
        result = [f"{sport_complex}  +  {abstract_result} "
                  for sport_complex, abstract_result in zip(self.sport_complex_list,
                                                            self.get_result_abstract_method())]
        return result

    def check_condition(self, condition):
        """" Checks the condition for all objects in the manager """
        all_condition = all(condition(sport_complex) for sport_complex in self.sport_complex_list)
        any_condition = any(condition(sport_complex) for sport_complex in self.sport_complex_list)
        return {"All =>": all_condition, "\n Any =>": any_condition}
