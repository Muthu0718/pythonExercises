cart = [
    ("apple", 1.5, 4),   # 4 apples at $1.5 each
    ("banana", 0.8, 6),  # 6 bananas at $0.8 each
    ("milk", 2.3, 2)     # 2 milks at $2.3 each
]
print("Receipt")
total_price=0
for item,price,quantity in cart:
    item_total=price*quantity 
    print(f"{item} : {price} x {quantity} = {item_total}")
    total_price+=item_total
print(f"Total_price = {total_price}")