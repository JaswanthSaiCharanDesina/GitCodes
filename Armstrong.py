n = int(input("Enter a number: "))
temp = n
rem=0
num=0
while temp>0:
    rem = temp%10
    num += rem ** 3
    temp = temp//10
if num == n:
    print(n," is Amstrong number")
    
else :
    print(n," is Not Armstrong number")