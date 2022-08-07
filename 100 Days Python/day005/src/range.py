# SYNTAX 
for number in range(a, b):
    print(number)

for number in range(1, 10):
    print(number)

#to skip the number 
for number in range(1, 11, 3):
    print(number)

#adding numbers using the range in loops
total = 0 
for number in range(1, 101):
    total += number
print(total)