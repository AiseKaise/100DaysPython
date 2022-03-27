from cgi import test
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

# Approach One
num_items = (len(names))

# Generate random numbers between 0 and last 
random_choice = random.randint(0, num_items - 1)
person_who_will_pay =  names[random_choice]


# Approach Two
person_who_will_pay = random.choice(names)

# Printing the output
print(person_who_will_pay + " is going to buy the meal today")