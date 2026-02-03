year = int(input("Enter year: "))
day = 365.25 * year
print("Day is ",day)
month = day // 30
print("Month is ",month)
second = day * 24 * 60 * 60
print("Second is ",second)