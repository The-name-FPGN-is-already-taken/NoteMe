import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from note import Note

note1 = list()


class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("nota.ui", self)
        self.loginButton.clicked.connect(self.LoginToHomeweek)

    def LoginToHomeweek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


class HomeWeek_window(QDialog):
    def __init__(self):
        super(HomeWeek_window, self).__init__()
        loadUi("home_week.ui", self)
        self.currentDay = -1  # ยังไม่เลือกวัน = Today, Monday =0 .... Sunday = 6
        self.signOutButton.clicked.connect(self.homeWeekToLogin)
        self.calendar_tab.clicked.connect(self.homeWeekToHomeCal)
        self.noteButton.clicked.connect(self.homeWeekToNoteWindow)
        self.taskButton.clicked.connect(self.homeWeekToTaskWindow)
        # self.monday_button.clicked.connect(self.setCurrentDay(0))
    #     self.tuesday_button.clicked.connect(self.setCurrentDay(1))

    def setCurrentDay(self, day=-1):
        self.currentDay = day
        print(self.currentDay)

    def homeWeekToLogin(self):
        loginWindow = LoginWindow()
        widget.addWidget(loginWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def homeWeekToHomeCal(self):
        homeCal_window = HomeCal_window()
        widget.addWidget(homeCal_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def homeWeekToNoteWindow(self):
        note_window = Note_window()
        widget.addWidget(note_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def homeWeekToTaskWindow(self):
        task_window = Task_window()
        widget.addWidget(task_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
    # def setColor(self,A_button ,B_button ): #A_button เป็นปุ่มที่เราไปกด B_button เป็นปุ่มที่เรากำลังอยู่
    #     A_button.setStyleSheet('QPushButton {background: #FFAC4B; color: white; border_radius: 8px; width: 40px;   }')
    #     B_button.setStyleSheet('QPushButton {background: rgb(228, 226, 199); color: white; border_radius: 8px; width: 40px;   }')

    def setColor(self):
        self.monday_button.setStyleSheet(
            'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')
        self.tuesday_button.setStyleSheet(
            'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')

# padding: 8px 0px;
# color: rgb(255, 255, 255);
# width: 40px;
# left: calc(50% - 40px/2 - 189.71px);
# background: #FFAC4B;
# border-radius: 8px;


class HomeCal_window(QDialog):
    def __init__(self):
        super(HomeCal_window, self).__init__()
        loadUi("home_cal.ui", self)
        self.signOutButton.clicked.connect(self.homeCalToLogin)
        self.weekView_tab.clicked.connect(self.homeCalToHomeWeek)
        self.noteButton.clicked.connect(self.homeCalToNoteWindow)

    def homeCalToLogin(self):
        loginWindow = LoginWindow()
        widget.addWidget(loginWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def homeCalToHomeWeek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def homeCalToNoteWindow(self):
        note_window = Note_window()
        widget.addWidget(note_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Note_window(QDialog):
    def __init__(self):
        super(Note_window, self).__init__()
        loadUi("note_window.ui", self)
        self.addNote.clicked.connect(self.goToAddNote)
        self.homeButton.clicked.connect(self.noteWindowToHomeWeek)
        self.taskButton.clicked.connect(self.goToTaskWindow)

        self.listWidget.clear()

        try:
            note1
        except NameError:
            print("well, it WASN'T defined after all!")
        else:
            print("sure, it was defined.")
            for i in range(len(note1)):
                print(note1[i].notename)
                self.listWidget.addItem(note1[i].notename)
        # try:
        #     note1
        # except NameError:
        #     note1 = None
        # else:
        #     for i in range(len(note1)):
        #         print(note1[i].notename)
        #         self.listWidget.addItem(note1[i].notename)

    def goToAddNote(self):
        addNoteWindow = AddNoteWindow()
        widget.addWidget(addNoteWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def homeCalToHomeWeek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def noteWindowToHomeWeek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToTaskWindow(self):
        task_window = Task_window()
        widget.addWidget(task_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


class AddNoteWindow(QDialog):
    def __init__(self):
        super(AddNoteWindow, self).__init__()
        loadUi("add_note.ui", self)
        self.addNote.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.addNoteWindowToHomeWeek)
        self.taskButton.clicked.connect(self.goToTaskWindow)

        self.saveNoteButton.clicked.connect(self.saveNote)
        self.cancelAdding.clicked.connect(self.cancelNote)

    def saveNote(self):
        note1.append(Note(self.textEdit.toPlainText(),
                          self.plainTextEdit.toPlainText()))
        self.textEdit.clear()
        self.plainTextEdit.clear()
        print("Saved")

    def cancelNote(self):
        self.textEdit.clear()
        self.plainTextEdit.clear()
        print("UnSaved")

    def goToTaskWindow(self):
        task_window = Task_window()
        widget.addWidget(task_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToNoteWindow(self):
        note_window = Note_window()
        widget.addWidget(note_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def addNoteWindowToHomeWeek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Task_window(QDialog):
    def __init__(self):
        super(Task_window, self).__init__()
        loadUi("task_window.ui", self)
        self.addTask.clicked.connect(self.goToAddTask)
        self.noteButton.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.taskWindowToHomeWeek)

    def goToAddTask(self):
        addTaskWindow = AddTaskWindow()
        widget.addWidget(addTaskWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToNoteWindow(self):
        note_window = Note_window()
        widget.addWidget(note_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def taskWindowToHomeWeek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


class AddTaskWindow(QDialog):
    def __init__(self):
        super(AddTaskWindow, self).__init__()
        loadUi("add_task_window.ui", self)
        self.unAddTask.clicked.connect(self.goToTaskWindow)
        self.noteButton.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.addTaskWindowToHomeWeek)

    def goToTaskWindow(self):
        task_window = Task_window()
        widget.addWidget(task_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToNoteWindow(self):
        note_window = Note_window()
        widget.addWidget(note_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def addTaskWindowToHomeWeek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginWindow = LoginWindow()
widget.addWidget(loginWindow)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("No im not out!")
