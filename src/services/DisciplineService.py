from src.domain.Discipline import Discipline
from src.repository.MemoryRepository import MemoryRepository
from src.commands.Manager import Manager
from src.commands.Commands import AddDisciplineCommand, RemoveDisciplineCommand, UpdateDisciplineCommand

class DisciplineService:
    def __init__(self, repo,manager):
        self._repo=repo
        self._history = manager
        self.generate_random_disciplines()


    def generate_random_disciplines(self):
        """
        generates rnadom disciplines
        """
        self._repo.clear_disciplines()
        list_of_disciplines = ["Fundamentals of Programming",
                                   "French", "English", "History", "Economics",
                                   "Algebra", "Computational Logic", "Mathematical Analysis",
                                   "Art", "Psychology", "Chemistry", "Geometry", "Sport", "Physics",
                                   "Computer System Architecture",
                                   "Dynamical Systems", "Statistics", "Music", "Geography",
                                   "Object Oriented Programming"]

        for i in range(len(list_of_disciplines)):
                discipline_id = i + 1
                name = list_of_disciplines[i]
                self._repo.add_discipline(Discipline(discipline_id, name))

    def add_discipline(self, discipline_id: int, name: str):
        """
        add a discipline if it does not already exsts, calling the right function from repo
        """
        new_discipline = Discipline(discipline_id, name)
        self._repo.add_discipline(new_discipline)
        self._history.record(AddDisciplineCommand(self._repo, new_discipline))

    def list_disciplines(self):
        """
        get all the disciplines
        """
        return self._repo.get_all_disciplines()

    def remove_discipline(self, discipline_id):
        """
        remove a discipline if it finds it and all the grades student got at that discipline
        """
        discipline= self._repo.get_discipline(discipline_id)
        remove_grades = [g for g in self._repo.list_grades()
                         if g.discipline_id == discipline_id
                         ]
        self._repo.remove_grades_discipline(discipline_id)
        self._repo.remove_discipline(discipline_id)
        self._history.record(RemoveDisciplineCommand(self._repo, discipline, remove_grades))

    def update_discipline(self, discipline_id, name):
        """
        search the disicpline by id and update the discipline with what users provided
        """
        old_discipline = self._repo.get_discipline(discipline_id)
        updated_discipline = Discipline(discipline_id, name)
        self._repo.update_discipline(updated_discipline)
        self._history.record(UpdateDisciplineCommand(self._repo, old_discipline, updated_discipline))

    def search_discipline(self,text):
        text=text.lower()
        results=[]
        for discipline in self._repo.get_all_disciplines():
            if text.isdigit() and int(text)==discipline.id:
                results.append(discipline)
                continue

            if text in discipline.name.lower():
                results.append(discipline)

        return results