import constant


class Stadium:
    def __init__(self, name="empty", capacity=0, current_attendance=0, home_team="empty", away_team="empty"):
        self.name = name
        self.capacity = capacity
        self.current_attendance = current_attendance
        self.home_team = home_team
        self.away_team = away_team

    __instance = None

    def add_attendance(self, count):
        if self.capacity >= self.current_attendance + count:
            self.current_attendance += count

    def decrease_attendance(self):
        if self.current_attendance > constant.DECREASE:
            self.current_attendance -= constant.DECREASE

    def change_home_team(self, team_name):
        self.home_team = team_name

    def change_away_team(self, team_name):
        self.away_team = team_name

    def _str_(self):
        return f"Stadium: name = {self.name}, capacity = {self.capacity}, " \
               f"current attendance =  {self.current_attendance}, home team = {self.home_team}, " \
               f"away team = {self.away_team}"

    @staticmethod
    def get_instance():
        if Stadium.__instance is None:
            Stadium.__instance = Stadium()
        return Stadium.__instance


if __name__ == "__main__":
    stadiums = [
        Stadium(),
        Stadium("Spartac", 3000, 2140, "Dinamo", "Shahtar"),
        Stadium.get_instance(),
        Stadium.get_instance()
    ]
for stadium in stadiums:
    print(stadium._str_())


