
from datetime import date
import dataType
from testCSV import *
currentUser = -1
inp = ''
while inp != "q":
    print("....User: {}".format(currentUser))
    inp = input("Enter mode : ")
    if inp == 're':
        txt = input("username password : ").split()
        registor(txt[0],txt[1])
    elif inp == 'login':
        txt = input("username password : ").split()
        currentUser = login(txt[0],txt[1])
    elif inp == 'add':
        if currentUser != -1:
            taskType = int(input("Type : "))
            if taskType == 0:
                dateInp = list(map(int,input("Date Month Year : ").split()))
                dateTarget = datetime.date(dateInp[2],dateInp[1],dateInp[0])
            elif taskType == 1:
                dateTarget = int(input("Enter day : "))
            elif taskType == 2:
                dateTarget = None
            
            txt = input("Detail : ")
            task(currentUser,dateTarget,taskType,txt)
    elif inp == 'del':
        inp = int(input("Enter row :"))
        # inp = input("Enter txt del : ")
        deletRow(inp)
    elif inp == 'show':
        if currentUser != -1:
            txt = input("type : ")
            showTask(currentUser,int(txt))



