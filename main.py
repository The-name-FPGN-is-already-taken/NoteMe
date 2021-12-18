from datetime import time
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import center
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from notaBack import *

notelst = list()

timetask = list()


class LoginWindow(QDialog):

    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("nota.ui", self)
        self.warning.setVisible(False)
        self.loginButton.clicked.connect(self.loginIn)
        self.signupButton.clicked.connect(self.LoginToSignUp)
        print("wcLogin", widget.currentIndex())

    def loginIn(self):
        global userName
        userName = self.username.text()
        password = self.userPassword.text()
        nota.login(userName, password)

        if nota.isLogin():
            self.warning.setVisible(False)
            self.LoginToHomeweek()
        else:
            self.warning.setVisible(True)

    def LoginToHomeweek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def LoginToSignUp(self):
        signUpWindow = SignUpWindow()
        widget.addWidget(signUpWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)


class SignUpWindow(QDialog):
    def __init__(self):
        super(SignUpWindow, self).__init__()
        loadUi("signUp_temp.ui", self)
        self.warning.setVisible(False)
        self.signUpButton.clicked.connect(self.registing)
        self.signInButton.clicked.connect(self.goToLoginWindow)
        # self.welComeUser.setText(nota.)
        print("wc", widget.currentIndex())

    def registing(self):
        userName = self.username.text()
        password = self.userPassword.text()
        if nota.registor(userName, password):
            self.goToHomeWeekWindow()
        else:
            self.warning.setVisible(True)

    def goToHomeWeekWindow(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToLoginWindow(self):
        loginWindow = LoginWindow()
        widget.addWidget(loginWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)


class HomeWeek_window(QDialog):
    def __init__(self):
        super(HomeWeek_window, self).__init__()
        loadUi("home_week.ui", self)
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

        self.signOutButton.clicked.connect(self.signOut)
        self.noteButton.clicked.connect(self.homeWeekToNoteWindow)
        self.taskButton.clicked.connect(self.homeWeekToTaskWindow)
        self.timeTableButton.clicked.connect(self.goToTimeTableWindow)

        self.listDayButton = list()
        self.listDayButton.append(self.monday_button)
        self.listDayButton.append(self.tuesday_button)
        self.listDayButton.append(self.wednesday_button)
        self.listDayButton.append(self.thursday_button)
        self.listDayButton.append(self.friday_button)
        self.listDayButton.append(self.saturday_button)
        self.listDayButton.append(self.sunday_button)

        self.taskTray.clear()
        self.timeTableTray.clear()

        self.currentDay = -1  # ยังไม่เลือกวัน = Today, Monday =0 .... Sunday = 6
        if self.currentDay == -1:
            dayhw = datetime.datetime.now()
            dayhw = str(dayhw.strftime("%a"))
            print(dayhw)
            if dayhw == "Mon":
                self.currentDay = 0
            elif dayhw == "Tue":
                self.currentDay = 1
            elif dayhw == "Wed":
                self.currentDay = 2
            elif dayhw == "Thu":
                self.currentDay = 3
            elif dayhw == "Fri":
                self.currentDay = 4
            elif dayhw == "Sat":
                self.currentDay = 5
            elif dayhw == "Sun":
                self.currentDay = 6
            print(self.currentDay)
            global timetablelst, notelst
            timetablelst = nota.getTimetableAll(self.currentDay)
            self.timeTableTray.clear()
            for i in range(len(timetablelst)):
                self.timeTableTray.addItem(timetablelst[i].topic)

            global today_tasklst
            today_tasklst = nota.getTaskToday()
            Sort.sortTaskDateTarget(today_tasklst)
            for i in range(len(today_tasklst)):
                self.taskTray.addItem(today_tasklst[i].topic+(60-len(today_tasklst[i].topic))*" "
                                      + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))
            # self.timeTableTray.itemDoubleClicked.connect(self.goToAddTimetable)
            # self.timeTableTray.setSpacing(15)
