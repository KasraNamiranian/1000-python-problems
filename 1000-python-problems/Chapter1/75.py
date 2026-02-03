# good question
import datetime
n = int(input("Enter n: "))
x = datetime.datetime.now()
y = x + datetime.timedelta(0,n)
print("Current time is ",x.time())
print("New Time is ",y.time())