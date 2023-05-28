"""Module that stores model of gym"""
from models.abstract_stadium import AbstractStadium


class Gym(AbstractStadium):
    """Class representing  gym"""

    # pylint: disable = (too-many-arguments)
    def __init__(self, name="empty", capacity=0, current_attendance=0, number_of_shower_rooms=0,
                 square=0, volleyball=False, basketball=False,
                 handball=False, karate=False):
        super().__init__(name, capacity, current_attendance)
        self.number_of_shower_rooms = number_of_shower_rooms
        self.square = square
        self.volleyball = volleyball
        self.basketball = basketball
        self.handball = handball
        self.karate = karate

    __instance = None

    @staticmethod
    def get_instance():
        """Static method that create instance"""
        if Gym.__instance is None:
            Gym.__instance = Gym()
        return Gym.__instance

    def get_supported_sports(self):
        """Method  that add to list sport what complex supported"""
        supported_sports = []
        if self.volleyball:
            supported_sports.append("Volleyball")
        if self.basketball:
            supported_sports.append("Skating")
        if self.handball:
            supported_sports.append("Handball")
        if self.karate:
            supported_sports.append("Karate")
        return supported_sports