# =======
#         global timetablelst
#         timetablelst = nota.getTimetableAll(self.currentDay)
#         self.taskTray.clear()
#         for i in range(len(timetablelst)):
#             self.taskTray.addItem(timetablelst[i].topic)
#         self.taskTray.itemDoubleClicked.connect(self.goToAddTimetable)
#         # self.taskTray.setSpacing(15)
# >>>>>>> parnBranch2.1.1

        for i in range(len(self.listDayButton)):

            # SET TEXT
            self.listDayButton[i].setText((nota.showDateOfToday()+datetime.timedelta(days=i)).strftime(
                "%A")+"\n"+str((nota.showDateOfToday()+datetime.timedelta(days=i)).day))
            # SET clicked connect
            self.listDayButton[i].clicked.connect(self.setCurrent)

    def goToAddTimetable(self):

        addTimeTableWindow = AddTimeTableWindow()
        widget.addWidget(addTimeTableWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signOut(self):
        nota.logout()
        self.homeWeekToLogin()

    def setCurrent(self):
        for i in range(len(self.listDayButton)):
            if self.listDayButton[i].objectName() == self.sender().objectName():
                # print(self.sender().objectName())
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')

                # Update listwidget taskTray
                nextday = (self.currentDay+i) % 7
                global timetablelst
                timetablelst = nota.getTimetableAll(nextday)
                self.timeTableTray.clear()
                for j in range(len(timetablelst)):
                    self.timeTableTray.addItem(timetablelst[j].topic)

                global today_tasklst
                today = datetime.datetime.now()
                x = today+datetime.timedelta(i)
                print("XXXXXXX,", x.date())
                today_tasklst = nota.getTaskByDate(x.date())
                Sort.sortTaskDateTarget(today_tasklst)
                self.taskTray.clear()
                for k in range(len(today_tasklst)):
                    self.taskTray.addItem(today_tasklst[k].topic+(60-len(today_tasklst[k].topic))*" "
                                          + str(today_tasklst[k].dateTarget.strftime("%H:%M:%S")))

                # self.timeTableTray.setSpacing(15)

            else:
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')

    def homeWeekToLogin(self):
        loginWindow = LoginWindow()
        widget.addWidget(loginWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def homeWeekToNoteWindow(self):
        note_window = Note_window()
        widget.addWidget(note_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def homeWeekToTaskWindow(self):
        task_window = Task_window()
        widget.addWidget(task_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToTimeTableWindow(self):
        timeTable_window = TimeTable_window()
        widget.addWidget(timeTable_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Note_window(QDialog):
    def __init__(self):
        super(Note_window, self).__init__()
        loadUi("note_window.ui", self)
        self.addNoteButton.clicked.connect(self.goToAddNote)
        self.homeButton.clicked.connect(self.goToHomeWeek)
        self.taskButton.clicked.connect(self.goToTaskWindow)
        self.timeTableButton.clicked.connect(self.goToTimeTableWindow)
        self.sortFromNewToOld = True
        self.sortButton.clicked.connect(self.sortNoteList)
        global userName
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

        self.noteTray.itemDoubleClicked.connect(self.showPopUp)

        self.noteTray.clear()
        global notelst
        notelst = nota.getNoteAll()

        Sort.sortNote(notelst, 1)  # new =1 ใหม่ขึ้นก่อน new =0  เก่ามาก่อน

        for i in range(len(notelst)):
            # self.noteTray.addItem(notelst[i].topic + (165-len(str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S"))) - len(
            #     notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S")))
            self.noteTray.addItem(notelst[i].topic++ (150-len(str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S"))) - len(
                notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S")))

    def sortNoteList(self):
        self.noteTray.clear()
        # global notelst
        notelst = nota.getNoteAll()
        if self.sortFromNewToOld:
            Sort.sortNote(notelst, 0)
            for i in range(len(notelst)):

                self.noteTray.addItem(notelst[i].topic + (150-len(str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S"))) - len(

                    notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S")))

        else:
            Sort.sortNote(notelst, 1)
            for i in range(len(notelst)):

                self.noteTray.addItem(notelst[i].topic + (150-len(str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S"))) - len(
                    notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S")))
        self.sortFromNewToOld = not self.sortFromNewToOld

    def refreshTable(self):
        self.noteTray.clear()
        # global notelst
        notelst = nota.getNoteAll()
        Sort.sortNote(notelst, 1)  # new =1 ใหม่ขึ้นก่อน new =0  เก่ามาก่อน
        for i in range(len(notelst)):
            self.noteTray.addItem(notelst[i].topic + (150-len(str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S"))) - len(
                notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S")))

    def showPopUp(self):
        pop = Popup(self)
        pop.show()

    def goToAddNote(self):
        addNoteWindow = AddNoteWindow()
        widget.addWidget(addNoteWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToHomeWeek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToTaskWindow(self):
        task_window = Task_window()
        widget.addWidget(task_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToTimeTableWindow(self):
        timeTable_window = TimeTable_window()
        widget.addWidget(timeTable_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


class AddNoteWindow(QDialog):
    def __init__(self):
        super(AddNoteWindow, self).__init__()
        loadUi("add_note.ui", self)
        self.warning.setVisible(False)
        self.unAddNote.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.addNoteWindowToHomeWeek)
        self.taskButton.clicked.connect(self.goToTaskWindow)
        self.saveNoteButton.disconnect()
        self.saveNoteButton.clicked.connect(self.addNote)
        self.cancelAdding.clicked.connect(self.cancelNote)

        self.noteName_textEdit.textChanged.connect(self.mytxtChanged)
        self.noteName_textEdit.setLineWrapMode(0)

        global userName
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

        if self.sender().objectName() == "edit":
            self.indexNote = fromWho.currentRow()
            self.noteName_textEdit.setPlainText(notelst[self.indexNote].topic)

            temptext = notelst[self.indexNote].description
            print(temptext)
            self.note_description.setPlainText(temptext.replace("\\n", '\n'))

            self.saveNoteButton.disconnect()
            self.saveNoteButton.clicked.connect(self.saveNote)
            self.saveNoteButton.setText("SAVE")

    def saveNote(self):
        # print("------>", self.indexNote)
        notelst[self.indexNote].topic = self.noteName_textEdit.toPlainText()

        # notelst[self.indexNote].description = self.note_description.toPlainText()
        temptext = self.note_description.toPlainText()
        notelst[self.indexNote].description = '\\n'.join(temptext.splitlines())

        time = datetime.datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        # print("TIME:", time)

        notelst[self.indexNote].dateCreate = time

        nota.editRecord(notelst[self.indexNote])
        self.note_description.clear()
        self.goToNoteWindow()

    def addNote(self):
        if self.noteName_textEdit.toPlainText() != "":
            temptext = self.note_description.toPlainText()
            temptext = '\\n'.join(temptext.splitlines())
            nota.addRecord(
                time, 2, self.noteName_textEdit.toPlainText(), temptext)
            self.noteName_textEdit.clear()
            self.note_description.clear()
            self.goToNoteWindow()
        else:
            self.warning.setVisible(True)

    def cancelNote(self):
        self.noteName_textEdit.clear()
        self.note_description.clear()
        print("UnSaved")
        self.goToNoteWindow()

    def mytxtChanged(self):
        maxlengthtext = 15
        if (len(self.noteName_textEdit.toPlainText())) > maxlengthtext:
            maxstringtext = self.noteName_textEdit.toPlainText()
            print(len(maxstringtext))
            self.noteName_textEdit.setPlainText(maxstringtext[:-1])

            cursor = self.noteName_textEdit.textCursor()
            cursor.setPosition(maxlengthtext)
            self.noteName_textEdit.setTextCursor(cursor)

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

    def goToTimeTableWindow(self):
        timeTable_window = TimeTable_window()
        widget.addWidget(timeTable_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Task_window(QDialog):
    def __init__(self):
        super(Task_window, self).__init__()
        loadUi("task_window.ui", self)
        self.sortFromNearToFar = True
        self.addTask.clicked.connect(self.goToAddTask)
        self.noteButton.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.taskWindowToHomeWeek)
        self.listWidget.itemDoubleClicked.connect(self.showPopUp)
        self.listWidget_incoming.itemDoubleClicked.connect(self.showPopUp)
        self.sortButton.clicked.connect(self.sortTaskList)
        self.timeTableButton.clicked.connect(self.goToTimeTableWindow)
        self.showButton.clicked.connect(self.show_hide_completed_tasks)
        global userName
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))
        self.hideCompletedTask = True
        self.listWidget.clear()
        global today_tasklst
        today_tasklst = nota.getTodayNotFinishTask()
        Sort.sortTaskDateTarget(today_tasklst)
        for i in range(len(today_tasklst)):

            self.listWidget.addItem(today_tasklst[i].topic+(35-len(today_tasklst[i].topic))*" "
                                    + str(today_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
        self.listWidget_incoming.clear()
        global incoming_tasklst
        incoming_tasklst = nota.getIncomingNotFinishTask()
        Sort.sortTaskDateTarget(incoming_tasklst)
        for i in range(len(incoming_tasklst)):
            self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(35-len(incoming_tasklst[i].topic))*" "
                                             + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))

    def showPopUp(self):
        pop = Popup(self)
        pop.show()

    def sortTaskList(self):
        global today_tasklst
        global incoming_tasklst
        self.listWidget.clear()
        self.listWidget_incoming.clear()
        if not self.sortFromNearToFar:
            x = 1
        else:
            x = 0
        if self.hideCompletedTask:
            today_tasklst = nota.getTodayNotFinishTask()
            incoming_tasklst = nota.getIncomingNotFinishTask()
        else:
            today_tasklst = nota.getTaskToday()
            incoming_tasklst = nota.getIncomingTask(7)

        Sort.sortTaskDateTarget(today_tasklst, x)
        for i in range(len(today_tasklst)):
            self.listWidget.addItem(today_tasklst[i].topic+(35-len(today_tasklst[i].topic))*" "
                                    + str(today_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
        Sort.sortTaskDateTarget(incoming_tasklst, x)
        for i in range(len(incoming_tasklst)):
            self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(35-len(incoming_tasklst[i].topic))*" "
                                             + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
        self.sortFromNearToFar = not self.sortFromNearToFar

    def show_hide_completed_tasks(self):
        if self.hideCompletedTask:
            self.listWidget.clear()
            global today_tasklst
            today_tasklst = nota.getTaskToday()
            Sort.sortTaskDateTarget(today_tasklst)
            for i in range(len(today_tasklst)):
                self.listWidget.addItem(today_tasklst[i].topic+(35-len(today_tasklst[i].topic))*" "
                                        + str(today_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
            self.listWidget_incoming.clear()
            global incoming_tasklst
            incoming_tasklst = nota.getIncomingTask(7)
            Sort.sortTaskDateTarget(incoming_tasklst)
            for i in range(len(incoming_tasklst)):
                self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(35-len(incoming_tasklst[i].topic))*" "
                                                 + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
            self.showButton.setText("HIDE COMPLETED TASKS")
        else:
            self.listWidget.clear()
            today_tasklst = nota.getTodayNotFinishTask()
            Sort.sortTaskDateTarget(today_tasklst)
            for i in range(len(today_tasklst)):
                self.listWidget.addItem(today_tasklst[i].topic+(35-len(today_tasklst[i].topic))*" "
                                        + str(today_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
            self.listWidget_incoming.clear()
            incoming_tasklst = nota.getIncomingNotFinishTask()
            Sort.sortTaskDateTarget(incoming_tasklst)
            for i in range(len(incoming_tasklst)):
                self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(35-len(incoming_tasklst[i].topic))*" "
                                                 + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
            self.showButton.setText("SHOW COMPLETED TASKS")
        self.hideCompletedTask = not self.hideCompletedTask

    def refreshTable(self):
        global today_tasklst
        global incoming_tasklst
        if self.hideCompletedTask:
            self.listWidget.clear()
            today_tasklst = nota.getTodayNotFinishTask()
            Sort.sortTaskDateTarget(today_tasklst)
            for i in range(len(today_tasklst)):
                self.listWidget.addItem(today_tasklst[i].topic+(35-len(today_tasklst[i].topic))*" " + str(
                    today_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
            self.listWidget_incoming.clear()

            incoming_tasklst = nota.getIncomingNotFinishTask()
            Sort.sortTaskDateTarget(incoming_tasklst)
            for i in range(len(incoming_tasklst)):
                self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(35-len(incoming_tasklst[i].topic))*" "
                                                 + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
        else:
            self.listWidget.clear()
            today_tasklst = nota.getTaskToday()
            Sort.sortTaskDateTarget(today_tasklst)
            for i in range(len(today_tasklst)):
                self.listWidget.addItem(today_tasklst[i].topic+(35-len(today_tasklst[i].topic))*" "
                                        + str(today_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
            self.listWidget_incoming.clear()
            incoming_tasklst = nota.getIncomingTask(7)
            Sort.sortTaskDateTarget(incoming_tasklst)
            for i in range(len(incoming_tasklst)):
                self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(35-len(incoming_tasklst[i].topic))*" "
                                                 + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))

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

    def goToTimeTableWindow(self):
        timeTable_window = TimeTable_window()
        widget.addWidget(timeTable_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


class AddTaskWindow(QDialog):
    def __init__(self):
        super(AddTaskWindow, self).__init__()
        loadUi("add_task_window.ui", self)
        self.warning.setVisible(False)
        self.unAddTask.clicked.connect(self.goToTaskWindow)
        self.noteButton.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.addTaskWindowToHomeWeek)
        self.saveNoteButton.disconnect()
        self.saveNoteButton.clicked.connect(self.addTask)
        self.cancelAdding.clicked.connect(self.cancelTask)
        self.taskName_textEdit.textChanged.connect(self.mytxtChanged)
        self.taskName_textEdit.setLineWrapMode(0)
        global userName
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

        temp = datetime.datetime.now()
        test = QtCore.QDateTime(int(temp.strftime("%Y")),
                                int(temp.strftime("%m")),
                                int(temp.strftime("%d")),
                                int(temp.strftime("%H")),
                                int(temp.strftime("%M")),
                                int(temp.strftime("%S")))
        self.dateTimeEdit.setDateTime(test)

        if self.sender().objectName() == "edit":
            global fromWho
            self.indextask = fromWho.currentRow()
            self.taskName_textEdit.setPlainText(
                incoming_tasklst[self.indextask].topic)

            # temptxt = incoming_tasklst[self.indextask].description
            # temptxt = temptxt.replace("\\n", '\n')
            # print(temptxt)

            self.task_description.setPlainText(
                incoming_tasklst[self.indextask].description.replace("\\n", '\n'))

            self.dateTimeEdit.setDateTime(
                incoming_tasklst[self.indextask].dateTarget)
            self.saveNoteButton.disconnect()
            self.saveNoteButton.clicked.connect(self.saveTask)
            self.saveNoteButton.setText("SAVE")

    def saveTask(self):
        print("------>", self.indextask)
        if self.sender().objectName() == "listWidget":
            today_tasklst[self.indextask].topic = self.taskName_textEdit.toPlainText()
            # today_tasklst[self.indextask].description = self.task_description.toPlainText(
            # )

            temptext = self.task_description.toPlainText()

            today_tasklst[self.indextask].description = '\\n'.join(
                temptext.splitlines())

            time = self.dateTimeEdit.dateTime()
            time = time.toPyDateTime()
            today_tasklst[self.indextask].dateTarget = time
            nota.editRecord(today_tasklst[self.indextask])

        else:
            incoming_tasklst[self.indextask].topic = self.taskName_textEdit.toPlainText(
            )
            # incoming_tasklst[self.indextask].description = self.task_description.toPlainText(
            # )
            temptext = self.task_description.toPlainText()
            incoming_tasklst[self.indextask].description = '\\n'.join(
                temptext.splitlines())

            time = self.dateTimeEdit.dateTime()
            time = time.toPyDateTime()
            incoming_tasklst[self.indextask].dateTarget = time
            nota.editRecord(incoming_tasklst[self.indextask])

        self.taskName_textEdit.clear()
        self.task_description.clear()
        self.goToTaskWindow()

    def addTask(self):

        if self.taskName_textEdit.toPlainText() != "":

            # M/d/yy h:mm AP
            # self.dateTimeEdit.setDateTime(incoming_tasklst[self.indextask].dateTarget)

            time = self.dateTimeEdit.dateTime()
            # yy/m/d h:mm:ss
            time = time.toPyDateTime()

            temptext = self.task_description.toPlainText()

            temptext = '\\n'.join(temptext.splitlines())
            nota.addRecord(
                time, 0, self.taskName_textEdit.toPlainText(), temptext)

            self.taskName_textEdit.clear()
            self.task_description.clear()

            self.goToTaskWindow()
        else:
            self.warning.setVisible(True)

    def cancelTask(self):
        self.taskName_textEdit.clear()
        self.task_description.clear()
        # print("------C", self.sender().objectName())
        # print("------C", self.taskName_textEdit.toPlainText())
        # print("------C", self.task_description.toPlainText())
        print("UnSaved")
        self.goToTaskWindow()

    def mytxtChanged(self):
        # dont use max 30      textlistwidget will bug cant see anything in list
        if self.sender().objectName() == "taskName_textEdit":
            maxlengthtext = 15
            if (len(self.taskName_textEdit.toPlainText())) > maxlengthtext:
                maxstringtext = self.taskName_textEdit.toPlainText()

                self.taskName_textEdit.setPlainText(maxstringtext[:-1])

                cursor = self.taskName_textEdit.textCursor()
                cursor.setPosition(maxlengthtext)
                self.taskName_textEdit.setTextCursor(cursor)
        # elif self.sender().objectName() == "task_description":
            # maxRow = 12
            # maxCharPerRow = 80
            # maxdescripText = self.task_description.toPlainText()
            # countn = 0
            # for i in range(len(maxdescripText)):
            #     if maxdescripText[i] == '\n':
            #         countn += 1
            # print(countn)
            # print("LENS:", len(maxdescripText))
            # if (len(maxdescripText)-(2*countn)) > maxCharPerRow-1 or countn > maxRow-1:
            #     maxdescripText = self.task_description.toPlainText()
            #     self.task_description.setPlainText(maxdescripText[:-1])

            #     cursor = self.task_description.textCursor()
            #     cursor.setPosition(len(maxdescripText))
            #     self.task_description.setTextCursor(cursor)

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

    def goToTimeTableWindow(self):
        timeTable_window = TimeTable_window()
        widget.addWidget(timeTable_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


class TimeTable_window(QDialog):
    def __init__(self):
        global checkbox
        checkbox = [True, True, True, True, True, True, True]
        super(TimeTable_window, self).__init__()
        loadUi("timetable.ui", self)
        self.addTimeTableButton.clicked.connect(self.goToAddTimeTable)
        self.noteButton.clicked.connect(self.goToNoteWindow)
        self.taskButton.clicked.connect(self.goToTaskWindow)
        self.homeButton.clicked.connect(self.taskWindowToHomeWeek)
        self.today_TimetableTray.itemDoubleClicked.connect(self.showPopUp)
        self.completed_TimetableTray.itemDoubleClicked.connect(self.showPopUp)
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))
        self.listDayButton = list()
        self.listDayButton.append(self.monday_button_2)
        self.listDayButton.append(self.tuesday_button_2)
        self.listDayButton.append(self.wednesday_button_2)
        self.listDayButton.append(self.thursday_button_2)
        self.listDayButton.append(self.friday_button_2)
        self.listDayButton.append(self.saturday_button_2)
        self.listDayButton.append(self.sunday_button_2)

        self.dayBarButtonList = ["monday_button_2", "tuesday_button_2", "wednesday_button_2",
                                 "thursday_button_2", "friday_button_2", "saturday_button_2", "sunday_button_2"]

        for i in range(len(self.listDayButton)):
            # SET clicked connect
            self.listDayButton[i].clicked.connect(self.setCurrent)
        self.currentDay = -1  # ยังไม่เลือกวัน = Today, Monday =0 .... Sunday = 6

        if self.currentDay == -1:
            dayhw = datetime.datetime.now()
            dayhw = str(dayhw.strftime("%a"))
            if dayhw == "Mon":
                self.currentDay = 0
            elif dayhw == "Tue":
                self.currentDay = 1
            elif dayhw == "Wed":
                self.currentDay = 2
            elif dayhw == "Thu":
                print("Check")
                self.currentDay = 3
            elif dayhw == "Fri":
                self.currentDay = 4
            elif dayhw == "Sat":
                self.currentDay = 5
            elif dayhw == "Sun":
                self.currentDay = 6
        print(self.currentDay)
        self.currentDay_objectName = self.dayBarButtonList[self.currentDay]
        timetablelst = nota.getTimetableAll(self.currentDay)

        self.today_TimetableTray.clear()
        for i in range(len(timetablelst)):
            self.today_TimetableTray.addItem(timetablelst[i].topic)
        # self.today_TimetableTray.setSpacing(15)

        for i in range(len(self.listDayButton)):

            self.listDayButton[i].clicked.connect(self.setCurrent)
        self.setColorAtStart()

    def showPopUp(self):
        pop = Popup(self)
        pop.show()

    def goToAddTimeTable(self):
        addTimeTableWindow = AddTimeTableWindow()
        widget.addWidget(addTimeTableWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToTaskWindow(self):
        task_window = Task_window()
        widget.addWidget(task_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToNoteWindow(self):
        note_window = Note_window()
        widget.addWidget(note_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def taskWindowToHomeWeek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def refreshTable(self):
        for i in range(len(self.listDayButton)):
            if self.listDayButton[i].objectName() == self.currentEditingDay:
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')

                global timetablelst
                timetablelst = list()
                timetablelst = nota.getTimetableAll(i)
                self.today_TimetableTray.clear()
                for i in range(len(timetablelst)):
                    self.today_TimetableTray.addItem(timetablelst[i].topic)
                # self.today_TimetableTray.setSpacing(15)

            else:
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')

    def setColorAtStart(self):
        for i in range(len(self.listDayButton)):
            if self.listDayButton[i].objectName() == self.currentDay_objectName:
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')
                timetablelst = nota.getTimetableAll(i)
                self.today_TimetableTray.clear()
                for i in range(len(timetablelst)):
                    self.today_TimetableTray.addItem(timetablelst[i].topic)

            else:
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')
        self.currentEditingDay = self.currentDay_objectName

    def setCurrent(self):
        self.currentEditingDay = self.sender().objectName()
        if self.sender().objectName() == self.currentDay_objectName:
            self.currentEditingDay_int = int(self.currentDay)
            self.label.setText("TODAY")
        elif self.sender().objectName() == self.dayBarButtonList[0]:
            self.currentEditingDay_int = 0
            self.label.setText("MONDAY")
        elif self.sender().objectName() == self.dayBarButtonList[1]:
            self.currentEditingDay_int = 1
            self.label.setText("TUESDAY")
        elif self.sender().objectName() == self.dayBarButtonList[2]:
            self.currentEditingDay_int = 2
            self.label.setText("WEDNESDAY")
        elif self.sender().objectName() == self.dayBarButtonList[3]:
            self.currentEditingDay_int = 3
            self.label.setText("THURSDAY")
        elif self.sender().objectName() == self.dayBarButtonList[4]:
            self.currentEditingDay_int = 4
            self.label.setText("FRIDAY")
        elif self.sender().objectName() == self.dayBarButtonList[5]:
            self.label.setText("SATURDAY")
            self.currentEditingDay_int = 5
        elif self.sender().objectName() == self.dayBarButtonList[6]:
            self.currentEditingDay_int = 6
            self.label.setText("SUNDAY")

        for i in range(len(self.listDayButton)):
            if self.listDayButton[i].objectName() == self.sender().objectName():
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')
                global timetablelst
                timetablelst = list()
                timetablelst = nota.getTimetableAll(i)
                self.today_TimetableTray.clear()
                for i in range(len(timetablelst)):
                    self.today_TimetableTray.addItem(timetablelst[i].topic)
                # self.today_TimetableTray.setSpacing(15)

            else:
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')


class AddTimeTableWindow(QDialog):
    def __init__(self):
        super(AddTimeTableWindow, self).__init__()
        loadUi("Timetableadd.ui", self)
        self.unAddButton.clicked.connect(self.goToTimeTableWindow)
        self.noteButton.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.goToHomeWeek)
        self.taskButton.clicked.connect(self.goToTaskWindow)
        self.saveTimetableButton.disconnect()
        self.saveTimetableButton.clicked.connect(self.addTimetable)
        self.cancelTimetableButton.clicked.connect(self.cancelTimetable)
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

        self.timetabletitleName_textEdit.textChanged.connect(self.mytxtChanged)
        self.timetabletitleName_textEdit.setLineWrapMode(0)

        self.listDayButton = list()
        self.listDayButton.append(self.monday_button_Repeat)
        self.listDayButton.append(self.tuesday_button_Repeat)
        self.listDayButton.append(self.wednesday_Repeat)
        self.listDayButton.append(self.thursday_Repeat)
        self.listDayButton.append(self.friday_button_Repeat)
        self.listDayButton.append(self.saturday_button_Repeat)
        self.listDayButton.append(self.sunday_button_Repeat)

        if self.sender().objectName() == "edit":
            self.indexTimetable = fromWho.currentRow()

            a = str(timetablelst[self.indexTimetable].dateTarget)
            a = a[11:13]
            a = int(a)
            b = str(timetablelst[self.indexTimetable].dateTarget)
            b = b[14:16]
            b = int(b)
            self.timetable_Edittime.setTime(time(a, b))
            self.timetabletitleName_textEdit.setPlainText(
                timetablelst[self.indexTimetable].topic)

            self.timetable_description.setPlainText(
                timetablelst[self.indexTimetable].description)

            self.saveTimetableButton.disconnect()
            self.saveTimetableButton.clicked.connect(self.saveTimetable)
            self.saveTimetableButton.setText("SAVE")

        for i in range(len(self.listDayButton)):
            # SET clicked connect
            self.listDayButton[i].clicked.connect(self.setCurrent)

    def setCurrent(self):
        for i in range(len(self.listDayButton)):
            if self.listDayButton[i].objectName() == self.sender().objectName() and checkbox[i] == True:
                # print(self.sender().objectName())
                checkbox[i] = False
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')

            elif self.listDayButton[i].objectName() == self.sender().objectName() and checkbox[i] == False:
                checkbox[i] = True
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')

    def saveTimetable(self):  # ได้แค่ของ Today
        timetablelst[self.indexTimetable].topic = self.timetabletitleName_textEdit.toPlainText()
        timetablelst[self.indexTimetable].description = self.timetable_description.toPlainText()
        a = str(self.timetable_Edittime.dateTime().toPyDateTime())
        a = a[11:]
        timetablelst[self.indexTimetable].dateTarget = a
        nota.editRecord(timetablelst[self.indexTimetable])
        self.timetabletitleName_textEdit.clear()
        self.timetable_description.clear()
        self.goToTimeTableWindow()

    def addTimetable(self):
        # M/d/yy h:mm AP
        time = self.timetable_Edittime.dateTime()
        # yy/m/d h:mm:ss
        time = time.toPyDateTime()
        for i in range(len(checkbox)):
            if checkbox[i] == False:
                nota.addRecord(time.strftime("%H:%M:%S"), 1, self.timetabletitleName_textEdit.toPlainText(
                ), self.timetable_description.toPlainText(), i)

        self.timetabletitleName_textEdit.clear()
        self.timetable_description.clear()
        self.goToTimeTableWindow()

    def cancelTimetable(self):
        self.timetabletitleName_textEdit.clear()
        self.timetable_description.clear()
        print("UNSAVE TIME TABLE")
        self.goToTimeTableWindow()

    def mytxtChanged(self):
        maxlengthtext = 15
        if (len(self.timetabletitleName_textEdit.toPlainText())) > maxlengthtext:
            maxstringtext = self.timetabletitleName_textEdit.toPlainText()
            print(len(maxstringtext))
            self.timetabletitleName_textEdit.setPlainText(maxstringtext[:-1])

            cursor = self.timetabletitleName_textEdit.textCursor()
            cursor.setPosition(maxlengthtext)
            self.timetabletitleName_textEdit.setTextCursor(cursor)

    def goToTimeTableWindow(self):
        timeTable_window = TimeTable_window()
        widget.addWidget(timeTable_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToTaskWindow(self):
        task_window = Task_window()
        widget.addWidget(task_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToNoteWindow(self):
        note_window = Note_window()
        widget.addWidget(note_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToHomeWeek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Popup(QDialog):
    def __init__(self, parent):
        super(Popup, self).__init__(parent)
        loadUi("popUp.ui", self)
        self.confirm.setVisible(False)
        self.cancel.setVisible(False)
        self.confirmation.setVisible(False)
        self.delete_2.clicked.connect(self.showConfirmationBox)
        self.mark.clicked.connect(self.markAsCompleted)
        global fromWho
        fromWho = self.sender()
        self.indextask = self.sender().currentRow()

        if fromWho.objectName() == 'noteTray':
            self.mark.setVisible(False)
            self.direction.setText(
                "Please choose action you want to do with this note")
            self.edit.clicked.connect(self.goToAddNote)

        elif fromWho.objectName() == 'today_TimetableTray':

            self.edit.clicked.connect(self.goToAddTimeTable)
        else:

            self.edit.clicked.connect(self.goToAddTask)

    def markAsCompleted(self):

        if fromWho.objectName() == "listWidget":
            today_tasklst[self.indextask].finish = 1
            nota.editRecord(today_tasklst[self.indextask])
        else:
            incoming_tasklst[self.indextask].finish = 1
            nota.editRecord(incoming_tasklst[self.indextask])
        self.parent().refreshTable()
        self.close()

    def goToAddNote(self):
        addNoteWindow = AddNoteWindow()
        widget.addWidget(addNoteWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.close()

    def goToAddTask(self):
        addTaskWindow = AddTaskWindow()
        widget.addWidget(addTaskWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.close()

    def goToAddTimeTable(self):
        addTimeTableWindow = AddTimeTableWindow()
        widget.addWidget(addTimeTableWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.close()

    def showConfirmationBox(self):
        self.confirm.setVisible(True)
        self.cancel.setVisible(True)
        self.confirmation.setVisible(True)
        self.delete_2.setGeometry(279, 21, 65, 32)
        self.delete_2.setStyleSheet(
            'QPushButton{background-color:rgb(212, 0, 0);border-radius: 10px;color: rgb(255, 255, 255);}')
        self.confirm.clicked.connect(self.deleteTask)
        self.cancel.clicked.connect(self.close)

    def deleteTask(self):

        if fromWho.objectName() in ["listWidget", "listWidget_incoming"]:

            nota.deletRow(incoming_tasklst[self.indextask])
            self.parent().refreshTable()
            self.close()
        elif fromWho.objectName() == "noteTray":
            nota.deletRow(notelst[self.indextask])
            self.parent().refreshTable()
            self.close()
        elif fromWho.objectName() == "today_TimetableTray":
            nota.deletRow(timetablelst[self.indextask])
            self.parent().refreshTable()
            self.close()


# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginWindow = LoginWindow()
nota = Nota()
widget.addWidget(loginWindow)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("No im not out!")
