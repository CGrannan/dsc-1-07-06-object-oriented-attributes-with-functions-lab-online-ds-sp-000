class School:
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster
    def add_student(self, student, grade):
        if grade in self.roster:
            self.roster[grade].append(student)
        else:
            self.roster[grade] = [student]
    def grade(self, grade):
        return self.roster[grade]
    def sort_roster(self):
        sorted_roster = self.roster
        for key in sorted_roster:
            sorted_roster[key] = sorted(sorted_roster[key])
        return sorted_roster