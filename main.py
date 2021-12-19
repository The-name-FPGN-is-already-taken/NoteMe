from datetime import time
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import center
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from notaBack import *
from PyQt5 import QtGui
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
        # this mf should not be here but, whatever
        global currentClickingDay, currentClickingDay_week, currentClickingDay_int_ttb,currentClickingDay_int_hw
        global fromWho
        # เก็บวันที่ของวันปัจจุบันที่เรากดอยู่
        currentClickingDay = datetime.datetime.today().date()
        # เก็บaddressของปุ่มวันที่กดในหน้าHome
        currentClickingDay_week = self.loginButton
        currentClickingDay_int_ttb = 0  # เก็บเลขวันที่กำลังกดอยู่ ณ ปัจจุบัน ใช้กับหน้าTTB
        currentClickingDay_int_hw = 0  # เก็บเลขวันที่กำลังกดอยู่ ณ ปัจจุบัน ใช้กับหน้าHome
        fromWho = self.loginButton

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
        global currentClickingDay_week,fromWho  # this mf should not be here but, whatever
        currentClickingDay_week = self.signUpButton
        fromWho = self.signUpButton

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
        self.timeTableTray.itemDoubleClicked.connect(self.showPopUp)
        self.taskTray.itemDoubleClicked.connect(self.showPopUp)
        self.showButton.clicked.connect(self.show_hide_completed_tasks)
        self.sortButton.clicked.connect(self.sortTaskList)
        self.sortFromNearToFar = True

        self.hideCompletedTask = True

        self.listDayButton = list()
        self.listDayButton.append(self.monday_button)
        self.listDayButton.append(self.tuesday_button)
        self.listDayButton.append(self.wednesday_button)
        self.listDayButton.append(self.thursday_button)
        self.listDayButton.append(self.friday_button)
        self.listDayButton.append(self.saturday_button)
        self.listDayButton.append(self.sunday_button)

        # ยังไม่เลือกวัน = Today, Monday =0 .... Sunday = 6, currentDayเก็บวัน(สัปดาห์)ของวันปัจจุบัน
        self.currentDay = -1
        if self.currentDay == -1:
            dayhw = datetime.datetime.now()
            dayhw = str(dayhw.strftime("%a"))
            # print(dayhw)
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
        global currentClickingDay_int_ttb
        currentClickingDay_int_ttb = self.currentDay
        self.timeTableTray.clear()
        self.taskTray.clear()
        global timetablelst,today_tasklst, currentClickingDay
        timetablelst = nota.getTimetableByday(currentClickingDay_int_hw, 0)
        today_tasklst = nota.getTaskByDateNotFinish(currentClickingDay)
        Sort.sortTaskDateTarget(today_tasklst)
        self.updateItemInListWidgets()
        self.timeTableTray.setSpacing(15)
        self.taskTray.setSpacing(15)
        if self.sender().objectName() not in ["signUpButton", "loginButton"]:
            global currentClickingDay_week
            if currentClickingDay_week.objectName() in ["signUpButton", "loginButton"]:
                currentClickingDay_week = self.monday_button
            self.setColorAtStart()

        for i in range(len(self.listDayButton)):
            # SET TEXT
            self.listDayButton[i].setText((nota.showDateOfToday()+datetime.timedelta(days=i)).strftime(
                "%A")+"\n"+str((nota.showDateOfToday()+datetime.timedelta(days=i)).day))
            # SET clicked connect
            self.listDayButton[i].clicked.connect(self.setCurrent)

    def updateItemInListWidgets(self):
        for i in range(len(today_tasklst)):
            self.taskTray.addItem(today_tasklst[i].topic+(17-len(today_tasklst[i].topic))*" "
                                    + str(today_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
            self.taskTray.item(i).setFont(
                QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))
        for i in range(len(timetablelst)):
            self.timeTableTray.addItem(timetablelst[i].topic+(28-len(timetablelst[i].topic))*" "
                                             + str(timetablelst[i].dateTarget.strftime("%H:%M:%S")))
            self.timeTableTray.item(i).setFont(
                QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))
    
    def goToAddTimetable(self):

        addTimeTableWindow = AddTimeTableWindow()
        widget.addWidget(addTimeTableWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signOut(self):
        nota.logout()
        self.homeWeekToLogin()

    def showPopUp(self):
        pop = Popup(self)
        pop.show()

    def sortTaskList(self):
        global today_tasklst
        global timetablelst
        self.taskTray.clear()
        self.timeTableTray.clear()
        if not self.sortFromNearToFar:
            x = 1
        else:
            x = 0
        if self.hideCompletedTask:
            today_tasklst = nota.getTaskByDateNotFinish(currentClickingDay)
            timetablelst = nota.getTimetableByday(currentClickingDay_int_hw, 0)
        else:
            today_tasklst = nota.getTaskByDate(currentClickingDay)
            timetablelst = nota.getTimetableAll(currentClickingDay_int_hw)

        Sort.sortTaskDateTarget(today_tasklst, x)
        Sort.sortTimetableNew(timetablelst, x)
        self.updateItemInListWidgets()
        self.sortFromNearToFar = not self.sortFromNearToFar
    
    def setCurrent(self):  # edit here 4:22 PM. 12/16/2021
        # print(self.sender().objectName)
        if self.sender().objectName() == "monday_button":
            self.label.setText("Today")
        elif self.sender().objectName() == "tuesday_button":
            self.label.setText("Tomorrow")
        else:
            self.label.setText(self.sender().text())
        for i in range(len(self.listDayButton)):
            if self.listDayButton[i].objectName() == self.sender().objectName():
                # print(self.sender().objectName())
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')

                # Update listwidget taskTray
                nextday = (self.currentDay+i) % 7
                global timetablelst, currentClickingDay_week,currentClickingDay_int_hw
                currentClickingDay_week = self.sender()
                currentClickingDay_int_hw = i
                timetablelst = nota.getTimetableByday(nextday, 0)
                self.timeTableTray.clear()
                global today_tasklst, currentClickingDay
                today = datetime.datetime.now()
                x = today+datetime.timedelta(i)
                y = x.date()
                currentClickingDay = y
                if self.hideCompletedTask == True:
                    today_tasklst = nota.getTaskByDateNotFinish(currentClickingDay)
                else:
                    today_tasklst = nota.getTaskByDate(currentClickingDay)
                Sort.sortTaskDateTarget(today_tasklst)
                self.taskTray.clear()
                self.updateItemInListWidgets()
                self.taskTray.setSpacing(15)

            else:
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')

    def setColorAtStart(self):
        global currentClickingDay, fromWho,currentClickingDay_week
        if currentClickingDay == datetime.datetime.today().date():
            self.label.setText("Today")
        elif currentClickingDay_week.objectName() == "tuesday_button":
            self.label.setText("Tomorrow")
        else:
            self.label.setText(currentClickingDay_week.text())
        for i in range(len(self.listDayButton)):
            if self.listDayButton[i].objectName() == currentClickingDay_week.objectName():
                # print(self.sender().objectName())
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')
                # Update listwidget taskTray
                nextday = (self.currentDay+i) % 7
                global timetablelst,today_tasklst
                timetablelst = nota.getTimetableByday(nextday, 0)
                self.timeTableTray.clear()
                today = datetime.datetime.now()
                x = today+datetime.timedelta(i)
                y = x.date()
                currentClickingDay = y
                if self.hideCompletedTask == True:
                    today_tasklst = nota.getTaskByDateNotFinish(
                        currentClickingDay)
                else:
                    today_tasklst = nota.getTaskByDate(currentClickingDay)
                Sort.sortTaskDateTarget(today_tasklst)
                self.taskTray.clear()
                self.updateItemInListWidgets()
                # self.timeTableTray.setSpacing(15)

            else:
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')

    def show_hide_completed_tasks(self):  # ได้แค่ของTask
        if self.hideCompletedTask:
            global today_tasklst
            self.taskTray.clear()
            today_tasklst = nota.getTaskByDate(currentClickingDay)
            Sort.sortTaskDateTarget(today_tasklst)
            for i in range(len(today_tasklst)):
                self.taskTray.addItem(today_tasklst[i].topic+(35-len(today_tasklst[i].topic))*" "
                                      + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))
            self.showButton.setText("HIDE COMPLETED TASKS")
        else:
            today_tasklst = nota.getTaskByDateNotFinish(currentClickingDay)
            Sort.sortTaskDateTarget(today_tasklst)
            self.taskTray.clear()
            for k in range(len(today_tasklst)):
                self.taskTray.addItem(today_tasklst[k].topic+(35-len(today_tasklst[k].topic))*" " + str(
                    today_tasklst[k].dateTarget.strftime("%H:%M:%S")))
            self.showButton.setText("SHOW COMPLETED TASKS")
        self.hideCompletedTask = not self.hideCompletedTask

    def refreshTable(self):  # ได้แค่ของTask
        if self.hideCompletedTask:
            self.taskTray.clear()
            today_tasklst = nota.getTaskByDateNotFinish(currentClickingDay)
            Sort.sortTaskDateTarget(today_tasklst)
            for i in range(len(today_tasklst)):
                self.taskTray.addItem(today_tasklst[i].topic+(35-len(today_tasklst[i].topic))*" " + str(
                    today_tasklst[i].dateTarget.strftime("%H:%M:%S")))

        else:
            self.taskTray.clear()
            today_tasklst = nota.getTaskByDate(currentClickingDay)
            Sort.sortTaskDateTarget(today_tasklst)
            for i in range(len(today_tasklst)):
                self.taskTray.addItem(today_tasklst[i].topic+(35-len(today_tasklst[i].topic))*" "
                                      + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))

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

        self.noteTray.setGeometry(60, 110, 761, 331)

        self.noteTray.clear()
        global notelst
        notelst = nota.getNoteAll()

        Sort.sortNote(notelst, 1)  # new =1 ใหม่ขึ้นก่อน new =0  เก่ามาก่อน

        # self.noteTray.addItem(topictext.topic)
        for i in range(len(notelst)):
            # self.noteTray.addItem(notelst[i].topic + (165-len(str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S"))) - len(
            #    notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S")))
          #  tehehe= str(notelst[i].dateCreate.strftime("%Y-%m-%d %H:%M:%S"))
            # self.noteTray.addItem(f"{notelst[i].topic : <1}{tehehe : >50}")
            self.noteTray.addItem(notelst[i].topic + (52 - len(str(
                notelst[i].topic))) * " "+str(notelst[i].dateCreate.strftime("%Y-%m-%d"+8*" "+"%H:%M:%S")))
            self.noteTray.item(i).setFont(
                QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))

          #  self.noteTray.item(i).setTextAlignment(QtCore.Qt.AlignCenter)


    def sortNoteList(self):
        self.noteTray.clear()
        global notelst
        notelst = nota.getNoteAll()
        if self.sortFromNewToOld:
            Sort.sortNote(notelst, 0)
            for i in range(len(notelst)):
    
                self.noteTray.addItem(notelst[i].topic + (52 - len(
                    notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d"+8*" "+"%H:%M:%S")))
                self.noteTray.item(i).setFont(
                    QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))


        else:
            Sort.sortNote(notelst, 1)
            for i in range(len(notelst)):

                self.noteTray.addItem(notelst[i].topic + (52 - len(
                    notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d"+8*" "+"%H:%M:%S")))
                self.noteTray.item(i).setFont(
                    QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))

        self.sortFromNewToOld = not self.sortFromNewToOld

    def refreshTable(self):
        self.noteTray.clear()
        global notelst
        notelst = nota.getNoteAll()
        Sort.sortNote(notelst, 1)  # new =1 ใหม่ขึ้นก่อน new =0  เก่ามาก่อน
        for i in range(len(notelst)):
            self.noteTray.addItem(notelst[i].topic + (52 - len(notelst[i].topic))*" "+str(notelst[i].dateCreate.strftime("%Y-%m-%d"+8*" " + "%H:%M:%S")))
            self.noteTray.item(i).setFont(QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))


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

            # self.note_description.setPlainText(
            #     notelst[self.indexNote].description)
            temptext = notelst[self.indexNote].description
            print(temptext)
            self.note_description.setPlainText(temptext.replace("\\n", '\n'))

            self.saveNoteButton.disconnect()
            self.saveNoteButton.clicked.connect(self.saveNote)
            self.saveNoteButton.setText("SAVE")

    def saveNote(self):
        notelst[self.indexNote].topic = self.noteName_textEdit.toPlainText()

        # notelst[self.indexNote].description = self.note_description.toPlainText()
        temptext = self.note_description.toPlainText()
        notelst[self.indexNote].description = '\\n'.join(temptext.splitlines())

        time = datetime.datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S")
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

            self.listWidget.addItem(today_tasklst[i].topic+(20-len(today_tasklst[i].topic))*" "

                                    + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))

            self.listWidget.item(i).setFont(
                QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))


        self.listWidget_incoming.clear()
        global incoming_tasklst
        incoming_tasklst = nota.getIncomingNotFinishTask()
        Sort.sortTaskDateTarget(incoming_tasklst)
        for i in range(len(incoming_tasklst)):

            self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(17-len(incoming_tasklst[i].topic))*" "
                                             + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
            self.listWidget_incoming.item(i).setFont(
                QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))


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

            self.listWidget.addItem(today_tasklst[i].topic+(20-len(today_tasklst[i].topic))*" "
                                    + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))
            self.listWidget.item(i).setFont(
                QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))
        Sort.sortTaskDateTarget(incoming_tasklst, x)
        for i in range(len(incoming_tasklst)):
            self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(17-len(incoming_tasklst[i].topic))*" "
                                             + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
            self.listWidget_incoming.item(i).setFont(
                QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))

        self.sortFromNearToFar = not self.sortFromNearToFar

    def show_hide_completed_tasks(self):
        if self.hideCompletedTask:
            self.listWidget.clear()
            global today_tasklst
            today_tasklst = nota.getTaskToday()
            Sort.sortTaskDateTarget(today_tasklst)
            for i in range(len(today_tasklst)):

                self.listWidget.addItem(today_tasklst[i].topic+(20-len(today_tasklst[i].topic))*" "
                                        + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))
                self.listWidget.item(i).setFont(
                    QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))

            self.listWidget_incoming.clear()
            global incoming_tasklst
            incoming_tasklst = nota.getIncomingTask(7)
            Sort.sortTaskDateTarget(incoming_tasklst)
            for i in range(len(incoming_tasklst)):

                self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(17-len(incoming_tasklst[i].topic))*" "
                                                 + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
                self.listWidget_incoming.item(i).setFont(
                    QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))

            self.showButton.setText("HIDE COMPLETED TASKS")
        else:
            self.listWidget.clear()
            today_tasklst = nota.getTodayNotFinishTask()
            Sort.sortTaskDateTarget(today_tasklst)
            for i in range(len(today_tasklst)):

                self.listWidget.addItem(today_tasklst[i].topic+(20-len(today_tasklst[i].topic))*" "
                                        + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))
                self.listWidget.item(i).setFont(
                    QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))

            self.listWidget_incoming.clear()
            incoming_tasklst = nota.getIncomingNotFinishTask()
            Sort.sortTaskDateTarget(incoming_tasklst)
            for i in range(len(incoming_tasklst)):

                self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(17-len(incoming_tasklst[i].topic))*" "
                                                 + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
                self.listWidget_incoming.item(i).setFont(
                    QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))

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

                self.listWidget.addItem(today_tasklst[i].topic+(20-len(
                    today_tasklst[i].topic))*" " + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))
                self.listWidget.item(i).setFont(
                    QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))

            self.listWidget_incoming.clear()

            incoming_tasklst = nota.getIncomingNotFinishTask()
            Sort.sortTaskDateTarget(incoming_tasklst)
            for i in range(len(incoming_tasklst)):

                self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(17-len(incoming_tasklst[i].topic))*" "
                                                 + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
                self.listWidget_incoming.item(i).setFont(
                    QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))

        else:
            self.listWidget.clear()
            today_tasklst = nota.getTaskToday()
            Sort.sortTaskDateTarget(today_tasklst)
            for i in range(len(today_tasklst)):

                self.listWidget.addItem(today_tasklst[i].topic+(20-len(
                    today_tasklst[i].topic))*" " + str(today_tasklst[i].dateTarget.strftime("%H:%M:%S")))
                self.listWidget.item(i).setFont(
                    QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))

            self.listWidget_incoming.clear()
            incoming_tasklst = nota.getIncomingTask(7)
            Sort.sortTaskDateTarget(incoming_tasklst)
            for i in range(len(incoming_tasklst)):

                self.listWidget_incoming.addItem(incoming_tasklst[i].topic+(17-len(incoming_tasklst[i].topic))*" "
                                                 + str(incoming_tasklst[i].dateTarget.strftime("%Y-%m-%d %H:%M:%S")))
                self.listWidget_incoming.item(i).setFont(
                    QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))


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
        self.unAddTask.clicked.connect(self.cancelTask)
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
        self.fromWho = self.sender()

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
            if fromWho.objectName() == "taskTray":
                self.indextask = fromWho.currentRow()
                self.taskName_textEdit.setPlainText(
                    today_tasklst[self.indextask].topic)

                # self.task_description.setPlainText(
                #     today_tasklst[self.indextask].description)
                # temptxt = incoming_tasklst[self.indextask].description
                # temptxt = temptxt.replace("\\n", '\n')
                # print(temptxt)

                self.task_description.setPlainText(
                    today_tasklst[self.indextask].description.replace("\\n", '\n'))

                self.dateTimeEdit.setDateTime(
                    today_tasklst[self.indextask].dateTarget)
            else:
                self.indextask = fromWho.currentRow()
                self.taskName_textEdit.setPlainText(
                    incoming_tasklst[self.indextask].topic)

                self.task_description.setPlainText(
                    incoming_tasklst[self.indextask].description.replace("\\n", '\n'))

                self.dateTimeEdit.setDateTime(
                    incoming_tasklst[self.indextask].dateTarget)
            self.saveNoteButton.disconnect()
            self.saveNoteButton.clicked.connect(self.saveTask)
            self.saveNoteButton.setText("SAVE")

    def saveTask(self):
        if self.sender().objectName() == "listWidget" or fromWho.objectName() == "taskTray":
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
        if fromWho.objectName() == "taskTray":
            self.goToHomeWeek()
        else:
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
            # self.task_description.overwriteMode(True)
            self.goToTaskWindow()
        else:
            self.warning.setVisible(True)

    def cancelTask(self):
        self.taskName_textEdit.clear()
        self.task_description.clear()
        print("UnSaved")
        if self.fromWho.objectName() == "addTask":
            self.goToTaskWindow()
        elif fromWho.objectName() == "taskTray":
            self.goToHomeWeek()
        else:
            self.goToTaskWindow()

    def goToHomeWeek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def mytxtChanged(self):
        # dont use max 30      textlistwidget will bug cant see anything in list
        maxlengthtext = 15
        if (len(self.taskName_textEdit.toPlainText())) > maxlengthtext:
            maxstringtext = self.taskName_textEdit.toPlainText()
            print(len(maxstringtext))
            self.taskName_textEdit.setPlainText(maxstringtext[:-1])

            cursor = self.taskName_textEdit.textCursor()
            cursor.setPosition(maxlengthtext)
            self.taskName_textEdit.setTextCursor(cursor)

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
        # global checkbox
        # checkbox = [True, True, True, True, True, True, True]
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
                self.currentDay = 3
            elif dayhw == "Fri":
                self.currentDay = 4
            elif dayhw == "Sat":
                self.currentDay = 5
            elif dayhw == "Sun":
                self.currentDay = 6
        global currentClickingDay_int_ttb, timetablelst
        self.currentDay_objectName = self.dayBarButtonList[currentClickingDay_int_ttb]
        # print("ಥ_ಥ", currentClickingDay_int_ttb)

        timetablelst = nota.getTimetableByday(currentClickingDay_int_ttb, 0)

        self.today_TimetableTray.clear()
        for i in range(len(timetablelst)):
            # print(timetablelst[i].topic)
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
                # timetablelst = nota.getTimetableAll(i)
                timetablelst = nota.getTimetableByday(i, 0)

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
                global timetablelst
                timetablelst = nota.getTimetableByday(i, 0)
                self.today_TimetableTray.clear()
                for i in range(len(timetablelst)):
                    self.today_TimetableTray.addItem(timetablelst[i].topic)

            else:
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')
        self.currentEditingDay = self.currentDay_objectName

    def setCurrent(self):
        self.currentEditingDay = self.sender().objectName()
        # รกมาก เดะค่อยม่าแก้อีกที
        if self.sender().objectName() == self.currentDay_objectName:
            self.label.setText("TODAY")
        elif self.sender().objectName() == self.dayBarButtonList[0]:
            self.label.setText("MONDAY")
        elif self.sender().objectName() == self.dayBarButtonList[1]:
            self.label.setText("TUESDAY")
        elif self.sender().objectName() == self.dayBarButtonList[2]:
            self.label.setText("WEDNESDAY")
        elif self.sender().objectName() == self.dayBarButtonList[3]:
            self.label.setText("THURSDAY")
        elif self.sender().objectName() == self.dayBarButtonList[4]:
            self.label.setText("FRIDAY")
        elif self.sender().objectName() == self.dayBarButtonList[5]:
            self.label.setText("SATURDAY")
        elif self.sender().objectName() == self.dayBarButtonList[6]:
            self.label.setText("SUNDAY")

        for i in range(len(self.listDayButton)):
            if self.listDayButton[i].objectName() == self.sender().objectName():
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')
                global timetablelst, currentClickingDay_int_ttb
                timetablelst = list()
                currentClickingDay_int_ttb = i
                timetablelst = nota.getTimetableByday(i, 0)
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
        self.warning.setVisible(False)
        self.unAddButton.clicked.connect(self.goToTimeTableWindow)
        self.noteButton.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.goToHomeWeek)
        self.taskButton.clicked.connect(self.goToTaskWindow)
        self.saveTimetableButton.disconnect()
        self.saveTimetableButton.clicked.connect(self.addTimetable)
        self.cancelTimetableButton.clicked.connect(self.cancelTimetable)
        self.welcomeUser.setText("Welcome,  "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))
        self.checkBox = [True,True,True,True,True,True,True]

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
            # a = a[11:13]
            # a = int(a)
            b = str(timetablelst[self.indexTimetable].dateTarget)

            if len(a) > 10 and len(b) > 10:  # เขียนดักบั๊ก
                a = a[11:13]
                b = b[14:16]
            else:
                a = a[:2]
                b = b[2:4]
            self.timetable_Edittime.setTime(time(int(a), int(b)))

            self.timetabletitleName_textEdit.setPlainText(
                timetablelst[self.indexTimetable].topic)
            # self.timetable_description.setPlainText(
            #     timetablelst[self.indexTimetable].description)
            self.timetable_description.setPlainText(
                timetablelst[self.indexTimetable].description.replace("\\n", '\n'))
            dayListInRecord = nota.getDayFromTimetableID(timetablelst[self.indexTimetable])
            for i in range(len(self.checkBox)):
                if i in dayListInRecord:
                    self.checkBox[i] = False
                    self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')
            self.saveTimetableButton.disconnect()
            self.saveTimetableButton.clicked.connect(self.saveTimetable)
            self.saveTimetableButton.setText("SAVE")

        for i in range(len(self.listDayButton)):
            # SET clicked connect
            self.listDayButton[i].clicked.connect(self.setCurrent)

    def setCurrent(self):
        for i in range(len(self.listDayButton)):
            if self.listDayButton[i].objectName() == self.sender().objectName() and self.checkBox[i] == True:
                self.checkBox[i] = False
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: #FFAC4B; color: white; border-radius: 8px; }')

            elif self.listDayButton[i].objectName() == self.sender().objectName() and self.checkBox[i] == False:
                self.checkBox[i] = True
                self.listDayButton[i].setStyleSheet(
                    'QPushButton {background: rgb(228, 226, 199); color: black; border-radius: 8px;  }')

    def saveTimetable(self):  # ได้แค่ของ Today
        timetablelst[self.indexTimetable].topic = self.timetabletitleName_textEdit.toPlainText()

        # timetablelst[self.indexTimetable].description = self.timetable_description.toPlainText()
        temptext = self.timetable_description.toPlainText()
        timetablelst[self.indexTimetable].description = '\\n'.join(
            temptext.splitlines())

        a = self.timetable_Edittime.dateTime().toPyDateTime()
        timetablelst[self.indexTimetable].dateTarget = a
        l=list()
        for i in range(len(self.checkBox)):
            if self.checkBox[i] == False:
                l.append(i)
        flag = False
        for i in self.checkBox:
            if i == False:  # ถ้ามีการกดปุ่ม flagเป็น True
                flag = True
        if self.timetabletitleName_textEdit.toPlainText() == "" or not flag:
            self.warning.setVisible(True)
            if self.timetabletitleName_textEdit.toPlainText() == "":
                self.warning.setText("Please fill in task name!!!")
            if not flag:
                self.warning.setText("Please choose at least one day!!")
        else:
            nota.editTimetable(timetablelst[self.indexTimetable],l)
            if fromWho.objectName() in ["today_TimetableTray", "completed_TimetableTray"]:
                self.goToTimeTableWindow()
            else:
                self.goToHomeWeek()

    def addTimetable(self):
        time = self.timetable_Edittime.dateTime()
        time = time.toPyDateTime()
        flag = False
        for i in self.checkBox:
            if i == False:  # ถ้ามีการกดปุ่ม flagเป็น True
                flag = True
        if self.timetabletitleName_textEdit.toPlainText() == "" or not flag:
            self.warning.setVisible(True)
            if self.timetabletitleName_textEdit.toPlainText() == "":
                self.warning.setText("Please fill in task name!!!")
            if not flag:
                self.warning.setText("Please choose at least one day!!")
        else:
            temp = list()
            for i in range(len(self.checkBox)):
                if self.checkBox[i] == False:
                    temp.append(i)
            temptext = self.timetable_description.toPlainText()
            temptext = '\\n'.join(temptext.splitlines())
            nota.addTimetable(time.strftime("%H:%M:%S"), 1, self.timetabletitleName_textEdit.toPlainText(
            ), temptext, temp, 0, 0, -1)

            global timetablelst
            timetablelst = nota.getTimetableByday(
                currentClickingDay_int_ttb, 0)
            self.timetabletitleName_textEdit.clear()
            self.timetable_description.clear()
            self.goToTimeTableWindow()

    def cancelTimetable(self):
        self.timetabletitleName_textEdit.clear()
        self.timetable_description.clear()
        print("UNSAVE TIME TABLE")

        global fromWho
        if fromWho.objectName() in ["today_TimetableTray", "completed_TimetableTray"]:
            self.goToTimeTableWindow()
        else:
            self.goToHomeWeek()


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
        elif fromWho.objectName() in ['timeTableTray', 'today_TimetableTray']:
            self.edit.clicked.connect(self.goToAddTimeTable)
        elif fromWho.objectName() in ['taskTray', 'listWidget', 'listWidget_incoming']:
            self.edit.clicked.connect(self.goToAddTask)

    def markAsCompleted(self):
        if fromWho.objectName() in ["listWidget", "taskTray"]:
            today_tasklst[self.indextask].finish = 1
            nota.editRecord(today_tasklst[self.indextask])
            self.parent().refreshTable()
        elif fromWho.objectName() == "listWidget_incoming":
            incoming_tasklst[self.indextask].finish = 1
            nota.editRecord(incoming_tasklst[self.indextask])
            self.parent().refreshTable()
        elif fromWho.objectName() in ["today_TimetableTray", "timeTableTray"]:
            print("_>_>_>_>_>_>", timetablelst[self.indextask].topic)
            # timetablelst[self.indextask].finish =1
            nota.markCompleteTimetable(timetablelst[self.indextask], 1)

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
        if fromWho.objectName() in ["listWidget", "listWidget_incoming", "taskTray"]:
            if fromWho.objectName() == "taskTray":
                nota.deletRow(today_tasklst[self.indextask])
            else:
                nota.deletRow(incoming_tasklst[self.indextask])
        elif fromWho.objectName() == "noteTray":
            nota.deletRow(notelst[self.indextask])
        elif fromWho.objectName() in ["today_TimetableTray", "timeTableTray"]:
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
