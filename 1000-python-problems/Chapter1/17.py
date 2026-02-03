# good question
amount = int(input("Please enter amount: "))
rate = float(input("Please enter rate: "))
years = int(input("Please enter years: "))
future_value = amount*((1+(0.01*rate))**years)
print("Future_value is %12.0f" %(future_value))