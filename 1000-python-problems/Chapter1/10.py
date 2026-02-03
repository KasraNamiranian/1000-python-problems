# good question to become familiar with economy stuffs
print("Program that calculate insurance, tax and net pay of an employee from his/her salary.")
salary = float(input("Enter your salary: "))
insurance = salary * 0.07
tax = salary * 0.1
netPay = salary - insurance - tax
print("Employee net pay is:" , netPay)