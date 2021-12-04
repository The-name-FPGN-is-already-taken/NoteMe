import csv
import os
import datetime
from dataType import *
#Record
class Record:
    def __init__(self,taskID:int,userID:int,taskType:int,dateCreate:datetime,dateTarget,topic:str="No topic",
    description:str="No description",day:int=-1,star=0) -> None:
        """taskID | userID | type | date_create | date_target | string
        type 0 = task | 1 = timetable | 2 = note |"""
        self.taskID = taskID
        self.userID = userID
        self.taskType = taskType
        self.dateCreate = dateCreate
        self.dateTarget = dateTarget
        self.topic = topic
        self.description = description
        self.day = day
        self.star = star
    def __str__(self) -> str:
        return "{} {} {}".format(self.dateTarget,self.topic,self.description)

    def isTaskType(self):
        return self.taskType == 0
    
    def isTimetableType(self):
        return self.taskType == 1

    def isNoteType(self):
        return self.taskType == 2

class Sort:
    def sortTaskDateTarget(li:list,near:int=1):
        """Insert list of Task object / near = 1 is going to sort nearest come first (near = 0 far come first)"""
        #This is insertion sort
        for i in range(1,len(li)):
            key = li[i]
            j = i -1
            if near == 1:
                # while j >= 0 and (key.dateTarget.date() - datetime.date.today()).days < (li[j].dateTarget.date() - datetime.date.today()).days :
                while j >= 0 and key.dateTarget < li[j].dateTarget:
                    # print("swap")
                    li[j+1] = li[j]
                    j -= 1
            elif near == 0:
                # while j >= 0 and (key.dateTarget.date() - datetime.date.today()).days > (li[j].dateTarget.date() - datetime.date.today()).days :
                #     print("swap")
                while j >= 0 and key.dateTarget > li[j].dateTarget:
                    li[j+1] = li[j]
                    j -= 1
            li[j+1] = key

    def sortNote(li:list,new=1):
        for i in range(1,len(li)):
            key = li[i]
            j = i -1
            if new == 1:
                # while j >= 0 and (key.dateTarget.date() - datetime.date.today()).days < (li[j].dateTarget.date() - datetime.date.today()).days :
                while j >= 0 and key.dateCreate < li[j].dateCreate:
                    # print("swap")
                    li[j+1] = li[j]
                    j -= 1
            elif new == 0:
                # while j >= 0 and (key.dateTarget.date() - datetime.date.today()).days > (li[j].dateTarget.date() - datetime.date.today()).days :
                #     print("swap")
                while j >= 0 and key.dateCreate > li[j].dateCreate:
                    li[j+1] = li[j]
                    j -= 1
            li[j+1] = key

    def sortTimeTable(li:list,near:int=1):
        today = datetime.datetime.today().weekday()
        for i in range(1,len(li)):
            key = li[i]
            j = i -1
            if near == 1:
                while j >= 0 and key.day < li[j].day:
                    # print("swap")
                    li[j+1] = li[j]
                    j -= 1
            elif near == 0:
                while j >= 0 and key.day > li[j].day:
                    li[j+1] = li[j]
                    j -= 1
            li[j+1] = key
        
            
    def sortTimeTableBeginAt(li:list,dayTarget:int):
        linkList = Link()
        for i in li:
            linkList.append(i)
        node = linkList.head
        tempNode = None
        while node.next != None:
            if node.next.data.day >= dayTarget and tempNode == None:
                tempNode = node.next
                node.next = None
                node = tempNode
                print("Found")
            else:
                node = node.next
            
        else:
            node.next = linkList.head
            linkList.head = tempNode
        node = linkList.head
        li = []
        while node != None:
            li.append(node.data)
            node = node.next
        return li        

