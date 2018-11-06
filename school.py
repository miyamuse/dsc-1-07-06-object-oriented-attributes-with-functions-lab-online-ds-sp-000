class School:
    def __init__(self, school_name = None):
        self.school_name = school_name
        self._roster = {}
    
    def roster(self):
        return self._roster
    
    def add_student(self, student_name, grade):
        if grade in self._roster:
            self._roster[grade].append(student_name)
        else:
            self._roster[grade] = []
            self._roster[grade].append(student_name)
        return self._roster
    
    def grade(self, grade):
        return self._roster[grade]
    
    def sort_roster(self):
        for key in self._roster:
            self._roster[key].sort()
        return self._roster
    