import src.commands.Commands

class Manager:
    def __init__(self):
        self._undo_stack=[]
        self._redo_stack=[]

    def record(self,command):
        self._undo_stack.append(command)
        self._redo_stack.clear()

    def undo(self):
        if not self._undo_stack:
            raise Exception("Nothing to undo")
        command = self._undo_stack.pop()
        command.undo()
        self._redo_stack.append(command)

    def redo(self):
        if not self._redo_stack:
            raise Exception("Nothing to redo")
        command = self._redo_stack.pop()
        command.redo()
        self._undo_stack.append(command)








