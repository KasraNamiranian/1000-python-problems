# good question
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("num1: ",num1,"\n","num2: ",num2)
num1 ^= num2
num2 ^= num1
num1 ^= num2
print("num1 after swapping: ",num1)
print("num2 aftert swapping: ",num2)