
class Discipline:
    def __init__(self,discipline_id,name):
        self.__id=discipline_id
        self.__name=name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"{self.id} {self.name}"
