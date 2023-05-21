from models.AbstractStadium import AbstractStadium


class SwimmingPool(AbstractStadium):

    def __init__(self, name, capacity, current_attendance, number_of_shower_rooms,
                 volume, max_number_of_participants, springboard_jumping,
                 artistic_swimming, complex_swimming):
        super().__init__(name, capacity, current_attendance)
        self.number_of_shower_rooms = number_of_shower_rooms
        self.volume = volume
        self.max_number_of_participants = max_number_of_participants
        self.springboard_jumping = springboard_jumping
        self.artistic_swimming = artistic_swimming
        self.complex_swimming = complex_swimming

    __instance = None

    @staticmethod
    def get_instance():
        if SwimmingPool.__instance is None:
            SwimmingPool.__instance = SwimmingPool()
        return SwimmingPool.__instance

    def get_supported_sports(self):
        supported_sports = list()
        if self.springboard_jumping: supported_sports.append("springboard_jumping")
        if self.artistic_swimming: supported_sports.append("artistic_swimming")
        if self.complex_swimming: supported_sports.append("complex_swimming")
        return supported_sports
