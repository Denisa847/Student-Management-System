import random
from faker import Faker
from src.domain.Student import Student
from src.commands.Manager import Manager
from src.commands.Commands import AddStudentCommand, RemoveStudentCommand, UpdateStudentCommand

class StudentService:
    def __init__(self,repo,manager):
        self._repo=repo
        self._history = manager
        self.generate_random_students()


    def generate_random_students(self):
        """
        This function adds random student using faker to generate random numbers
        :return:
        """
        self._repo.clear_students()
        fake=Faker()
        for i in range(20):
            student_id=i+1
            name=fake.name()
            self._repo.add_student(Student(student_id,name))

    def add_student(self,student_id, name):
        """
        adds a new student if the same student wth the same id does not already exists, callinf the function in repo
        which check that
        """
        new_student=Student(student_id,name)
        self._repo.add_student(new_student)
        self._history.record(AddStudentCommand(self._repo,new_student))


    def list_students(self):
        """
        this functions will get all the students
        """
        return self._repo.get_all_students()

    def remove_student(self, student_id):
        """
        Will remove a student by id and its grades as well
        """
        student=self._repo.get_student(student_id)
        remove_grades=[g for g in self._repo.list_grades()
                       if g.student_id==student_id
                       ]

        self._repo.remove_grades_student(student_id)
        self._repo.remove_student(student_id)
        self._history.record(RemoveStudentCommand(self._repo, student, remove_grades))

    def update_student(self, student_id, name):
        """
        will search the student and when it finds it it will update it
        """
        old_student=self._repo.get_student(student_id)
        update_student = Student(student_id, name)
        self._repo.update_student(update_student)
        self._history.record(UpdateStudentCommand(self._repo,old_student,update_student))

    def search_student(self,text):
        text=text.lower()
        results=[]
        for student in self._repo.get_all_students():
            if text.isdigit() and int(text)==student.id:
                results.append(student)
                continue

            if text in student.name.lower():
                results.append(student)

        return results