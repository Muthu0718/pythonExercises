students = [
    ("Alice", 95),
    ("Bob", 85),
    ("Charlie", 70),
    ("David", 50),
    ("Eva", 60)
]

for name,marks in students:
    if marks >=90:
        grade="A"
        print(f"{name} got {grade} Grade")
    elif 80 <= marks <=89:
        grade="B"
        print(f"{name} got {grade} Grade")
    elif 70 <= marks <=79:
        grade="C"
        print(f"{name} got {grade} Grade")
    elif 60 <= marks <=69:
        grade="D"
        print(f"{name} got {grade} Grade")
    elif marks<60:
        grade="F"
        print(f"{name} got {grade} Grade")

    


