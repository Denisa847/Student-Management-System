from src.domain.Student import Student
from src.domain.Discipline import Discipline
from src.domain.Grade import Grade
from src.repository.RepositoryException import RepositoryException

class MemoryRepository:
    def __init__(self):
        self._students= {}
        self._disciplines={}
        self._grades = []

    def get_student(self,st_id):
        if st_id not in self._students:
            raise ValueError("Discipline ID is not in the list")
        return self._students[st_id]

    def get_discipline(self,d_id):
        if d_id not in self._disciplines:
            raise ValueError("Discipline ID is not in the list")
        return self._disciplines[d_id]

    def clear_students(self):
        self._students={}

    def clear_disciplines(self):
        self._disciplines={}

    def clear_grades(self):
        self._grades = []

    def check_present(self,id):
        if id in self._students:
            raise RepositoryException("It is already in!")

    def check_no_present(self,id):
        if id not in self._students:
            raise RepositoryException("This instance is not in the repository!")

    def add_student(self,entity):
        """
        check if the student is present and if it is raise an error and not add it
        """
        self.check_present(entity.id)
        self._students[entity.id]=entity

    def get_all_students(self):
        """
        returns a list with all the students
        """
        return list(self._students.values())

    def remove_student(self,id):
        """
        check if the student is not present there is nothing to delte=> raise errror and do nothing
        """
        self.check_no_present(id)
        del self._students[id]

    def update_student(self, entity):
        """
        updates the student if is present in the list, else raise erorr and do nothing
        """
        self.check_no_present(entity.id)
        self._students[entity.id]=entity

#--------Discipline
    def check_present_dis(self,id):
        if id in self._disciplines:
            raise RepositoryException("It is already in!")

    def check_no_present_dis(self,id):
        if id not in self._disciplines:
            raise RepositoryException("This instance is not in the repository!")

    def add_discipline(self,entity):
        """
          check  if the discipline is present and if it is raise an error and not add it
        """
        self.check_present_dis(entity.id)
        self._disciplines[entity.id]=entity

    def get_all_disciplines(self):
        """
                returns a list with all the disciplines
         """
        return list(self._disciplines.values())

    def remove_discipline(self,id):
        """
        check if the discipline is not present there is nothing to delte=> raise errror and do nothing
               """
        self.check_no_present_dis(id)
        del self._disciplines[id]

    def update_discipline(self, entity):
        """
               updates the discipline if is present in the list, else raise erorr and do nothing
               """
        self.check_no_present_dis(entity.id)
        self._disciplines[entity.id]=entity



    def add_grade(self,grade):
        self._grades.append(grade)

    def remove_grade(self,grade):
        for i,g in enumerate(self._grades):
            if(g.student_id==grade.student_id) and (g.discipline_id==grade.discipline_id) and (g.grade_value==grade.grade_value):
                del self._grades[i]
                return


    def list_grades(self):
        return list(self._grades)

    def remove_grades_student(self,st):
        self._grades=[
            g for g in self._grades
            if g.student_id!=st
        ]

    def remove_grades_discipline(self,dis):
        self._grades = [
            g for g in self._grades
            if g.discipline_id != dis
        ]

