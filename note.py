import time
class Note:
    def __init__(self, notename="", notefield="", time=time.time()):
        self.notename = notename
        self.notefield = notefield
        self.noteTime = time

    def get_notename(self):
        return self.notename

    def get_notefield(self):
        return self.notefield

    def get_noteTime(self):
        return self.noteTime