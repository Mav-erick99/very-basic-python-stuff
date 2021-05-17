class student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name  # name of student is gonna be the name we pass
        self.major = major  # name of student major is gonna be the major we pass
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
