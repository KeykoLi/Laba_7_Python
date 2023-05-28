"""Module that stores model of ice palace of sport"""
from models.abstract_stadium import AbstractStadium


class IcePalaceOfSport(AbstractStadium):
    """Class representing  ice palace of sport"""

    # pylint: disable = (too-many-arguments)
    def __init__(self, name="empty", capacity=0, current_attendance=0, cover=False,
                 closed_type=False, curling=False, hockey=False, figure_skating=False):
        super().__init__(name, capacity, current_attendance)
        self.cover = cover
        self.closed_type = closed_type
        self.curling = curling
        self.hockey = hockey
        self.figure_skating = figure_skating

    set_facilities = {"ice rink", "hockey nets", "locker rooms"}

    __instance = None

    @staticmethod
    def get_instance():
        """Static method that create instance"""
        if IcePalaceOfSport.__instance is None:
            IcePalaceOfSport.__instance = IcePalaceOfSport()
        return IcePalaceOfSport.__instance

    def get_supported_sports(self):
        """Abstract method  that add to list sport what complex supported"""
        supported_sports = []
        if self.curling:
            supported_sports.append("Curling")
        if self.hockey:
            supported_sports.append("Hockey")
        if self.figure_skating:
            supported_sports.append("Figure skating")
        return supported_sports
