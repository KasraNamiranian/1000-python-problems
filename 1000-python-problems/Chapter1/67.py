# good question
num = int(input("Enter a number: "))
n = int(input("nth bit: "))
newnum =  (1 << n) | num
print("before: ",num)
print("after: ",newnum)