
import datetime
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
t6 = datetime.datetime.today() + datetime.timedelta(days=40)
print(t6)
print("--------------------")
f = "2021-11-24"
t5 = datetime.datetime.strptime("2021-11-25","%Y-%m-%d")
# t5.strptime("2021-11-25","%Y-%m-%d")
print(t5)


