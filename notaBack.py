import csv
import os
import datetime
from dataType import *
#Record
class Record:
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

    def isTaskType(self):
        return self.taskType == 0
    
    def isTimetableType(self):
        return self.taskType == 1

    def isNoteType(self):
        return self.taskType == -1

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
        #เอาจาก string เป็น Task Object
        self.isTaskTableExis()
        temptable = self.readTaskTable()
        self.table.clear()
        for row in temptable:
            if int(row[1]) == self.userID:
                if int(row[2]) == 0:
                    self.table.enqueue(Record(int(row[0]),int(row[1]),int(row[2]),datetime.datetime.strptime(row[3],"%Y-%m-%d %H:%M:%S"),
                    datetime.datetime.strptime(row[4],"%Y-%m-%d %H:%M:%S"),row[5],row[6]))
                elif int(row[2]) == 1:
                    self.table.enqueue(Record(int(row[0]),int(row[1]),int(row[2]),datetime.datetime.strptime(row[3],"%Y-%m-%d %H:%M:%S"),
                    int(row[4]),row[5],row[6]))
                elif int(row[2]) == 1:
                    self.table.enqueue(Record(int(row[0]),int(row[1]),int(row[2]),datetime.datetime.strptime(row[3],"%Y-%m-%d %H:%M:%S"),
                    -1,row[5],row[6]))
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

    def logout(self):
        self.table.li.clear()
        self.userID = -1        

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


    def addRecord(self,dateTarget:datetime,type:int=0,topic:str="No detail",descrption:str="No descrption"):
        """taskID | userID | type | date_create | date_target | string
        type 0 = task | 1 = timetable | 2 = note |"""
        self.isTaskTableExis()
        

        table = self.readTaskTable()
        lastIndex = int(table[-1][0])
        if type == 0:
            #type = 0 is task (have date and maybe time)
            self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),dateTarget,topic,descrption])
        elif type == 1:
            #type = 1 is timetable (Have only day of week)
            #day of week 0 = Monday ... 6 = Sunday
            self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),dateTarget,topic,descrption])
        elif type == 2:
            #type = 2 is Note 
            #No time target
            self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),-1,topic,descrption])
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

    def getTaskByDate(self,targetDate:datetime):
        """targetDate format is YEAR-MONTH-DAY ex.. 2022-01-10"""
        # tempDate = datetime.datetime.strptime(targetDate,"%Y-%m-%d")
        result = []
        for row in self.table.li:
            if row.isTaskType() and targetDate == row.dateTarget.date():
                result.append(row)
        # print(result[0].topic)
        return result

    def getTaskToday(self)->list:
        """Return queue of Task obj"""
        # print(datetime.datetime.today())
        return self.getTaskByDate(datetime.date.today())

    def getIncomingTask(self,delta:int):
        result = []
        for row in self.table.li:
            if row.isTaskType() and (row.dateTarget.date() - datetime.date.today()).days <= delta:
                result.append(row)
        print(result)
        return result

    def getTimetableByAll(self):
        result = []
        for row in self.table.li:
            if row.isTimetableType():
                result.append(row)
        return result


        
# print(readUserTable())
# print(login('nut','1234'))
nota = Nota()
# nota.registor("parn55",231)
nota.login("catty","5")
# nota.getTaskToday()
nota.getIncomingTask(7)

