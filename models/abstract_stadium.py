"""Module that stores model of abstract stadium"""
from abc import ABC, abstractmethod


class AbstractStadium(ABC):
    """Class representing abstract stadium"""
    def __init__(self, name="empty", capacity=0, current_attendance=0):
        self.name = name
        self.capacity = capacity
        self.current_attendance = current_attendance

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"

    @abstractmethod
    def get_supported_sports(self):
        """Abstract method  that add to list sport what complex supported"""

    def get_attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}