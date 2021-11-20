import csv
import os
import datetime

def deletRow(row):
    with open("aLotOfText.csv", "r") as f:
        lines = f.readlines()
    with open("aLotOfText.csv", "w") as f:
        
        # for line in lines:
        #     if line.strip("\n") != row:
        #         print("what")
        #         f.write(line)
        i = 0
        for line in lines:
            print(i)
            if i != row:
                print("what")
                f.write(line)
            i += 1
                

def writeDemo(txt:list):
    with open("aLotOfText.csv", "a",newline="",encoding="utf8") as f:
        fw = csv.writer(f)
        fw.writerow(txt)


def readDemo()->list:
    with open('aLotOfText.csv',newline="",encoding="utf8") as f:
        reader = csv.reader(f)
        return list(reader)

def writeTaskTable(txt:list):
    with open("taskTable.csv", "a",newline="",encoding="utf8") as f:
        fw = csv.writer(f)
        fw.writerow(txt)

def readTaskTable()->list:
    with open('taskTable.csv',newline="",encoding="utf8") as f:
        reader = csv.reader(f)
        return list(reader)

#write : id(run) type date string
#type 1=task 2=timetable 3=note
def addNota(type,date,string):
    writeDemo([str(type),str(date),string])
    print("Task added")

# addNota(1,"2/2/2019","ส่งงาน")

def login(user_name,password):
    auth = False
    table = readDemo()
    for row in table:
        if row[1] == user_name and row[2] == password:
            userID = int(row[0])
            
            auth = True
            break
    if auth == False:
        print("User or Pasword is incorrect")
    else:
        print("Login success")
        return userID

def registor(reUser,rePass):
    #check,Are there exist
    table = readDemo()
    for row in table:
        if reUser in row:
            print("This username hass been taken")
            return
    lastIndex = int(table[-1][0])+1
    writeDemo([lastIndex,reUser,rePass])
    print("Register success")

def task(userID,dateTarget:datetime,type:int=0,txt:str="No detail"):
    #index | user_id | type | date_create | date_target | string
    #type 0 = task | 1 = timetable | 2 = note |

    if os.path.isfile('./taskTable.csv') == False:
        writeTaskTable([0,userID,type,datetime.datetime.now(),dateTarget,txt])
    else:
        table = readTaskTable()
        lastIndex = int(table[-1][0])
        if type == 0:
            #type = 0 is task (have date and maybe time)
            writeTaskTable([lastIndex+1,userID,type,datetime.datetime.now(),dateTarget,txt])
        elif type == 1:
            #type = 1 is timetable (Have only day of week)
            #day of week 0 = Monday ... 6 = Sunday
            writeTaskTable([lastIndex+1,userID,type,datetime.datetime.now(),dateTarget,txt])
        elif type == 2:
            #type = 2 is Note 
            #No time target
            writeTaskTable([lastIndex+1,userID,type,datetime.datetime.now(),dateTarget,txt])
        else:
            print("No type")
            

def showTask(userID:int,type:int):
    table = readTaskTable()
    result = []
    for row in table:
        if userID == int(row[1]) and type == int(row[2]):
            result.append([row[4],row[5]])
    for i in result:
        print(i)
    
    

# print(readDemo())
# print(login('nut','1234'))

