import csv
import os
import datetime
from typing import Mapping
from dataType import *
#Record
class Record:
    def __init__(self,taskID:int,userID:int,taskType:int,dateCreate:datetime,dateTarget,topic:str="No topic",
    description:str="No description",day:int=-1,star=0,finish=0) -> None:
        """taskID | userID | type | date_create | date_target | string | 
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
        self.finish = finish
    def __str__(self) -> str:
        return "{} {} {} {}".format(self.dateCreate,self.dateTarget,self.topic,self.description)

    def isTaskType(self):
        return self.taskType == 0
    
    def isTimetableType(self):
        return self.taskType == 1

    def isNoteType(self):
        return self.taskType == 2

    def isFinish(self):
        if self.finish == 1:
            return True
        else:
            return False

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


    def sortTimeTable(self,li:list,near:int=1):
        for i in li:
            i.head = self.mergeSort(i.head)
    
    def getFinishTask(self):
        """Only finish task"""
        result = []
        for row in self.table.li:
            if row.isTaskType() and row.isFinish() == True and row.dateTarget == datetime.datetime.today():
                result.append(row)
        return result
    
    def sortedMerge(self, a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a
        if a.data.dateTarget <= b.data.dateTarget:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
     
    def mergeSort(self, h):
         
        if h == None or h.next == None:
            return h
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
        middle.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(nexttomiddle)
 
        sortedlist = self.sortedMerge(left, right)
        return sortedlist
     
    def getMiddle(self, head):
        if (head == None):
            return head
        slow = head
        fast = head
        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow
                   
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

    def partition(self,arr, low, high,new):
        i = (low-1)         # index of smaller element
        pivot = arr[high]     # pivot
    
        for j in range(low, high):
    
            if arr[j].dateCreate <= pivot.dateCreate and new == 1:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
            elif arr[j].dateCreate >= pivot.dateCreate and new == 0:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
    
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)
 
    def quickSort(self,arr, low, high,new):
        if len(arr) == 1:
            return arr
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high,new)
    
            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi-1,new)
            self.quickSort(arr, pi+1, high,new)

    def sortNote(li:list,new=1):
        sort = Sort()
        sort.quickSort(li, 0, len(li)-1,new)

    def transposition(li:list,index:int):
        if index > 0:
            li[index],li[index-1] = li[index-1],li[index]

class Nota:
    def __init__(self) -> None:
        self.userID = -1
        self.table = Queue()
        self.toDoList = Stack()
        self.timeTable = list()
        for i in range(7):
            self.timeTable.append(Link())

    def __str__(self) -> str:
        s = ''
        for row in self.table.li:
            s += "{} {} {} {} {} {} {} {} {} {} \n".format(row.taskID,row.userID,row.taskType,row.dateCreate,row.dateTarget,row.topic,row.description,row.day,row.star,row.finish)
        return s

    def showRecord(li):
        s = ''
        for row in li:
            s += "{} {} {} {} {} {} {} {} {} {} \n".format(row.taskID,row.userID,row.taskType,row.dateCreate,row.dateTarget,row.topic,row.description,row.day,row.star,row.finish)
        print(s)
    def isLogin(self):
        if self.userID == -1:
            return False
        else:
            return True
    def deletRow(self,obj:Record):
        with open("taskTable.csv", "r",encoding="utf8") as f:
            lines = f.readlines()
        with open("taskTable.csv", "w",encoding="utf8") as f:
            for row in lines:
                if int(row.split(",")[0]) != int(obj.taskID):
                    f.write(row)
        self.refreshTable()
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
                    datetime.datetime.strptime(row[4],"%Y-%m-%d %H:%M:%S"),row[5],row[6],int(row[7]),int(row[8]),int(row[9])))
                elif int(row[2]) == 1:
                    self.table.enqueue(Record(int(row[0]),int(row[1]),int(row[2]),datetime.datetime.strptime(row[3],"%Y-%m-%d %H:%M:%S"),
                    datetime.datetime.strptime(row[4],"%H:%M:%S"),row[5],row[6],int(row[7]),int(row[8]),int(row[9])))
                elif int(row[2]) == 2:
                    self.table.enqueue(Record(int(row[0]),int(row[1]),int(row[2]),datetime.datetime.strptime(row[3],"%Y-%m-%d %H:%M:%S"),
                    -1,row[5],row[6],int(row[7]),int(row[8]),int(row[9])))
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

    def checkStrForAdd(s:str)->bool:
        if ',' in s:
            return False
        else:
            return True

    def addRecord(self,dateTarget:datetime,type:int=0,topic:str="No detail",descrption:str="No descrption",day:int=-1,star=0,finish=0):
        """For timetable dateTarget is time"""
        """taskID | userID | type | date_create | date_target | string
        type 0 = task | 1 = timetable | 2 = note |"""
        try:
            self.isTaskTableExis()
            table = self.readTaskTable()
            lastIndex = int(table[-1][0])
            if type == 0:
                #type = 0 is task (have date and maybe time)
                self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),dateTarget,topic,descrption,day,star,finish])
            elif type == 1:
                #type = 1 is timetable (Have only day of week)
                #day of week 0 = Monday ... 6 = Sunday
                # self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),dateTarget,topic,descrption])
                self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),dateTarget,topic,descrption,day,star,finish])
            elif type == 2:
                #type = 2 is Note 
                #No time target
                self.writeTaskTable([lastIndex+1,self.userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),-1,topic,descrption,day,star,finish])
            else:
                print("No type")
            self.refreshTable()
        except:
            print("Error in add fuction")
                

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
    #Get All task for home page
    def getAllTask(self)->list:
        """Finish and not finish task"""
        result = []
        for row in self.table.li:
            if row.isTaskType():
                result.append(row)
        return result

    def getNotFinishTask(self):
        """Only not finish task"""
        result = []
        for row in self.table.li:
            if row.isTaskType() and row.isFinish() == False:
                result.append(row)
        return result
    
    def getTodayNotFinishTask(self):
        """Only not finish task for today"""
        result = []
        for row in self.table.li:
            if row.isTaskType() and row.isFinish() == False and  (row.dateTarget.date() - datetime.date.today()).days == 0:
                result.append(row)
        return result
    
    def getIncomingNotFinishTask(self):
        """Only not finish task for incoming 7 days"""
        result = []
        for row in self.table.li:
            if row.isTaskType() and 0 <= (row.dateTarget.date() - datetime.date.today()).days <= 7 and row.isFinish() == False:
                result.append(row)
        return result

    def getFinishTask(self):
        """Only finish task"""
        result = []
        for row in self.table.li:
            if row.isTaskType() and row.isFinish() == True:
                result.append(row)
        return result
    
    def getTodayFinishTask(self):
        """Only finish task for today"""
        result = []
        for row in self.table.li:
            if row.isTaskType() and row.isFinish() == True and row.dateTarget == datetime.datetime.today():
                result.append(row)
        return result

    def getTimetableAll(self,day):
        self.timeTable.clear()
        for i in range(7):
            self.timeTable.append(Link())
        for row in self.table.li:
            if row.isTimetableType():
                # result.append(row)
                self.timeTable[row.day].append(row)
        sort = Sort()
        sort.sortTimeTable(self.timeTable)
        result = []
        node = self.timeTable[day].head
        while node != None:
            result.append(node.data)
            node = node.next
        return result


    def getNoteAll(self):
        result = []
        for row in self.table.li:
            if row.isNoteType():
                result.append(row)
        return result

    def editRecord(self,obj:Record):
        with open("taskTable.csv", "r",encoding="utf8") as f:
            lines = f.readlines()
        with open("taskTable.csv", "w",encoding="utf8") as f:
            for row in lines:
                if int(row.split(",")[0]) == int(obj.taskID):
                    f.write("{},{},{},{},{},{},{},{},{},{}\n".format(obj.taskID,obj.userID,obj.taskType,obj.dateCreate
                    ,obj.dateTarget,obj.topic,obj.description,obj.day,obj.star,obj.finish))
                else:
                    f.write(row)
        self.refreshTable()

    def addToDoList(self,obj:Record):
        self.toDoList.append(obj)

# s1 = "Task1p\t\t\t\tspace"
# s2 = "Task1poioio\t\t\t\tspace7"
# print(s1)
# print(s2)