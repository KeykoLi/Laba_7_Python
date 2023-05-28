"""Module that stores model of stadium"""
import constant
from models.abstract_stadium import AbstractStadium


class Stadium(AbstractStadium):
    """Class representing a stadium"""

    # pylint: disable = (too-many-arguments)
    def __init__(self, name, capacity, current_attendance, home_team="empty", away_team="empty",
                 bicycle_track=False, skating_sport=False, football=False, athletics=False):
        super().__init__(name, capacity, current_attendance)
        self.home_team = home_team
        self.away_team = away_team
        self.bicycle_track = bicycle_track
        self.skating_sport = skating_sport
        self.football = football
        self.athletics = athletics

    __instance = None

    def add_attendance(self, count):
        """Method  that increases the attendance by the given number"""
        if self.capacity >= self.current_attendance + count:
            self.current_attendance += count

    def decrease_attendance(self):
        """Method  that decreases the attendance by the given number"""
        if self.current_attendance > constant.DECREASE:
            self.current_attendance -= constant.DECREASE

    def change_home_team(self, team_name):
        """Method  that change name of home team to other"""
        self.home_team = team_name

    def change_away_team(self, team_name):
        """Method  that change name of away team to other"""
        self.away_team = team_name

    @staticmethod
    def get_instance():
        """Static method that create instance"""
        if Stadium.__instance is None:
            Stadium.__instance = Stadium()
        return Stadium.__instance

    def get_supported_sports(self):
        """Abstract method  that add to list sport what complex supported"""
        supported_sports = []
        if self.bicycle_track:
            supported_sports.append("Bicycle races")
        if self.skating_sport:
            supported_sports.append("Skating")
        if self.football:
            supported_sports.append("Football")
        if self.athletics:
            supported_sports.append("Athletics")
        return supported_sports
