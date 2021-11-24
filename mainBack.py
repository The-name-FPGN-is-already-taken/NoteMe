
from datetime import date
import dataType
from testCSV import *

#sim for testing not implement

obj = Nota()

inp = ''
table = None
while inp != "q":
    print("....User: {}".format(obj.userID))
    inp = input("Enter mode : ")
    if inp == 're':
        txt = input("username password : ").split()
        obj.registor(txt[0],txt[1])
    elif inp == 'login':
        txt = input("username password : ").split()
        obj.login(txt[0],txt[1])
        

            
    elif inp == 'add':
        if obj.isLogin():
            taskType = int(input("Type : "))
            if taskType == 0:
                dateInp = list(map(int,input("Date Month Year : ").split()))
                dateTarget = datetime.date(dateInp[2],dateInp[1],dateInp[0])
            elif taskType == 1:
                dateTarget = int(input("Enter day : "))
            elif taskType == 2:
                dateTarget = None
            
            txt = input("Detail : ")
            des = input("Descrpition : ")
            obj.task(dateTarget,taskType,txt,des)
    elif inp == 'del':
        #Must input taskID
        inp = int(input("Enter row :"))
        # inp = input("Enter txt del : ")
        obj.deletRow(inp)
    elif inp == 'show':
        if obj.isLogin():
            txt = input("type : ")
            obj.showTask(currentUser,int(txt))



