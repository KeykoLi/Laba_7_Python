"""Module that stores and filters objects"""


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
