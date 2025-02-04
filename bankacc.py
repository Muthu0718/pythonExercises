operations = [
    ("deposit", 500),
    ("withdraw", 200),
    ("checkbalance",0),
    ("withdraw", 1200),  
    ("deposit", 300)
]
balance=1000
for operation,amount in operations:
    if operation=="deposit":
        balance+=amount
        print(f"Deposited :${amount}.Available balance : ${balance}")
    elif operation=="withdraw":
        if balance<amount:
            print(f"Insufficient balance. Current balance :${balance}")
        else:
            balance-=amount
            print(f"Withdrew :${amount}.Available balance : ${balance}")
    elif operation=="checkbalance":
        print(f"Current balance : ${balance}")
 

