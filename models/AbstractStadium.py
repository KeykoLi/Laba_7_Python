from abc import ABC, abstractmethod


class AbstractStadium(ABC):
    def __init__(self, name="empty", capacity=0, current_attendance=0):
        self.name = name
        self.capacity = capacity
        self.current_attendance = current_attendance

    @abstractmethod
    def get_supported_sports(self):
        pass