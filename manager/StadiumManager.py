
class StadiumManager:
    sport_complex_list = list()

    def add_copmlex(self, sport_complex):
        self.sport_complex_list.append(sport_complex)

    def find_all_current_attendance_less_than(self, current_attendance):
        return [complex for complex in self.sport_complex_list if complex.current_attendance < current_attendance]

    def find_all_more_capacity_than(self, capacity):
        return [complex for complex in self.sport_complex_list if complex.capacity > capacity]
