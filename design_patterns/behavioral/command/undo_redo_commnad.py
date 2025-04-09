# the Command pattern helps to track the history of executed operations and
#  makes it possible to revert an operation if needed.

from abc import ABC, abstractmethod

class Editor:
    def __init__(self, text=""):
        self.text = ""
    
    def getSelection(self):
        # logic to return the selection
        return self.text
    
    def deleteSelection(self):
        # delete the selected text
        return True
    
    def replaceSelection(self):
        # paste the selection
        return True
        
    
class Command:
    def __init__(self):
        pass

class CopyCommand:
    pass

class CutCommand:
    pass

class PasteCommand:
    pass

class UndoCommand:
    pass


class Application:
    def __init__(self, activeEditor):
        self.editors = []
        self.activeEditor = activeEditor

class History:
    def __init__(self):
        self.history_cmd = []
        self.redo = []
    
    def pushCmd(self, command):
        self.history_cmd.append(command)
    
    def undoCmd(self, command):
        cmd =  self.history_cmd.pop()
        self.redo.append(command)
        return cmd

    def redoCmd(self, command):
        cmd = self.redo.pop()
        self.history_cmd.append(cmd)
        return cmd


        
    
    

