# good question
x = int(input("Enter x: "))
y = int(input("Enter y: "))
x , y = y , x
print("X = ",x)
print("y = ",y)

"""book answer is cool but a bit oldschool,
because in newer python version we have the above syntax and we don't need to do it like the book."""
"""
Book Solution:
x = int(input("Enter x: "))
y = int(input("Enter y: "))
x = x + y
y = x - y
x = x - y
print("X" ,x , "Y" ,y)
"""
