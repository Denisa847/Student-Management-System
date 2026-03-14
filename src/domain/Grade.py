
class Grade:
    def __init__(self, discipline_id, student_id, grade_value):
        self.__student_id = student_id
        self.__discipline_id = discipline_id
        self.__grade_value = grade_value

    @property
    def student_id(self):
        return self.__student_id

    @property
    def discipline_id(self):
        return self.__discipline_id

    @property
    def grade_value(self):
        return self.__grade_value

    def __str__(self):
        return f"StudentID:{self.student_id}, DisciplineID:{self.discipline_id}, Grade:{self.grade_value}"