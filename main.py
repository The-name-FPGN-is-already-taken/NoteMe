import sys 
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import  *
from notaBack import *
from note import Note
note1 = list()
    
class LoginWindow(QDialog):#editing here
    
    def __init__(self) :
        super(LoginWindow,self).__init__()
        loadUi("nota.ui",self)
        self.warning.setVisible(False)
        self.loginButton.clicked.connect(self.loginIn)
        self.signupButton.clicked.connect(self.LoginToSignUp)
    def loginIn(self):
        global userName
        userName = self.username.text()
        password = self.userPassword.text()
        nota.login(userName,password)

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
    def __init__(self) :
        super(SignUpWindow,self).__init__()
        loadUi("signUp_temp.ui",self)
        self.warning.setVisible(False)
        self.signUpButton.clicked.connect(self.registing)
        self.signInButton.clicked.connect(self.goToLoginWindow)
        # self.welComeUser.setText(nota.)
    def registing(self): 
        global userName
        userName = self.username.text()
        password = self.userPassword.text()
        if nota.registor(userName,password):
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
    def __init__(self) :
        super(HomeWeek_window,self).__init__()
        loadUi("home_week.ui",self)
        global userName
        self.welcomeUser.setText("Welcome, "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))
        self.currentDay = -1 # ยังไม่เลือกวัน = Today, Monday =0 .... Sunday = 6
        self.signOutButton.clicked.connect(self.homeWeekToLogin)
        self.calendar_tab.clicked.connect(self.homeWeekToHomeCal)
        self.noteButton.clicked.connect(self.homeWeekToNoteWindow)
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

        global userName
        self.welcomeUser.setText("Welcome, "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

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
        
class HomeCal_window(QDialog):
    def __init__(self) :
        super(HomeCal_window,self).__init__()
        loadUi("home_cal.ui",self)
        self.currentbutton = -1
        self.signOutButton.clicked.connect(self.goToLoginWindow)
        self.weekView_tab.clicked.connect(self.goToHomeWeek)
        self.noteButton.clicked.connect(self.homeCalToNoteWindow)
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
       
        global userName
        self.welcomeUser.setText("Welcome, "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))

    def goToLoginWindow(self):
        loginWindow = LoginWindow()
        widget.addWidget(loginWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def goToHomeWeek(self):
        homeWeek_window = HomeWeek_window()
        widget.addWidget(homeWeek_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def homeCalToNoteWindow(self):
        note_window = Note_window()
        widget.addWidget(note_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Note_window(QDialog):
    def __init__(self) :
        super(Note_window,self).__init__()
        loadUi("note_window.ui",self)
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
        global userName
        self.welcomeUser.setText("Welcome, "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))
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
class AddNoteWindow(QDialog):
    def __init__(self) :
        super(AddNoteWindow,self).__init__()
        loadUi("add_note.ui",self)
        self.addNote.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.addNoteWindowToHomeWeek)
        self.taskButton.clicked.connect(self.goToTaskWindow)
        
        self.saveNoteButton.clicked.connect(self.saveNote)
        self.cancelAdding.clicked.connect(self.cancelNote)
        global userName
        self.welcomeUser.setText("Welcome, "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))
# NUT
    def saveNote(self):
        note1.append(Note(self.noteName.toPlainText(),
                          self.textField.toPlainText()))
        self.noteName.clear()
        self.textField.clear()
        print("Saved")
        self.goToNoteWindow()

    def cancelNote(self):
        self.noteName.clear()
        self.textField.clear()
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
class Task_window(QDialog):
    def __init__(self) :
        super(Task_window,self).__init__()
        loadUi("task_window.ui",self)
        self.addTask.clicked.connect(self.goToAddTask)
        self.noteButton.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.taskWindowToHomeWeek)
        global userName
        self.welcomeUser.setText("Welcome, "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))
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
    def __init__(self) :
        super(AddTaskWindow,self).__init__()
        loadUi("add_task_window.ui",self)
        
        self.unAddTask.clicked.connect(self.goToTaskWindow)
        self.noteButton.clicked.connect(self.goToNoteWindow)
        self.homeButton.clicked.connect(self.addTaskWindowToHomeWeek)
        global userName
        self.welcomeUser.setText("Welcome, "+userName)
        self.date.setText(nota.showDateOfToday().strftime("%B %d, %Y"))
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
#main
app =QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginWindow = LoginWindow()
global nota 
nota= Nota()
widget.addWidget(loginWindow)
widget.show()
try: 
    sys.exit(app.exec_())
except:
    print("No im not out!")
