lastYear = float(input("Please enter last year price: "))
thisYear = float(input("Please enter this year price: "))
inflation = (thisYear - lastYear) / lastYear
nextYear = lastYear + thisYear * inflation
print("Inflation rate: %",inflation,"\t","Next year price: ",nextYear)
