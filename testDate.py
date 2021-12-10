
import datetime
from time import time
from dataType import *
# x = datetime.datetime(2021,12,1)
# print(x.strftime("%m"))
inp = [2021,11,21]
t1 = datetime.date(inp[0],inp[1],inp[2])
t2 = datetime.date(inp[0],inp[1],inp[2]+2)
print((t2-t1).days)
# t3 = datetime.date.weekday()
# print(t3)
str = '2021-11-19 21:39:59.527164'
t4 = datetime.date.today()
print(type(t4.weekday))
print("today:",t4.weekday())

# x = datetime.datetime(inp[0],inp[1],inp[2])
# print(x.year, x.month ,x.day+1)
# t5 = 
#----------------------------
# table = None
# table = [4,5,7]
# print(table)
# table = [2,5]
# print(table[0])
# print("-------")
# t5 = datetime.date.today()
# print((t5+datetime.timedelta(days=7)).day)
# print(t5.strftime("%A"))
#----------------------------f
# t6 = datetime.datetime.today() + datetime.timedelta(days=40)
# print(t6)
# print("--------------------")
# f = "2021-11-24"
# t5 = datetime.datetime.strptime("2021-11-25","%Y-%m-%d")
# # t5.strptime("2021-11-25","%Y-%m-%d")
# print(t5)
# print("--------------------")
# t7 = datetime.datetime(2021,11,26)
# print(t7)
# print("--------------------")
# print("2021-11-24 24.2".split("."))

#---------------------------------
def sortTaskDateTargerTime(li:list):
    for i in range(1,len(li)):
        key = li[i]
        j = i -1
        while j >= 0 and key.dateTarget.date() == li[j].dateTarget.date() and key.dateTarget.seconds > li[j].dateTarget.seconds:
            print("swap")
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key

def sortTaskDateTarget(li:list,near:int=1):
        """Insert list of Task object / near = 1 is going to sort nearest come first (near = 0 far come first)"""
        #This is insertion sort
        for i in range(1,len(li)):
            key = li[i]
            j = i -1
            if near == 1:
                while j >= 0 and (key.dateTarget.date() - datetime.date.today()).days < (li[j].dateTarget.date() - datetime.date.today()).days :
                    print("swap")
                    li[j+1] = li[j]
                    j -= 1
            elif near == 0:
                while j >= 0 and (key.dateTarget.date() - datetime.date.today()).days > (li[j].dateTarget.date() - datetime.date.today()).days :
                    print("swap")
                    li[j+1] = li[j]
                    j -= 1
            li[j+1] = key

def transposition(li:list,index:int):
    if index > 0:
        li[index],li[index-1] = li[index-1],li[index]
# t5 = datetime.datetime.today()
# print("----------------")
# print((t5 - t5.replace(hour=0, minute=0, second=0)))
# print((t5 - t5.replace(hour=0, minute=0, second=0)).total_seconds())
# print(t5)
# t6 = datetime.datetime.today() + datetime.timedelta(hours=4)
# print(t6)
# li = [datetime.datetime.today() + datetime.timedelta(hours=4),datetime.datetime.today() + datetime.timedelta(hours=2),
# datetime.datetime.today() + datetime.timedelta(hours=3)]
# print(li)
# sortTaskDateTarget(li)

# s = "1"
# print(bool(int(s)))
print("--------------------")
s = "Test\nLovely"
print(s)


print("--------------------")
li = [20,15,30,12,13,17]
target = 21
print(li)
for i in range(len(li)):
    if target > li[i]:
        print("Yeah :",i)
        transposition(li,i)
print(li)

