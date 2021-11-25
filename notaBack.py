import csv
import os
import datetime
from dataType import *

class Task:
    def __init__(self,taskID,userID,taskType,dateCreate,dateTarget,topic="No topic",description="No description") -> None:
        """taskID | userID | type | date_create | date_target | string
        type 0 = task | 1 = timetable | 2 = note |"""
        self.taskID = taskID
        self.userID = userID
        self.taskType = taskType
        self.dateCreate = dateCreate
        self.dateTarget = dateTarget
        self.topic = topic
        self.description = description

    def __str__(self) -> str:
        return "{} {} {}".format(self.dateTarget,self.topic,self.description)

class Nota:
    def __init__(self) -> None:
        self.userID = -1
        self.table = Queue()
    
    def isLogin(self):
        if self.userID == -1:
            return False
        else:
            return True
    def deletRow(self,taskID):
        with open("aLotOfText.csv", "r") as f:
            lines = f.readlines()
        with open("aLotOfText.csv", "w") as f:
            for row in lines:
                if int(row[0]) != taskID:
                    f.write(row)
        self.refreshTable()
            # i = 0
            # for line in lines:
            #     print(i)
            #     if i != row:
            #         f.write(line)
            #     i += 1
    def showDateOfToday(self):
        today = datetime.datetime.today()
        return today

    def writeUserTable(self,txt:list):
        with open("userTable.csv", "a",newline="",encoding="utf8") as f:
            fw = csv.writer(f)
            fw.writerow(txt)


    def readUserTable(self)->list:
        with open('userTable.csv',newline="",encoding="utf8") as f:
            reader = csv.reader(f)
            return list(reader)

    def writeTaskTable(self,txt:list):
        with open("taskTable.csv", "a",newline="",encoding="utf8") as f:
            fw = csv.writer(f)
            fw.writerow(txt)

    def readTaskTable(self)->list:
        with open('taskTable.csv',newline="",encoding="utf8") as f:
            reader = csv.reader(f)
            return list(reader)

    def refreshTable(self):
        self.isTaskTableExis()
        temptable = self.readTaskTable()
        self.table.clear()
        for row in temptable:
            if int(row[1]) == self.userID:
                self.table.enqueue(Task(int(row[0]),int(row[1]),int(row[2]),row[3],row[4],row[5],row[6]))
        print("Table refreshed")
    #write : id(run) type date string
    #type 1=task 2=timetable 3=note
    def addNota(self,type,date,string):
        self.writeUserTable([str(type),str(date),string])
        print("Task added")


    # addNota(1,"2/2/2019","ส่งงาน")

    def login(self,user_name,password):
        self.isUserTableExis()
        auth = False
        table = self.readUserTable()
        for row in table:
            if row[1] == user_name and row[2] == password:
                self.userID = int(row[0])
                
                auth = True
                break
        if auth == False:
            print("User or Pasword is incorrect")
        else:
            self.refreshTable()
            print("Login success")        

    def registor(self,reUser,rePass):
        #check,Are there exist
        self.isUserTableExis()
        table = self.readUserTable()
        for row in table:
            if reUser in row:
                print("This username hass been taken")
                return False
        lastIndex = int(table[-1][0])+1
        self.writeUserTable([lastIndex,reUser,rePass])
        print("Register success")
        return True

    def isTaskTableExis(self):
        if os.path.isfile('./taskTable.csv') == False:
            self.writeTaskTable([-1,-1,-1,"date","dateTarget","topic","descrption"])
    
    def isUserTableExis(self):
        if os.path.isfile('./userTable.csv') == False:
            self.writeUserTable([-1,"username","password"])


    def task(self,dateTarget:datetime,type:int=2,topic:str="No detail",descrption:str="No descrption"):
        """taskID | userID | type | date_create | date_target | string
        type 0 = task | 1 = timetable | 2 = note |"""
        self.isTaskTableExis()
        

        table = self.readTaskTable()
        lastIndex = int(table[-1][0])
        if type == 0:
            #type = 0 is task (have date and maybe time)
            self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now(),dateTarget,topic,descrption])
        elif type == 1:
            #type = 1 is timetable (Have only day of week)
            #day of week 0 = Monday ... 6 = Sunday
            self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now(),dateTarget,topic,descrption])
        elif type == 2:
            #type = 2 is Note 
            #No time target
            self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now(),dateTarget,topic,descrption])
        else:
            print("No type")
        self.refreshTable()
                

    def showTask(self,userID:int,type:int):
        table = self.readTaskTable()
        result = []
        for row in table:
            if userID == int(row[1]) and type == int(row[2]):
                result.append([row[4],row[5]])
        for i in result:
            print(i)

    def showTaskByDate(self,targetDate=0):
        """targetDate format is YEAR-MONTH-DAY ex.. 2022-01-10"""
        for row in self.table.li:
            print(row)
    

# print(readUserTable())
# print(login('nut','1234'))
# nota = Nota()
# nota.registor("parn55",231)
