def factorial (n):
     if n < 0:
          raise ValueError
     result=1
     for i in range(2,n+1):
          result*=i
     return result

n=int(input("Enter n :"))
print (factorial(n))
     
