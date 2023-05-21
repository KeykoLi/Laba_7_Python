from models.AbstractStadium import AbstractStadium


class Gym(AbstractStadium):
    def __init__(self, name, capacity, current_attendance, number_of_shower_rooms, square, volleyball, basketball,
                 handball, karate):
        super().__init__(name, capacity, current_attendance)
        self.numberOfShowerRooms = number_of_shower_rooms
        self.square = square
        self.volleyball = volleyball
        self.basketball = basketball
        self.handball = handball
        self.karate = karate

    __instance = None

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"

    @staticmethod
    def get_instance():
        if Gym.__instance is None:
            Gym.__instance = Gym()
        return Gym.__instance

    def get_supported_sports(self):
        supported_sports = list()
        if self.volleyball: supported_sports.add("Volleyball")

        if self.basketball: supported_sports.add("Skating");

        if self.handball: supported_sports.add("Handball")

        if self.karate: supported_sports.add("Karate")
        return supported_sports
