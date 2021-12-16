import csv
import os
import datetime



class Nota:
    def __init__(self) -> None:
        self.userID = -1
        self.table = []
    
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
    # def showDateOfToday(self) :
    #     today = datetime.datetime.now()
    #     today= today.strftime("%d")
    #     return today           
    def showDateOfToday(self):
        today = datetime.datetime.today()
        return today   
    def writeDemo(self,txt:list):
        with open("aLotOfText.csv", "a",newline="",encoding="utf8") as f:
            fw = csv.writer(f)
            fw.writerow(txt)


    def readDemo(self,)->list:
        with open('aLotOfText.csv',newline="",encoding="utf8") as f:
            reader = csv.reader(f)
            return list(reader)

    def writeTaskTable(self,txt:list):
        with open("taskTable.csv", "a",newline="",encoding="utf8") as f:
            fw = csv.writer(f)
            fw.writerow(txt)

    def readTaskTable(self,)->list:
        with open('taskTable.csv',newline="",encoding="utf8") as f:
            reader = csv.reader(f)
            return list(reader)

    def refreshTable(self):
        temptable = self.readTaskTable()
        self.table.clear()
        for row in temptable:
            if int(row[1]) == self.userID:
                self.table.append(row)
        print("Table refreshed")
    #write : id(run) type date string
    #type 1=task 2=timetable 3=note
    def addNota(self,type,date,string):
        self.writeDemo([str(type),str(date),string])
        print("Task added")
        self

    # addNota(1,"2/2/2019","ส่งงาน")

    def login(self,user_name,password):
        auth = False
        table = self.readDemo()
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
        table = self.readDemo()
        for row in table:
            if reUser in row:
                print("This username hass been taken")
                return
        lastIndex = int(table[-1][0])+1
        # lastIndex = 2
        self.writeDemo([lastIndex,reUser,rePass])
        print("Register success")

    def task(self,dateTarget:datetime,type:int=0,topic:str="No detail",descrption:str="No descrption"):
        #index | user_id | type | date_create | date_target | string
        #type 0 = task | 1 = timetable | 2 = note |
        if os.path.isfile('./taskTable.csv') == False:
            self.writeTaskTable([0,self.userID,type,datetime.datetime.now(),dateTarget,topic,descrption])
        else:
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
                

    def showTask(self,userID:int,type:int):
        table = self.readTaskTable()
        result = []
        for row in table:
            if userID == int(row[1]) and type == int(row[2]):
                result.append([row[4],row[5]])
        for i in result:
            print(i)

    def today(userID):
        pass
    
# print(readDemo())
# print(login('nut','1234'))