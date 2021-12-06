from datetime import time
import sys
from PyQt5.QtCore import center
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from notaBack import *
from note import Note

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
        global userName
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
        global userName
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
            elif dayhw == "Thur":
                self.currentDay = 3
            elif dayhw == "Fri":
                self.currentDay = 4
            elif dayhw == "Sat":
                self.currentDay = 5
            elif dayhw == "Sun":
                self.currentDay = 6
            print(self.currentDay)
            global timetablelst
            timetablelst = nota.getTimetableAll(self.currentDay)
            self.timeTableTray.clear()
            for i in range(len(timetablelst)):
                self.timeTableTray.addItem(timetablelst[i].topic)
            self.timeTableTray.itemDoubleClicked.connect(self.goToAddTimetable)
            # self.timeTableTray.setSpacing(15)

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

                # Update listwidget timeTableTray
                global timetablelst
                timetablelst = nota.getTimetableAll(i)
                self.timeTableTray.clear()
                for i in range(len(timetablelst)):
                    self.timeTableTray.addItem(timetablelst[i].topic)
                self.timeTableTray.itemDoubleClicked.connect(
                    self.goToAddTimetable)
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
        self.homeButton.clicked.connect(self.noteWindowToHomeWeek)
        self.taskButton.clicked.connect(self.goToTaskWindow)
        self.timeTableButton.clicked.connect(self.goToTimeTableWindow)
        self.sortFromNewToOld = True
        self.sortButton.clicked.connect(self.sortNoteList)
        global userName
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

        self.noteTray.itemDoubleClicked.connect(self.goToAddNote)
        self.noteTray.clear()
        global notelst

        notelst = nota.getNoteAll()
        Sort.sortNote(notelst, 1)  # new =1 ใหม่ขึ้นก่อน new =0  เก่ามาก่อน

        for i in range(len(notelst)):
            self.noteTray.addItem(notelst[i].topic + (165-len(str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S"))) - len(
                notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S")))

    def sortNoteList(self):
        self.noteTray.clear()
        global notelst
        notelst = nota.getNoteAll()
        if self.sortFromNewToOld:
            Sort.sortNote(notelst, 0)
            for i in range(len(notelst)):
                self.noteTray.addItem(notelst[i].topic + (165-len(str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S"))) - len(
                    notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S")))

        else:
            Sort.sortNote(notelst, 1)
            for i in range(len(notelst)):
                self.noteTray.addItem(notelst[i].topic + (165-len(str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S"))) - len(
                    notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S")))
        self.sortFromNewToOld = not self.sortFromNewToOld

    def goToAddNote(self):
        addNoteWindow = AddNoteWindow()
        widget.addWidget(addNoteWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToHomeWeek(self):
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
        global userName
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

        if self.sender().objectName() == "noteTray":
            self.indexNote = self.sender().currentRow()
            self.noteName_textEdit.setPlainText(notelst[self.indexNote].topic)
            self.note_description.setPlainText(
                notelst[self.indexNote].description)
            self.saveNoteButton.disconnect()
            self.saveNoteButton.clicked.connect(self.saveNote)
            self.saveNoteButton.setText("SAVE")

            print(notelst[self.indexNote].taskID)

    def saveNote(self):
        # print("------>", self.indexNote)
        notelst[self.indexNote].topic = self.noteName_textEdit.toPlainText()
        notelst[self.indexNote].description = self.note_description.toPlainText()

        time = datetime.datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        # print("TIME:", time)

        notelst[self.indexNote].dateCreate = time

        nota.editRecord(notelst[self.indexNote])
        self.note_description.clear()
        self.goToNoteWindow()

    def addNote(self):
        if self.noteName_textEdit.toPlainText() != "":

            nota.addRecord(time, 2, self.noteName_textEdit.toPlainText(),
                           self.note_description.toPlainText())
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
        global userName
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

        self.listWidget.clear()
        global today_tasklst
        today_tasklst = nota.getTaskToday()
        Sort.sortTaskDateTarget(today_tasklst)
        for i in range(len(today_tasklst)):
            self.listWidget.addItem(today_tasklst[i].topic+(60-len(today_tasklst[i].topic))*" "
                                    + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))
        self.listWidget_incoming.clear()
        global incoming_tasklst
        incoming_tasklst = nota.getIncomingTask(7)
        Sort.sortTaskDateTarget(incoming_tasklst)

        for i in range(len(incoming_tasklst)):
            self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(35-len(incoming_tasklst[i].topic))*" "
                                             + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))

    def showPopUp(self):
        pop = Popup(self)
        pop.show()

    def sortTaskList(self):
        self.listWidget.clear()
        self.listWidget_incoming.clear()
        global today_tasklst
        today_tasklst = nota.getTaskToday()
        global incoming_tasklst
        incoming_tasklst = nota.getIncomingTask(7)

        if not self.sortFromNearToFar:
            x = 1
        else:
            x = 0
        Sort.sortTaskDateTarget(today_tasklst, x)
        for i in range(len(today_tasklst)):
            self.listWidget.addItem(today_tasklst[i].topic+(60-len(today_tasklst[i].topic))*" "
                                    + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))
        Sort.sortTaskDateTarget(incoming_tasklst, x)
        for i in range(len(incoming_tasklst)):
            self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(35-len(incoming_tasklst[i].topic))*" "
                                             + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
        self.sortFromNearToFar = not self.sortFromNearToFar

    def refreshTable(self):
        self.listWidget.clear()
        global today_tasklst
        today_tasklst = nota.getTaskToday()
        Sort.sortTaskDateTarget(today_tasklst)
        for i in range(len(today_tasklst)):
            self.listWidget.addItem(today_tasklst[i].topic+(60-len(today_tasklst[i].topic))*" "
                                    + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))
        self.listWidget_incoming.clear()
        global incoming_tasklst
        incoming_tasklst = nota.getIncomingTask(7)
        Sort.sortTaskDateTarget(incoming_tasklst)

        for i in range(len(incoming_tasklst)):
            self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(35-len(incoming_tasklst[i].topic))*" "
                                             + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))

    def getUpdate(self):
        pass
        # addTaskWindow = AddTaskWindow()
        # widget.addWidget(addTaskWindow)
        # widget.setCurrentIndex(widget.currentIndex()+1)

        # indextask = self.listWidget.currentRow()
        # print(today_tasklst[indextask].topic)

        # addTaskWindow.task_description.setPlainText(
        #     today_tasklst[indextask].description)
        # addTaskWindow.taskName_textEdit.setPlainText(today_tasklst[indextask].topic)
        # timetarget = today_tasklst[indextask].dateTarget
        # print(timetarget)
        # print(type(timetarget))
        # addTaskWindow.dateTimeEdit.setDateTime(timetarget)

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
        global userName
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

        if self.sender().objectName() == "edit":
            global fromWho
            self.indextask = fromWho.currentRow()
            self.taskName_textEdit.setPlainText(
                incoming_tasklst[self.indextask].topic)
            self.task_description.setPlainText(
                incoming_tasklst[self.indextask].description)
            self.dateTimeEdit.setDateTime(
                incoming_tasklst[self.indextask].dateTarget)
            self.saveNoteButton.disconnect()
            self.saveNoteButton.clicked.connect(self.saveTask)
            self.saveNoteButton.setText("SAVE")
        # elif self.sender().objectName() == "addTask":
        #     self.dateTimeEdit.setDateTime(datetime.datetime.today())
        print("------>", self.sender().parent())
        print("------>", self.taskName_textEdit.toPlainText())
        print("------>", self.task_description.toPlainText())

    def saveTask(self):
        print("------>", self.indextask)
        if self.sender().objectName() == "listWidget":
            today_tasklst[self.indextask].topic = self.taskName_textEdit.toPlainText()
            today_tasklst[self.indextask].description = self.task_description.toPlainText(
            )
            time = self.dateTimeEdit.dateTime()
            time = time.toPyDateTime()
            today_tasklst[self.indextask].dateTarget = time
            nota.editRecord(today_tasklst[self.indextask])

        else:
            incoming_tasklst[self.indextask].topic = self.taskName_textEdit.toPlainText(
            )
            incoming_tasklst[self.indextask].description = self.task_description.toPlainText(
            )
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
        super(TimeTable_window, self).__init__()
        loadUi("timetable.ui", self)
        self.addTimeTableButton.clicked.connect(self.goToAddTimeTable)
        self.noteButton.clicked.connect(self.goToNoteWindow)
        self.taskButton.clicked.connect(self.goToTaskWindow)
        self.homeButton.clicked.connect(self.taskWindowToHomeWeek)
        global userName
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

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


class AddTimeTableWindow(QDialog):
    def __init__(self):
        super(AddTimeTableWindow, self).__init__()
        loadUi("Timetableadd.ui", self)

        self.unAddButton.clicked.connect(self.goToTimeTableWindow)
        self.noteButton.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.goToHomeWeek)
        self.taskButton.clicked.connect(self.goToTaskWindow)
        self.saveTimetableButton.disconnect()
        # FAILED SAT NOV 27 2:04:44 AM
        self.saveTimetableButton.clicked.connect(self.addTimetable)

        self.cancelTimetableButton.clicked.connect(self.cancelTimetable)
        global userName
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

        if self.sender().objectName() == "timeTableTray":
            print("HIIII")
            self.indexTimetable = self.sender().currentRow()
            print("---<><><>", self.indexTimetable)
            self.timetabletitleName_textEdit.setPlainText(
                timetablelst[self.indexTimetable].topic)
            self.timetable_description.setPlainText(
                timetablelst[self.indexTimetable].description)

            # self.timetable_Edittime.setHour(9)

            self.saveTimetableButton.disconnect()
            self.saveTimetableButton.clicked.connect(self.saveTimetable)
            self.saveTimetableButton.setText("SAVE")

    def saveTimetable(self):
        timetablelst[self.indexTimetable].topic = self.timetabletitleName_textEdit.toPlainText()
        timetablelst[self.indexTimetable].description = self.timetable_description.toPlainText()

    def addTimetable(self):
        # M/d/yy h:mm AP
        time = self.timetable_Edittime.dateTime()
        print("->timeedit:", time)
        # yy/m/d h:mm:ss
        time = time.toPyDateTime()
        print("->timePy:", time)

        nota.addRecord(6, 1, self.timetabletitleName_textEdit.toPlainText(
        ), self.timetable_description.toPlainText())

        self.timetabletitleName_textEdit.clear()
        self.timetable_description.clear()
        self.goToTimeTableWindow()

    def cancelTimetable(self):
        self.timetabletitleName_textEdit.clear()
        self.timetable_description.clear()
        print("UNSAVE TIME TABLE")
        self.goToTimeTableWindow()

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
        self.edit.clicked.connect(self.goToAddTask)
        self.mark.clicked.connect(self.markAsCompleted)

        if self.sender().objectName() in ["listWidget", "listWidget_incoming"]:
            global fromWho
            fromWho = self.sender()
            self.indextask = self.sender().currentRow()

    def markAsCompleted(self):
        pass

    def goToAddTask(self):
        addTaskWindow = AddTaskWindow()
        widget.addWidget(addTaskWindow)
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
        nota.deletRow(incoming_tasklst[self.indextask])
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
