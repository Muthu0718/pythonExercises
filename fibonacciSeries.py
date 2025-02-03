n=int(input("Enter n:" ))
num1=0
num2=1
count=0
while count < n:
    print(num1,end=" ")
    num1,num2 = num2,num1+num2
    count+=1
print ()
