programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving Item from dictionary
print(programming_dictionary["Bug"])

# Adding new item to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Creating an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit and item in a dictionary
programming_dictionary["Bug"] = "smtg smtg"

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary["Bug"])