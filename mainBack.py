
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
            txt = input("type | string : ").split()
            task(currentUser,int(txt[0]),txt[1])
    elif inp == 'show':
        if currentUser != -1:
            txt = input("type : ")
            showTask(currentUser,int(txt))



