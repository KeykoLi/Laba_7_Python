from abc import ABC, abstractmethod


class AbstractStadium(ABC):

    def __init__(self, name="empty", capacity=0, current_attendance=0):
        self.name = name
        self.capacity = capacity
        self.current_attendance = current_attendance

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"

    @abstractmethod
    def get_supported_sports(self):
        pass