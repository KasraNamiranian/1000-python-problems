from math import tan , pi
print("This program calculate the area of your polygon.")
n = int(input("How many sides has your polygon? "))
length = int(input("Enter the side length of your polygon: "))
area = (n * (length ** 2)) / (4 * tan(pi/n))
print("The area of your polygon is:", area)