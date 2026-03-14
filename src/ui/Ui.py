from src.services.StudentService import StudentService
from src.services.DisciplineService import DisciplineService
from src.services.GradeService import GradeService
from src.repository.MemoryRepository import MemoryRepository
from src.repository.TextRepository import TextRepository
from src.repository.BinaryRepository import BinaryRepository
from src.repository.RepositoryException import RepositoryException
from src.commands.Manager import Manager

class Ui:
    def __init__(self,student_service,discipline_service, grade_service,manager):
        self._student_service=student_service
        self._discipline_service= discipline_service
        self._grade_service=grade_service
        self._manager=manager

    def ui_undo(self):
        try:
            self._manager.undo()
            print("Undo successful")
        except Exception as e:
            print(e)

    def ui_redo(self):
        try:
            self._manager.redo()
            print("Redo successful")
        except Exception as e:
            print(e)

    def ui_add_student(self):
        student_id = input("Student ID: ")
        try:
            student_id = int(student_id)
            if student_id <= 0:
                raise ValueError
        except ValueError:
            print("Student ID must be a positive integer")
            return

        name = input("Name: ")
        if name=="":
            print("Name can not be empty")
            return

        try:
            self._student_service.add_student(student_id, name)
            print("Student added")
        except (RepositoryException,ValueError) as e:
            print(e)


    def ui_failing_students(self):
        result=self._grade_service.students_failing()
        if not result:
            print("No one is failing")
            return

        print("Students failing: ")
        for s in result:
            print(s)

    def ui_list_student(self):
        print("\nStudents: ")
        for s in self._student_service.list_students():
            print(s)

    def ui_remove_student(self):
        student_id = input("Student ID to remove: ")
        try:
            student_id = int(student_id)
            if student_id <= 0:
                raise ValueError
        except ValueError:
            print("Student ID must be a positive integer")
            return

        try:
            self._student_service.remove_student(student_id)
            print("Student removed")
        except (RepositoryException,ValueError) as e:
            print(e)

    def ui_update_student(self):
        student_id = input("Student ID to update: ")
        try:
            student_id = int(student_id)
            if student_id <= 0:
                raise ValueError
        except ValueError:
            print("Student ID must be a positive integer")
            return

        name = input("New name: ")
        try:
            self._student_service.update_student(student_id, name)
            print("Student updated")
        except (RepositoryException,ValueError) as v:
            print(v)

    def ui_add_discipline(self):
        discipline_id = input("Discipline ID: ")
        try:
            discipline_id = int(discipline_id)
            if discipline_id <= 0:
                raise ValueError
        except ValueError:
            print("Discipline ID must be a positive integer")
            return

        name = input("Name: ")
        if name=="":
            print("Name can not be empty")
            return

        try:
            self._discipline_service.add_discipline(discipline_id, name)
            print("Discipline added")
        except (RepositoryException,ValueError) as e:
            print(e)

    def ui_list_discipline(self):
        print("\nDisciplines: ")
        for d in self._discipline_service.list_disciplines():
            print(d)

    def ui_remove_discipline(self):
        discipline_id = input("Discipline ID to remove: ")
        try:
            discipline_id = int(discipline_id)
            if discipline_id <= 0:
                raise ValueError
        except ValueError:
            print("Discipline ID must be a positive integer")
            return

        try:
            self._discipline_service.remove_discipline(discipline_id)
            print("Discipline removed")
        except (RepositoryException,ValueError) as e:
            print(e)

    def ui_update_discipline(self):
        discipline_id = input("Discipline ID to update: ")
        try:
            discipline_id = int(discipline_id)
            if discipline_id <= 0:
                raise ValueError
        except ValueError:
            print("Discipline ID must be a positive integer")
            return

        name = input("New name: ")
        try:
            self._discipline_service.update_discipline(discipline_id, name)
            print("Discipline updated")
        except (RepositoryException,ValueError) as v:
            print(v)

    def ui_add_grade(self):
        try:
            discipline_id=int(input("Displine ID: "))
            student_id=int(input("Student ID: "))
            value=float(input("Grade: "))
        except ValueError:
                print("Wronf input ")
                return

        try:
            self._grade_service.add_grade(discipline_id,student_id,value)
            print("Graded added")
        except ValueError as e:
            print(e)

    def ui_list_grades(self):
        for g in self._grade_service.list_grades():
            print(g)


    def ui_search_student(self):
        text=input("Search text(ID or name): ").strip()
        results=self._student_service.search_student(text)

        if not results:
            print("No matching student")
            return
        print("Matching students: ")
        for s in results:
            print(s)

    def ui_search_discipline(self):
        text = input("Search text(ID or name): ").strip()
        results = self._discipline_service.search_discipline(text)

        if not results:
            print("No matching discipline")
            return
        print("Matching discipline: ")
        for d in results:
            print(d)

    def ui_students_best_situation(self):
        results=self._grade_service.students_best_situation()

        if not results:
            print("No data available")
            return

        for student,avg in results:
            print(f"{student}: average {avg:.2f}")


    def ui_disciplines_by_avg(self):
        results=self._grade_service.disciplines_by_average_grade()

        if not results:
            print("No grades available")
            return

        for d,avg in results:
            print(f"{d.id} {d.name}: average {avg:.2f}")

    def print_menu(self):
        print("\n==== MENU ====")
        print("1. Manage students")
        print("2. Manage disciplines")
        print("3. Manage grade")
        print("4. Undo")
        print("5. Redo")
        print("6. Students failing")
        print("7. Best students based on aggregate average")
        print("8. Disciplie averages")
        print("0. Exit")


    def print_grade_menu(self):
        print("\n-- Grades Menu --")
        print("1.Add grade")
        print("2.Display grade")
        print("0.Back")

    def print_student_menu(self):
        print("\n-- Student Menu --")
        print("1.Add student")
        print("2.Display students")
        print("3.Remove student")
        print("4.Update student")
        print("5.Search student")
        print("0.Back")

    def print_discipline_menu(self):
        print("\n-- Discipline Menu --")
        print("1.Add discipline")
        print("2.List disciplines")
        print("3.Remove discipline")
        print("4.Update discipline")
        print("5.Search discipline")
        print("0.Back")


    def students_menu(self):
        while True:
            self.print_student_menu()
            cmd=input("Student menu command: ")
            if cmd=="0":
                return
            elif cmd=="1":
                self.ui_add_student()
            elif cmd=="2":
                self.ui_list_student()
            elif cmd == "3":
                self.ui_remove_student()
            elif cmd == "4":
                self.ui_update_student()
            elif cmd=="5":
                self.ui_search_student()

            else: print("Invalid command\n")


    def discipline_menu(self):
        while True:
            self.print_discipline_menu()
            cmd=input("Discipline menu command: ")
            if cmd=="0":
                return
            elif cmd=="1":
                self.ui_add_discipline()
            elif cmd=="2":
                self.ui_list_discipline()
            elif cmd=="3":
                self.ui_remove_discipline()
            elif cmd=="4":
                self.ui_update_discipline()
            elif cmd=="5":
                self.ui_search_discipline()
            else:
                print("Invalid command\n")


    def grade_menu(self):
        while True:
            self.print_grade_menu()
            cmd = input("Discipline menu command: ")
            if cmd == "0":
                return
            elif cmd == "1":
                self.ui_add_grade()
            elif cmd=="2":
                self.ui_list_grades()
            else:
                print("Invalid command\n")

    def main(self):
        while True:
            self.print_menu()
            cmd=input("Command: ")

            if cmd=="0":
                print("Goodbye!\n")
                break
            elif cmd=="1":
                self.students_menu()
            elif cmd=="2":
                self.discipline_menu()
            elif cmd=="3":
                self.grade_menu()
            elif cmd=="4":
                self.ui_undo()
            elif cmd=="5":
                self.ui_redo()
            elif cmd == "6":
                self.ui_failing_students()
            elif cmd=="7":
                self.ui_students_best_situation()
            elif cmd=="8":
                self.ui_disciplines_by_avg()
            else:
                print("Invalid command")

