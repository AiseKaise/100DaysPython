print("Welcome to the rollercoaster!")
height = int(input("What is your height in cms? "))

if height > 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))

    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $14")
        
else:
    print("Sorry, your pp isn't grown up to ride the rollercoaster")