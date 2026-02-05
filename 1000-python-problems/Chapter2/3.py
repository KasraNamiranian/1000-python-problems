#good question
#fibonacci
#O(N):
n = int(input("Enter the number you want to calculate: "))
f = [0] * n  #for defining a list with n zero elements.
if n == 1:
    f[0] = 1
    print(f[0])
elif n == 2:
    f[0] = 1
    f[1] = 1
    print(f[0] ,f[1])
else:
    f[0] = 1
    f[1] = 1
    for i in range(2,n):
        f[i]=f[i-1]+f[i-2]
    print(*f)   #for printing n values of lis in a row with space between them.