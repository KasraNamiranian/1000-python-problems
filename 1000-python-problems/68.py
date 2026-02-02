# good question
num = int(input("Enter a number: "))
n = int(input("nth bit to check: "))
m = ~(1 << n)
newnum = num & m
print("before: ",num)
print("after: ",newnum)