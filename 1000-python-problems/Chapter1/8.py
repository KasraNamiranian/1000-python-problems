# good question because you can also write 3*math.pow(10,-23) like this with e notation: 3.0e-23
import math
print("Program that calculate the molecules in n liter water.")
l = float(input("Enter the volume of your water in liter: "))
m = (l * 950) / (3 * math.pow(10,-23))   # you can also write 3.0e-23
print("molecules number is" , m)