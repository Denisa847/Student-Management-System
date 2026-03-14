
from src.repository.MemoryRepository import MemoryRepository

class Command:
    def undo(self):
        raise NotImplementedError

    def redo(self):
        raise NotImplementedError


class AddStudentCommand(Command):
    def __init__(self,repo,student):
        self._repo=repo
        self._student=student

    def undo(self):
        self._repo.remove_student(self._student.id)

    def redo(self):
        self._repo.add_student(self._student)


class RemoveStudentCommand(Command):
    def __init__(self,repo,student,remove_grades):
        self._repo=repo
        self._student=student
        self._remove_grades=remove_grades

    def undo(self):
        self._repo.add_student(self._student)
        for g in self._remove_grades:
            self._repo.add_grade(g)

    def redo(self):
        self._repo.remove_grades_student(self._student.id)
        self._repo.remove_student(self._student.id)

class UpdateStudentCommand(Command):
    def __init__(self, repo, old_student, new_student):
        self._repo = repo
        self._old_student = old_student
        self._new_student = new_student

    def undo(self):
        self._repo.update_student(self._old_student)

    def redo(self):
        self._repo.update_student(self._new_student)



class AddDisciplineCommand(Command):
    def __init__(self, repo, discipline):
        self._repo = repo
        self._discipline =discipline

    def undo(self):
        self._repo.remove_discipline(self._discipline.id)

    def redo(self):
        self._repo.add_discipline(self._discipline)


class RemoveDisciplineCommand(Command):
    def __init__(self, repo, discipline,remove_grades):
        self._repo = repo
        self._discipline =discipline
        self._remove_grades=remove_grades

    def undo(self):
        self._repo.add_discipline(self._discipline)
        for g in self._remove_grades:
            self._repo.add_grade(g)


    def redo(self):
        self._repo.remove_grades_discipline(self._discipline.id)
        self._repo.remove_discipline(self._discipline.id)


class UpdateDisciplineCommand(Command):
    def __init__(self, repo, old_discipline, new_discipline):
        self._repo = repo
        self._old_discipline = old_discipline
        self._new_discipline = new_discipline

    def undo(self):
        self._repo.update_discipline(self._old_discipline)

    def redo(self):
        self._repo.update_discipline(self._new_discipline)

class AddGradeCommand(Command):
    def __init__(self,repo,grade):
        self._repo=repo
        self._grade=grade

    def undo(self):
        self._repo.remove_grade(self._grade)

    def redo(self):
        self._repo.add_grade(self._grade)


