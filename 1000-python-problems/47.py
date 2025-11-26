# good question
M_PER_MILE = 1609.35
M_PER_FOOT = 0.30480
miles = int(input("Please enter the number of miles: "))
feet = int(input("Please enter the number of feet: "))
total_meters = miles * M_PER_MILE + feet * M_PER_FOOT
total_kilometers = total_meters / 1000
kilometers = int(total_kilometers)
meters = (total_kilometers - kilometers) * 1000
print("The distance is ",kilometers,", kilometers, ",meters," meters.")