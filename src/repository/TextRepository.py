
from src.domain.Student import Student
from src.domain.Discipline import Discipline
from src.domain.Grade import Grade
from src.repository.MemoryRepository import MemoryRepository

class TextRepository(MemoryRepository):
    def __init__(self,student_file, discipline_file,grade_file):
        super().__init__()
        self._student_file=student_file
        self._discipline_file=discipline_file
        self._grade_file=grade_file

        self._load_students()
        self._load_disciplines()
        self._load_grade()

    def _load_students(self):
        try:
            with open(self._student_file,"r") as f:
                for line in f:
                    sid,name=line.strip().split(",")
                    self._students[int(sid)]=Student(int(sid),name)
        except FileNotFoundError:
            open(self._student_file, "w").close()


    def _load_disciplines(self):
        try:
            with open(self._discipline_file, "r") as f:
                for line in f:
                    did, name = line.strip().split(",")
                    self._disciplines[int(did)] = Discipline(int(did), name)
        except FileNotFoundError:
            open(self._discipline_file, "w").close()


    def _load_grade(self):
        try:
            with open(self._grade_file, "r") as f:
                for line in f:
                    if line.strip()=="":
                        continue
                    sid,did,value = line.strip().split(",")
                    self._grades.append(Grade(int(did), int(sid), float(value)))
        except FileNotFoundError:
                open(self._grade_file, "w").close()



    def save_students(self):
        with open(self._student_file, "w") as f:
            for s in self._students.values():
                f.write(f"{s.id},{s.name}\n")

    def save_disciplines(self):
        with open(self._discipline_file, "w") as f:
            for d in self._disciplines.values():
                f.write(f"{d.id},{d.name}\n")

    def save_grade(self):
        with open(self._grade_file, "w") as f:
            for g in self._grades:
                f.write(f"{g.student_id},{g.discipline_id},{g.grade_value}\n")

    def add_student(self,student):
        """
            check if the student is present and if it is raise an error and not add it
            save updated list
        """
        super().add_student(student)
        self.save_students()

    def remove_student(self,student_id):
        """
        if the student is not present there is nothing to delte=> raise errror and do nothing
        save updated list

        """
        super().remove_student(student_id)
        self.save_students()

    def update_student(self,student):
        """
        updates the student if is present in the list, else raise erorr and do nothing
        save updated list
        """
        super().update_student(student)
        self.save_students()

    def add_discipline(self,discipline):
        """
         check if the discipline is present and if it is raise an error and not add it
         save updated list
      """

        super().add_discipline(discipline)
        self.save_disciplines()

    def remove_discipline(self,discipline_id):
        """
         if the discipline is not present there is nothing to delte=> raise errror and do nothing
        save updated list
        """
        super().remove_discipline(discipline_id)
        self.save_disciplines()

    def update_discipline(self, discipline):
        """
        updates the discipline if is present in the list, else raise erorr and do nothing
        """
        super().update_discipline(discipline)
        self.save_disciplines()


    def add_grade(self,grade):
        super().add_grade(grade)
        self.save_grade()

    def remove_grade_students(self,student_id):
        super().remove_grades_student(student_id)
        self.save_grade()

    def remove_grades_discipline(self,discipline_id):
        super().remove_grades_discipline(discipline_id)
        self.save_grade()

    def clear_students(self):
        super().clear_students()
        self.save_students()

    def clear_disciplines(self):
        super().clear_disciplines()
        self.save_disciplines()

    def clear_grades(self):
        super().clear_grades()
        self.save_grade()

