"""Module main"""
from managers.stadium_manager import StadiumManager
from models.stadium import Stadium
from models.swimming_pool import SwimmingPool
from models.ice_palace_of_sport import IcePalaceOfSport
from models.gym import Gym
from managers.set_stadium_manager import SetManager
import constant

if __name__ == "__main__":

    manager = StadiumManager()
    manager.add_complex(Stadium("Spartac", 29000, 23500, "Shahtar", "Dynamo",
                                True, True, True, True))
    manager.add_complex(SwimmingPool("Delfin", 1910, 1540, 40, 280.5, 10,
                                     True, True, True))
    manager.add_complex(IcePalaceOfSport("White bars", 380, 308, "artificial",
                                         False, False, True, True))
    manager.add_complex(Gym("Vitaz", 100, 78, 5, 490,
                            False, False, True, True))

    for complex1 in manager.sport_complex_list:
        print(complex1)

    print(f"\n\tSport complexes with current attendance less than "
          f"{constant.FILTER_CURR_ATTENDANCE}:")
    filter_list_current_attendance = (manager.
                                      find_all_current_attendance_less_than(constant.
                                                                            FILTER_CURR_ATTENDANCE))
    for sport_complex in filter_list_current_attendance:
        print(sport_complex)

    print(f"\n\tSport complexes with capacity of more than "
          f"{constant.FILTER_CAPACITY}:")
    filter_list_capacity = (manager.
                            find_all_more_capacity_than(constant.FILTER_CAPACITY))
    for complex2 in filter_list_capacity:
        print(complex2)

    print(f"\n\tResult abstract method : \n {manager.get_result_abstract_method()}")

    print(f"\n\tIndex with value : \n {manager.get_enumerated_objects()}")

    print(f"\n\t Zip:")
    for obj in manager.get_zipping():
        print(obj)

    std = Stadium("Spartac", 29000, 23500, "Shahtar", "Dynamo",
                  True, True, True, True)
    print(std.get_attributes_by_type(bool))
    set_manager = SetManager(manager)
    for item in set_manager:
        print(item)

    print(len(set_manager))

    item = set_manager[157]
    print(item)