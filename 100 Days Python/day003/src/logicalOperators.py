# In "and" operator if ONE is false the whole is false
# in "or" operator if ONE is true the whole is true 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cms? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride")
    else:
        bill = 14
        print("Adult tickets are $14")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill is $ {bill}")

else:
    print("Sorry, your pp isn't grown up to ride the rollercoaster")