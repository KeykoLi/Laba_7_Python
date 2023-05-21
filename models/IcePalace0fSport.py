from models.AbstractStadium import AbstractStadium


class IcePalaceOfSport(AbstractStadium):

    def __init__(self, name, capacity, current_attendance, cover,
                 closed_type, curling, hockey, figure_skating):
        super().__init__(name, capacity, current_attendance)
        self.cover = cover
        self.closed_type = closed_type
        self.curling = curling
        self.hockey = hockey
        self.figure_skating = figure_skating

    __instance = None

    @staticmethod
    def get_instance():
        if IcePalaceOfSport.__instance is None:
            IcePalaceOfSport.__instance = IcePalaceOfSport()
        return IcePalaceOfSport.__instance

    def get_supported_sports(self):
        supported_sports = list()
        if self.curling: supported_sports.append("Curling")
        if self.hockey: supported_sports.append("Hockey")
        if self.figure_skating: supported_sports.append("Figure skating")
        return supported_sports
