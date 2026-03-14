from src.domain.Grade import Grade
from src.domain.Student import Student
from src.domain.Discipline import Discipline
from src.repository.MemoryRepository import MemoryRepository
import random
from src.commands.Manager import Manager
from src.commands.Commands import AddGradeCommand
import statistics

class GradeService:
    def __init__(self,repo,manager):
        self._repo=repo
        self._history = manager
        self.generate_random_grades()



    def has_grades(self):
        return len(self._repo.list_grades())>0

    def generate_random_grades(self):

        if self.has_grades():
            return
        students=self._repo.get_all_students()
        disciplines=self._repo.get_all_disciplines()

        if not students or not disciplines:
            print("No students or disciplines")
            return

        for _ in range(20):
            student=random.choice(students)
            discipline=random.choice(disciplines)
            grade_value=round(random.uniform(2,10),2)
            self._repo.add_grade(Grade(discipline.id,student.id,grade_value))

    def add_grade(self, discipline_id, student_id, grade_value):
        if student_id not in self._repo._students:
            raise ValueError("Student ID is not in the list")
        if discipline_id not in self._repo._disciplines:
            raise ValueError("Discipline ID is not in the list")
        if not (0<grade_value<11):
            raise ValueError("Grade must be between 1 and 10")
        grade = Grade(discipline_id, student_id, grade_value)
        self._repo.add_grade(grade)
        self._history.record(AddGradeCommand(self._repo,grade))

    def list_grades(self):
        return self._repo.list_grades()

    def remove_grades_for_students(self, student_id):
        self._repo.remove_grades_student(student_id)

    def remove_grades_for_discipline(self, discipline_id):
        self._repo.remove_grades_discipline(discipline_id)

    def students_failing(self):
        grades=self._repo.list_grades()
        students=self._repo.get_all_students()

        grade_map={}
        for g in grades:
            key=(g.student_id, g.discipline_id)
            grade_map.setdefault(key,[]).append(g.grade_value)

        failig_students=set()
        for(student_id,_), values in grade_map.items():
            avg=statistics.mean(values)
            if avg<5:
                failig_students.add(student_id)

        return [
            student for student in students
            if student.id in failig_students
        ]

    def students_best_situation(self):
        grades = self._repo.list_grades()
        students = self._repo.get_all_students()

        data={}
        for g in grades:
            data.setdefault(g.student_id,{})
            data[g.student_id].setdefault(g.discipline_id,[])
            data[g.student_id][g.discipline_id].append(g.grade_value)

        results=[]
        for student in students:
            if student.id not in data:
                continue
            discipline_averages=[
                statistics.mean(values)
                for values in data[student.id].values()]

            aggregated_avg=statistics.mean(discipline_averages)
            results.append((student,aggregated_avg))

        results.sort(key=lambda x:x[1],reverse=True)
        return results

    def disciplines_by_average_grade(self):
        grades = self._repo.list_grades()
        disciplines = self._repo.get_all_disciplines()
        disciplines_grade={}
        for g in grades:
            disciplines_grade.setdefault(g.discipline_id,[]).append(g.grade_value)

        result=[]
        for d in disciplines:
            if d.id in disciplines_grade:
                avg=sum(disciplines_grade[d.id])/len(disciplines_grade[d.id])
                result.append((d,avg))

        result.sort(key=lambda x: x[1], reverse=True)
        return result




