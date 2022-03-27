from audioop import add


print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra Cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else: 
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"You final bill is ${bill}")
