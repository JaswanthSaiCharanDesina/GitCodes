n = int(input("Enter a number: "))
sum = 0
i=1
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if sum == n:
    print("Perfect")
else:
    print("Not perfect")
