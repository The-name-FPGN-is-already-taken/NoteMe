
from datetime import date
import dataType
from notaBack import *

#sim for testing not implement


nota = Nota()
nota.login("catty","5")
# text = "บรรดทัด\nบรรทัด"
# nota.addTimetable(datetime.time(12,16,10),1,"ให้อาหารแมวด้วยหมา","",[0,3,4])
li = nota.getTimetableAll(0)
for i in li:
    print(i)
# nota.deletRow(li[0].taskID)
# print(nota.getDayFromTimetableID(li[1].taskID))
# li[0].topic = "เปลี่ยนวันอีกรอบ งดงามมาก"
# nota.editTimetable(li[0],[0,1,3,4])
# nota.markCompleteTimetable(li[1])
nota.resetCompleteTimetable()

# s = "บรรดทัด\nบรรทัด"
# print(s)












# inp = ''
# table = None
# while inp != "q":
#     print("....User: {}".format(obj.userID))
#     inp = input("Enter mode : ")
#     if inp == 're':
#         txt = input("username password : ").split()
#         obj.registor(txt[0],txt[1])
#     elif inp == 'login':
#         txt = input("username password : ").split()
#         obj.login(txt[0],txt[1])
        
            
#     elif inp == 'add':
#         if obj.isLogin():
#             taskType = int(input("Type : "))
#             if taskType == 0:
#                 dateInp = list(map(int,input("Date Month Year : ").split()))
#                 dateTarget = datetime.datetime(dateInp[2],dateInp[1],dateInp[0])
#             elif taskType == 1:
#                 dateTarget = int(input("Enter day : "))
#             elif taskType == 2:
#                 dateTarget = -1
            
#             txt = input("Detail : ")
#             des = input("Descrpition : ")
#             if Nota.checkStrForAdd(txt) and Nota.checkStrForAdd(des):
#                 obj.addRecord(dateTarget,taskType,txt,des)
#     elif inp == 'del':
#         #Must input taskID
#         inp = int(input("Enter row :"))
#         # inp = input("Enter txt del : ")
#         obj.deletRow(inp)
#     elif inp == 'show':
#         if obj.isLogin():
#             print(obj.getTaskToday())
#     elif inp == 'logout':
#         obj.logout()





