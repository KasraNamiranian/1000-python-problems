while(1):
    sum = 0
    num = int(input("Enter a number: "))
    for i in range(1,num):
        if num % i ==0:
            sum+=i
    if sum == num:
        print("The number is perfect.")
    else:
        print("The number isn't perfect.")
    response = input("Do you want to continue the process?y/n: ")
    if response=="n" or response=="no":
        break
