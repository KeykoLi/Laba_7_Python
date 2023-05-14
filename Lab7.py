
class Stadium:
    def __init__(self, name="empty", capacity=0, current_attendance=0, home_team="empty", away_team="empty"):
        self._name = name
        self._capacity = capacity
        self._current_attendance = current_attendance
        self._home_team = home_team
        self._away_team = away_team

    instance = None

    def add_attendance(self, count):
        if self._capacity >= self._current_attendance + count:
            self._current_attendance += count

    def decrease_attendance(self):
        DECREASE = 100
        if self._current_attendance > DECREASE:
            self._urrent_attendance -= DECREASE

    def change_home_team(self, team_name):
        self._home_team = team_name

    def change_away_team(self, team_name):
        self._away_team = team_name

    def to_string(self):
        return f"Stadium: name = {self._name}, capacity = {self._capacity}, " \
               f"current attendance =  {self._current_attendance}, home team = {self._home_team}, " \
               f"away team = {self._away_team}"

    @staticmethod
    def get_instance():
        if Stadium.instance is None:
            Stadium.instance = Stadium()
        return Stadium.instance


if __name__ == "__main__":
    default_stadium = Stadium()
    stadiums = [
        Stadium(),
        Stadium("Spartac", 3000, 2140, "Dinamo", "Shahtar"),
        Stadium.get_instance(),
        Stadium.get_instance()
    ]
for stadium in stadiums:
    print(stadium.to_string())
