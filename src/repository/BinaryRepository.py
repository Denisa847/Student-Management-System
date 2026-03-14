import pickle
from src.repository.MemoryRepository import MemoryRepository

class BinaryRepository(MemoryRepository):
    def __init__(self,student_file, discipline_file,grade_file):
        super().__init__()
        self._student_file = student_file
        self._discipline_file = discipline_file
        self._grade_file=grade_file
        self._load_students()
        self._load_disciplines()
        self._load_grades()

    def _load_students(self):
        try:
            with open(self._student_file,"rb") as f:
                self._students=pickle.load(f)
        except FileNotFoundError:
            self.save_students()


    def _load_disciplines(self):
        try:
            with open(self._discipline_file, "rb") as f:
                self._disciplines = pickle.load(f)
        except FileNotFoundError:
            self.save_disciplines()


    def _load_grades(self):
        try:
            with open(self._grade_file, "rb") as f:
                self._grades = pickle.load(f)
        except FileNotFoundError:
            self.save_grades()

    def save_students(self):
        with open(self._student_file, "wb") as f:
            pickle.dump(self._students, f)

    def save_disciplines(self):
        with open(self._discipline_file, "wb") as f:
            pickle.dump(self._disciplines,f)

    def save_grades(self):
        with open(self._grade_file, "wb") as f:
            pickle.dump(self._grades, f)

    def add_grade(self, grade):
        super().add_grade(grade)
        self.save_grades()

    def remove_grade_students(self, student_id):
        super().remove_grades_student(student_id)
        self.save_grades()

    def remove_grades_discipline(self, discipline_id):
        super().remove_grades_discipline(discipline_id)
        self.save_grades()


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
         save changes
        """
        super().update_discipline(discipline)
        self.save_disciplines()

    def clear_students(self):
        super().clear_students()
        self.save_students()

    def clear_disciplines(self):
        super().clear_disciplines()
        self.save_disciplines()

    def clear_grades(self):
        super().clear_grades()
        self.save_grades()




