n = int(input("Enter a value:"))
count = 0             
if n==1:
    print(n, " is a prime number")  
else: 
    for i in range(1,n+1): 
        if( n%i== 0):       
            count+=1     
if count == 2 :      
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")