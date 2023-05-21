from models.Gym import Gym
from models.Stadium import Stadium
from manager.StadiumManager import StadiumManager
from models.SwimmingPool import SwimmingPool
from models.IcePalace0fSport import IcePalaceOfSport
import constant

if __name__ == "__main__":
    manager = StadiumManager()
    manager.add_copmlex(Stadium("Spartac", 29000, 23500, "Shahtar", "Dynamo", True, True, True, True))
    manager.add_copmlex(SwimmingPool("Delfin", 1910, 1540, 40, 280.5, 10, True, True, True))
    manager.add_copmlex(IcePalaceOfSport("White bars", 380, 308, "artificial", False, False, True, True))
    manager.add_copmlex(Gym("Vitaz", 100, 78, 5, 490, False, False, True, True))

    for complex in manager.sport_complex_list: print(complex)

    print(f"\n\tSport complexes with current attendance less than {constant.FILTER_CURRENT_ATTENDANCE}:")
    filter_list_current_attendance = (manager.find_all_current_attendance_less_than(constant.FILTER_CURRENT_ATTENDANCE))
    for sport_complex in filter_list_current_attendance:
        print(sport_complex)

    print(f"\n\tSport complexes with capacity of more than {constant.FIlTER_CAPACITY}:")
    filter_list_capacity = (manager.find_all_more_capacity_than(constant.FIlTER_CAPACITY))
    for complex in filter_list_capacity:
        print(complex)
