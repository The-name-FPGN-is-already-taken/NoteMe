import csv
import os
import datetime
from notaBack import Record

class RecordTimetable:
    def __init__(self,taskID:int,userID:int,taskType:int,dateCreate:datetime,dateTarget,topic:str="No topic",
    description:str="No description",day:list=[],star=0,finish=0) -> None:
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


class Timetable:
    def __init__(self) -> None:
        self.table = []

    def writeTimeTable(self,txt:list):
        with open("timeTable.csv", "a",newline="",encoding="utf8") as f:
            fw = csv.writer(f)
            fw.writerow(txt)

    def readTaskTable(self)->list:
        with open('timeTable.csv',newline="",encoding="utf8") as f:
            reader = csv.reader(f)
            return list(reader)

    def readTaskTable(self)->list:
        with open('taskTable.csv',newline="",encoding="utf8") as f:
            reader = csv.reader(f)
            return list(reader)
    
    def writeTaskTable(self,txt:list):
        with open("taskTable.csv", "a",newline="",encoding="utf8") as f:
            fw = csv.writer(f)
            fw.writerow(txt)

    def updateTimeTable(self,userID):
        self.table.clear()
        temp = self.readTaskTable()
        for row in temp:
            if int(row(1)) == userID:
                self.table.append(RecordTimetable(int(row[0]),int(row[1]),int(row[2]),datetime.datetime.strptime(row[3],"%Y-%m-%d %H:%M:%S"),
                    datetime.datetime.strptime(row[4],"%H:%M:%S"),row[5],row[6], int(row[7]) ,int(row[8]),int(row[9])))

        print("Update Timetable")

    def isTimeTableInTaskTable(self,timeTableID:int):
        tempTable = self.readTaskTable()
        # for row
        for row in tempTable:
            if int(row[10]) == timeTableID:
                return True
        return False #Has timeTable in taskTable

    def addTimeTableInTasktable(self,obj:RecordTimetable):
        temp = self.readTaskTable()
        lastIndex = int(temp[-1][0])

        for i in range(len(obj.day)):
            self.writeTaskTable([lastIndex+1,obj.userID,1,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            datetime.date.today().strftime("%Y-%m-%d") + " " + obj.dateTarget.strftime("%H:%M:%S"),
            obj.topic,obj.descrption,obj.day[i],obj.star,obj.finish,obj.timeTableID])


    def makeTimeTableInTaskTable(self,userID):
        self.updateTimeTable()
        for row in self.table:
            if self.isTimeTableInTaskTable(row[0]) == False:

        
    def addTimeTable(self,userID,dateTarget:datetime.time,type:int=0,topic:str="No detail",descrption:str="No descrption",day:list=[],star=0,finish=0):
        '''dateTarget is only Time'''
        self.table = self.readTaskTable()
        lastIndex = int(self.table[-1][0])
        x = [lastIndex+1,userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),dateTarget,topic,descrption," ".join(str(x) for x in day),star,finish]
        self.writeTimeTable(x)



objTimetable = Timetable()
# x = [self.userID,type,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),dateTarget,topic,descrption,day,star,finish]
# x = [0,1,1,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"12:10:31","Topic","Descrption"," ".join(str(x) for x in [0,2,4]),0,0]
# objTimetable.writeTimeTable(x)
t = datetime.time(11,15,0)
objTimetable.addTimeTable(0,t,1,"New TimeTable test","This is new TT",[0,2,4])
y = objTimetable.readTaskTable()
print(y)



