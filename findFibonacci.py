def fibonacci(n,memo={0:0,1:1}):
    if n<0:
        raise ValueError
    if n not in memo:
        memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo)
    return memo[n]

n=int(input("Enter n:"))
print(fibonacci(n))
