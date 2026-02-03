# good question
num = int(input("Enter a number: "))
n = int(input("nth bit to check: "))
checking = (num >> n) & 1
print("The ",n,"bit is ",checking)