# good question
num = int(input("Enter a number: "))
n = int(input("nth bit to check: "))
nn = 1 << n
newnum = nn ^ num  # ^ is bitwise xor
print("before: ",num)
print("after: ",newnum)