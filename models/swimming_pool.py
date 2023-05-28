"""Module that stores model of swimming pool"""
from models.abstract_stadium import AbstractStadium


class SwimmingPool(AbstractStadium):
    """Class representing  swimming pool"""

    # pylint: disable = (too-many-arguments)
    def __init__(self, name="empty", capacity=0, current_attendance=0,
                 number_of_shower_rooms=0, volume=0, max_number_of_participants=0,
                 springboard_jumping=False, artistic_swimming=False, complex_swimming=False):
        super().__init__(name, capacity, current_attendance)
        self.number_of_shower_rooms = number_of_shower_rooms
        self.volume = volume
        self.max_number_of_participants = max_number_of_participants
        self.springboard_jumping = springboard_jumping
        self.artistic_swimming = artistic_swimming
        self.complex_swimming = complex_swimming

    set_facilities = {"swimming lanes", "diving boards", "showers"}

    __instance = None

    @staticmethod
    def get_instance():
        """Static method that create instance"""
        if SwimmingPool.__instance is None:
            SwimmingPool.__instance = SwimmingPool()
        return SwimmingPool.__instance

    def get_supported_sports(self):
        """Abstract method  that add to list sport what complex supported"""
        supported_sports = []
        if self.springboard_jumping:
            supported_sports.append("springboard_jumping")
        if self.artistic_swimming:
            supported_sports.append("artistic_swimming")
        if self.complex_swimming:
            supported_sports.append("complex_swimming")
        return supported_sports
