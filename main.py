import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
<<<<<<< Updated upstream
=======
from testCSV import *
>>>>>>> Stashed changes
from note import Note

<<<<<<< Updated upstream
note1 = list()
=======

timetask = list()
>>>>>>> Stashed changes


class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("nota.ui", self)
<<<<<<< Updated upstream
        self.loginButton.clicked.connect(self.LoginToHomeweek)
=======
        self.loginButton.clicked.connect(self.loginIn)
        self.signupButton.clicked.connect(self.LoginToSignUp)
        # self.welComeUser.setText(nota.)

    def loginIn(self):
        global userName
        userName = self.username.text()
        # print(userName)
        # print(password)
        try:
            password = int(self.userPassword.text())
        except ValueError:
            password = 1234

        nota.login(userName, password)
        if nota.isLogin:
            self.LoginToHomeweek()
>>>>>>> Stashed changes

    def LoginToHomeweek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
<<<<<<< Updated upstream
=======
        widget.setCurrentIndex(widget.currentIndex()+1)

    def LoginToSignUp(self):
        signUpWindow = SignUpWindow()
        widget.addWidget(signUpWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)


class SignUpWindow(QDialog):
    def __init__(self):
        super(SignUpWindow, self).__init__()
        loadUi("signUp_temp.ui", self)
        self.signUpButton.clicked.connect(self.registing)
        # self.welComeUser.setText(nota.)

    def registing(self):
        global userName
        userName = self.username.text()
        # print(userName)
        password = int(self.userPassword.text())
        # print(password)
        nota.registor(userName, password)
        if nota.isLogin:
            self.goToHomeWeekWindow()

    def goToHomeWeekWindow(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        # self.monday_button.clicked.connect(self.setCurrentDay(0))
    #     self.tuesday_button.clicked.connect(self.setCurrentDay(1))

    def setCurrentDay(self, day=-1):
        self.currentDay = day
        print(self.currentDay)
=======

        self.welcomeUser.setText("Welcome ,  "+userName)

        x = datetime.datetime.now()
        self.date.setText(x.strftime("%B")+' ' +
                          x.strftime("%d")+', '+x.strftime("%Y"))

        self.listDayButton = list()
        self.listDayButton.append(self.monday_button)
        self.listDayButton.append(self.tuesday_button)
        self.listDayButton.append(self.wednesday_button)
        self.listDayButton.append(self.thursday_button)
        self.listDayButton.append(self.friday_button)
        self.listDayButton.append(self.saturday_button)
        self.listDayButton.append(self.sunday_button)

        for i in range(len(self.listDayButton)):

            # SET TEXT
            self.listDayButton[i].setText((nota.showDateOfToday()+datetime.timedelta(days=i)).strftime(
                "%A")+"\n"+str((nota.showDateOfToday()+datetime.timedelta(days=i)).day))

            # SET clicked connect
            self.listDayButton[i].clicked.connect(self.setCurrent)

    def setCurrent(self):
        for i in range(len(self.listDayButton)):
            if self.listDayButton[i].objectName() == self.sender().objectName():
                # print(self.sender().objectName())
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')
            else:
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
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
=======
>>>>>>> Stashed changes


class HomeCal_window(QDialog):
    def __init__(self):
        super(HomeCal_window, self).__init__()
        loadUi("home_cal.ui", self)
<<<<<<< Updated upstream
=======
        self.currentbutton = -1
>>>>>>> Stashed changes
        self.signOutButton.clicked.connect(self.homeCalToLogin)
        self.weekView_tab.clicked.connect(self.homeCalToHomeWeek)
        self.noteButton.clicked.connect(self.homeCalToNoteWindow)

<<<<<<< Updated upstream
=======
        # self.month1_button.clicked.connect(self.setCurrentMon)
        # self.month2_button.clicked.connect(self.setCurrentTue)
        # self.month3_button.clicked.connect(self.setCurrentWed)
        # self.month4_button.clicked.connect(self.setCurrentThurs)
        # self.month5_button.clicked.connect(self.setCurrentFri)
        # self.month6_button.clicked.connect(self.setCurrentSat)
        # self.month7_button.clicked.connect(self.setCurrentSun)
        # self.monday_button.setText("Monday\n"+str(nota.showDateOfToday().weekday()))
        # self.month1_button.setText(nota.showDateOfToday().strftime("%A")+"\n"+str((nota.showDateOfToday()+datetime.timedelta(days = 0)).day))
        # self.month2_button.setText((nota.showDateOfToday()+datetime.timedelta(days = 1)).strftime("%A")+"\n"+str((nota.showDateOfToday()+datetime.timedelta(days =1)).day))
        # self.month3_button.setText((nota.showDateOfToday()+datetime.timedelta(days = 2)).strftime("%A")+"\n"+str((nota.showDateOfToday()+datetime.timedelta(days = 2)).day))
        # self.month4_button.setText((nota.showDateOfToday()+datetime.timedelta(days = 3)).strftime("%A")+"\n"+str((nota.showDateOfToday()+datetime.timedelta(days = 3)).day))
        # self.month5_button.setText((nota.showDateOfToday()+datetime.timedelta(days = 4)).strftime("%A")+"\n"+str((nota.showDateOfToday()+datetime.timedelta(days = 4)).day))
        # self.month6_button.setText((nota.showDateOfToday()+datetime.timedelta(days = 5)).strftime("%A")+"\n"+str((nota.showDateOfToday()+datetime.timedelta(days = 5)).day))
        # self.month7_button.setText((nota.showDateOfToday()+datetime.timedelta(days = 6)).strftime("%A")+"\n"+str((nota.showDateOfToday()+datetime.timedelta(days = 6)).day))

        self.welcomeUser.setText("Welcome ,  "+userName)

        x = datetime.datetime.now()
        self.date.setText(x.strftime("%B")+' ' +
                          x.strftime("%d")+', '+x.strftime("%Y"))

        self.listCalendarButton = list()
        self.listCalendarButton.append(self.month1_button)
        self.listCalendarButton.append(self.month2_button)
        self.listCalendarButton.append(self.month3_button)
        self.listCalendarButton.append(self.month4_button)
        self.listCalendarButton.append(self.month5_button)
        self.listCalendarButton.append(self.month6_button)
        self.listCalendarButton.append(self.month7_button)

        for i in range(len(self.listCalendarButton)):
            # SET TEXT MONTH
            self.listCalendarButton[i].setText((nota.showDateOfToday()+datetime.timedelta(
                days=+i)).strftime("%b")+"\n"+str((nota.showDateOfToday()+datetime.timedelta(days=i)).month))

            self.listCalendarButton[i].clicked.connect(self.setCurrent)

    def setCurrent(self):
        for i in range(len(self.listCalendarButton)):
            if self.listCalendarButton[i].objectName() == self.sender().objectName():
                # print(self.sender().objectName())
                self.listCalendarButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')
            else:
                self.listCalendarButton[i].setStyleSheet(
                    'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')

>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
        try:
            note1
        except NameError:
            print("well, it WASN'T defined after all!")
        else:
            print("sure, it was defined.")
            for i in range(len(note1)):
                print(note1[i].notename)
                self.listWidget.addItem(note1[i].notename)
<<<<<<< Updated upstream
        # try:
        #     note1
        # except NameError:
        #     note1 = None
        # else:
        #     for i in range(len(note1)):
        #         print(note1[i].notename)
        #         self.listWidget.addItem(note1[i].notename)
=======
=======
        #  CANT USE   Fri Nov 26 1:44:50 AM
        global notelst
        notelst = nota.getNoteAll()
        for i in range(len(notelst)):
            # print(notelst[i].topic)
            print("Topic:", notelst[i].topic,
                  "des:", notelst[i].description,
                  "I:", i)
            self.listWidget.addItem(notelst[i].top)

>>>>>>> Stashed changes
        global userName
        self.welcomeUser.setText("Welcome ,  "+userName)
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
=======
        global userName
        self.welcomeUser.setText("Welcome, "+userName)
# NUT
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
=======
        global userName
        self.welcomeUser.setText("Welcome, "+userName)
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
        global userName
        self.welcomeUser.setText("Welcome, "+userName)
>>>>>>> Stashed changes
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        self.saveNoteButton.disconnect()
        self.saveNoteButton.clicked.connect(self.addTask)
        self.cancelAdding.clicked.connect(self.cancelTask)
        global userName
        self.welcomeUser.setText("Welcome ,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

        if self.sender().objectName() == "listWidget":
<<<<<<< Updated upstream
            indextask = self.sender().currentRow()
            self.taskName_textEdit.setPlainText(tasklst[indextask].topic)
            self.task_description.setPlainText(tasklst[indextask].description)
            self.dateTimeEdit.setDateTime(tasklst[indextask].dateTarget)
=======
            self.indextask = self.sender().currentRow()
            self.taskName_textEdit.setPlainText(tasklst[self.indextask].topic)
            self.task_description.setPlainText(
                tasklst[self.indextask].description)
            self.dateTimeEdit.setDateTime(tasklst[self.indextask].dateTarget)
>>>>>>> Stashed changes
            self.saveNoteButton.disconnect()
            self.saveNoteButton.clicked.connect(self.saveTask)
            self.saveNoteButton.setText("SAVE")

<<<<<<< Updated upstream
            print(tasklst[indextask].taskID)
=======
            print(tasklst[self.indextask].taskID)
>>>>>>> Stashed changes
            # indextask = self.listWidget.currentRow()
        # print(tasklst[indextask].topic)

        # addTaskWindow.task_description.setPlainText(
        #     tasklst[indextask].description)
        # addTaskWindow.taskName_textEdit.setPlainText(tasklst[indextask].topic)
        # timetarget = tasklst[indextask].dateTarget
        # print(timetarget)
        # print(type(timetarget))
        # addTaskWindow.dateTimeEdit.setDateTime(timetarget)
        print("------>", self.sender().objectName())
        print("------>", self.taskName_textEdit.toPlainText())
        print("------>", self.task_description.toPlainText())

    def saveTask(self):
<<<<<<< Updated upstream
        print("WTF")
=======
        print("------>", self.indextask)
        tasklst[self.indextask].topic = self.taskName_textEdit.toPlainText()
        tasklst[self.indextask].description = self.task_description.toPlainText()
        time = self.dateTimeEdit.dateTime()
        time = time.toPyDateTime()
        tasklst[self.indextask].dateTarget = time
        nota.editRecord(tasklst[self.indextask])
        self.taskName_textEdit.clear()
        self.task_description.clear()
        self.goToTaskWindow()

    def addTask(self):
>>>>>>> Stashed changes

    def addTask(self):
        # M/d/yy h:mm AP
        time = self.dateTimeEdit.dateTime()
        # yy/m/d h:mm:ss
        time = time.toPyDateTime()
        print(str(time))
        # print(str(self.taskName_textEdit.toPlainText()))
        # print(str(self.task_description.toPlainText()))
        nota.addRecord(time, 0, self.taskName_textEdit.toPlainText(),
                       self.task_description.toPlainText())
        self.taskName_textEdit.clear()
        self.task_description.clear()
        # self.task_description.overwriteMode(True)
        print("------S", self.sender().objectName())
        print("------S", self.taskName_textEdit.toPlainText())
        print("------S", self.task_description.toPlainText())
        self.goToTaskWindow()

    def cancelTask(self):
        self.taskName_textEdit.clear()
        self.task_description.clear()
        print("------C", self.sender().objectName())
        print("------C", self.taskName_textEdit.toPlainText())
        print("------C", self.task_description.toPlainText())
        print("UnSaved")
        self.goToTaskWindow()
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
=======
global nota
nota = Nota()
>>>>>>> Stashed changes
widget.addWidget(loginWindow)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("No im not out!")
