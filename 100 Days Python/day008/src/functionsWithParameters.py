# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello World")
  print("YOLO")
  print("lol xd")

greet()

# Function that allows input 

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How you doing {name}?")

# greet_with_name("Angela")

# Functions with more than one input 

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"Ur location is {location}")

# greet_with("Angela", "London")

greet_with(name="angela", location="london")
