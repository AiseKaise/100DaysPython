################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# local scope
def drink_water():
  drink_portion = 2 
  print(drink_portion)

drink_water()

# Global scope
player_health = 10

def drink_portion():
  portion_strength = 2
  print(player_health) #<------

drink_portion()

# There is no Block Scope here
game_level = 3
enemies = ["skeleton", "zombies", "aliens"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy)

# Modifying Global Scope
# V.Bad Idea to call ur local variable and global variable with same names mf

enemies = 0
def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constant

PI = 3.14159
URL = "www.google.com"
TWITTER_HANDLE = "@yu_angela"