class Nota:
    def __init__(self) -> None:
        self.userID = -1
        self.table = Queue()
        self.toDoList = Stack()

    def __str__(self) -> str:
        s = ''
        for row in self.table.li:
            s += "{} {} {} {} {} {} {} {} {} \n".format(row.taskID,row.userID,row.taskType,row.dateCreate,row.dateTarget,row.topic,row.description,row.day,row.star)
        return s

    def showRecord(li):
        s = ''
        for row in li:
            s += "{} {} {} {} {} {} {} {} {} \n".format(row.taskID,row.userID,row.taskType,row.dateCreate,row.dateTarget,row.topic,row.description,row.day,row.star)
        print(s)
    def isLogin(self):
        if self.userID == -1:
            return False
        else:
            return True
    def deletRow(self,obj:Record):
        with open("taskTable.csv", "r") as f:
            lines = f.readlines()
        with open("taskTable.csv", "w") as f:
            for row in lines:
                if int(row.split(",")[0]) != int(obj.taskID):
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
                    datetime.datetime.strptime(row[4],"%Y-%m-%d %H:%M:%S"),row[5],row[6],int(row[7]),int(row[8])))
                elif int(row[2]) == 1:
                    self.table.enqueue(Record(int(row[0]),int(row[1]),int(row[2]),datetime.datetime.strptime(row[3],"%Y-%m-%d %H:%M:%S"),
                    datetime.datetime.strptime(row[4],"%H:%M:%S"),row[5],row[6],int(row[7]),int(row[8])))
                elif int(row[2]) == 2:
                    self.table.enqueue(Record(int(row[0]),int(row[1]),int(row[2]),datetime.datetime.strptime(row[3],"%Y-%m-%d %H:%M:%S"),
                    -1,row[5],row[6],int(row[7]),int(row[8])))
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

    def registor(self,reUser:str,rePass:str):
        #check,Are there exist
        self.isUserTableExis()
        table = self.readUserTable()
        if len(reUser.strip()) > 0 and len(rePass.strip()) > 0:
            for row in table:
                if reUser in row:
                    print("This username hass been taken")
                    return False
            lastIndex = int(table[-1][0])+1
            self.writeUserTable([lastIndex,reUser,rePass])
            print("Register success")
            return True
        else:
            print("Please enter username and password")
            return False
    def isTaskTableExis(self):
        if os.path.isfile('./taskTable.csv') == False:
            self.writeTaskTable([-1,-1,-1,"date","dateTarget","topic","descrption"])
    
    def isUserTableExis(self):
        if os.path.isfile('./userTable.csv') == False:
            self.writeUserTable([-1,"username","password"])


    def addRecord(self,dateTarget:datetime,type:int=0,topic:str="No detail",descrption:str="No descrption",day:int=-1,star=False):
        """For timetable dateTarget is time"""
        """taskID | userID | type | date_create | date_target | string
        type 0 = task | 1 = timetable | 2 = note |"""
        self.isTaskTableExis()
        

        table = self.readTaskTable()
        lastIndex = int(table[-1][0])
        if type == 0:
            #type = 0 is task (have date and maybe time)
            self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),dateTarget,topic,descrption,day,star])
        elif type == 1:
            #type = 1 is timetable (Have only day of week)
            #day of week 0 = Monday ... 6 = Sunday
            # self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),dateTarget,topic,descrption])
            self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now().strftime("%H:%M:%S"),dateTarget,topic,descrption,day,star])
        elif type == 2:
            #type = 2 is Note 
            #No time target
            self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),-1,topic,descrption,day,star])
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

    def getIncomingTask(self,delta:int)->list:
        result = []
        for row in self.table.li:
            # print((row.dateTarget.date() - datetime.date.today()).days)
            if row.isTaskType() and 0 <= (row.dateTarget.date() - datetime.date.today()).days <= delta:
                result.append(row)
        # print(result)
        return result

    def getTimetableAll(self):
        result = []
        for row in self.table.li:
            if row.isTimetableType():
                result.append(row)
        return result

    def getNoteAll(self):
        result = []
        for row in self.table.li:
            if row.isNoteType():
                result.append(row)
        return result

    def editRecord(self,obj:Record):
        with open("taskTable.csv", "r") as f:
            lines = f.readlines()
        with open("taskTable.csv", "w") as f:
            for row in lines:
                if int(row.split(",")[0]) == int(obj.taskID):
                    f.write("{},{},{},{},{},{},{},{},{}\n".format(obj.taskID,obj.userID,obj.taskType,obj.dateCreate,obj.dateTarget,obj.topic,obj.description,obj.day,obj.star))
                else:
                    f.write(row)
        self.refreshTable()
    
    def addTimeTable(self,dateTarget:datetime,type:int=0,topic:str="No detail",descrption:str="No descrption"):
        pass

    def addToDoList(self,obj:Record):
        self.toDoList.append(obj)
        
# print(readUserTable())
# print(login('nut','1234'))
nota = Nota()
# nota.registor("parn55",231)
# nota.login("catty","5")
# nota.getTaskToday()
# nota.getIncomingTask(7)
nota.login("catty","5")
cat = nota.getTimetableAll()
Nota.showRecord(cat)
Sort.sortTimeTable(cat)
Nota.showRecord(cat)
Sort.sortTimeTableBeginAt(cat,3)
Nota.showRecord(cat)

# nota.addRecord(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),0,"Test","testNut")

# print(nota.showRecord(cat))
# Sort.sortTaskDateTarget(cat,1)
# print(nota.showRecord(cat))




# inputTime = datetime.datetime.today().strftime("%w %H:%M:%S") 
# inputTime = "6 17:10:21"
# print("Write in CSV :",inputTime)
# s = inputTime
# t = datetime.datetime.strptime(s.split()[1],"%H:%M:%S")
# wDay = int(s.split()[0])
# print(wDay)
# print(t.time())


# cat[2].topic = "Father died"
# nota.editRecord(cat[2])
# nota.deletRow(cat[2])
# s = "-1"
# print(int(s))

# cat = nota.getTimetableAll()
# cat = nota.getNoteAll()
#-----------------------------g
# t1 = datetime.datetime(2021,11,26,14,10,11)
# t2 = datetime.datetime(2021,11,30,16,11,15)
# print((t2-t1).seconds)
