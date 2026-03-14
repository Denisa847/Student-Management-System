from jproperties import Properties
from src.services.StudentService import StudentService
from src.services.DisciplineService import DisciplineService
from src.services.GradeService import GradeService
from src.commands.Manager import Manager
from src.ui.Ui import Ui
from src.repository.MemoryRepository import MemoryRepository
from src.repository.TextRepository import TextRepository
from src.repository.BinaryRepository import BinaryRepository


def get_repo():
    configs=Properties()
    with open('settings.properties', 'rb') as configFile:
        configs.load(configFile)

    repo_string=configs.get("REPO").data
    repo=""
    if repo_string == "Memory":
        repo = MemoryRepository()
    elif repo_string == "Text":
        stud_file=configs.get("STUDENT_TEXT").data
        dis_file=configs.get("DISCIPLINE_TEXT").data
        grade_file=configs.get("GRADE_TEXT").data
        repo = TextRepository(stud_file,dis_file,grade_file)
    elif repo_string == "Binary":
        stud_file = configs.get("STUDENT_BIN").data
        dis_file = configs.get("DISCIPLINE_BIN").data
        grade_file = configs.get("GRADE_BIN").data
        repo = BinaryRepository(stud_file,dis_file,grade_file)
    return repo

def start():
    repo=get_repo()
    manager=Manager()
    student_service=StudentService(repo,manager)
    discipline_service=DisciplineService(repo,manager)
    grade_service=GradeService(repo,manager)

    ui=Ui(student_service,discipline_service,grade_service,manager)
    ui.main()

start()