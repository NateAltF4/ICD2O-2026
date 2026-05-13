inventory = []

# Rolls a 20-sided die and returns the result
def roll_d20():
    import random
    return random.randint(1, 20)

# Calculates attack damage
# Accepts base damage (int) and bonus (int)
# Returns total damage (int)
def calculate_damage(base, bonus):
    return base + bonus

# Calculates health after damage taken
# Accepts current health and damage
# Returns new health (int)
def take_damage(health, damage):
    return health - damage

# Heals the character
# Accepts current health and heal amount
# Returns new health and a string status
def heal(health, amount):
    new_health = health + amount
    return new_health, "You feel stronger!"

# Adds an item to inventory
# Accepts the inventory list and item (str)
# Modifies the inventory directly
def add_item(inventory, item):
    inventory.append(item)

# Displays all items in inventory
# Accepts inventory list
# Returns nothing
def display_inventory(inventory):
    print("Inventory contains:")
    for item in inventory:
        print("- " + item)

# Determines if attack was a critical hit
# Accepts a d20 roll (int)
# Returns True or False
def is_critical_hit(roll):
    return roll == 20

# Returns character's status
# Accepts name (str), health (int), inventory (list)
# Returns a formatted string with player status
def get_status(name, health, inventory):
    return f"{name} has {health} HP and carries: {', '.join(inventory)}"

# Calculates experience needed for next level
# Accepts current level (int)
# Returns required experience (int)
def exp_to_next_level(level):
    return level * 1000

# Combines weapon stats
# Accepts weapon name (str), base damage (int), and magic bonus (int)
# Returns a string summary and total damage (int)
def weapon_summary(name, base, bonus):
    return f"{name} does {base}+{bonus} damage", base + bonus


# Tasks
# 1.	Roll a d20 for initiative and print the result.
print(roll_d20())
# 2.	Calculate the total damage dealt when a player does 6 base damage and has a +2 bonus.
print(calculate_damage(6, 2))
# 3.	Take 12 damage from a monster. Update your health from 30.
print(take_damage(30, 12))
# 4.	Heal for 10 points from a potion. You currently have 18 health.
heal(18, 10)
# 5.	Add a "Magic Wand" and "Healing Potion" to your inventory list.
add_item(inventory, "Magic Wand")
add_item(inventory, "Healing Potion")
# 6.	Display your current inventory.
display_inventory(inventory)
# 7.	Check if your attack roll of 20 is a critical hit.
print(is_critical_hit(20))
# 8.	Print your character’s status using the name "Elaria", 25 health, and your current inventory.
get_status("Elaria", 25, inventory)
# 9.	Find out how much experience is needed to reach level 5.
print(exp_to_next_level(5))
# 10.	Create a summary for a "Flaming Sword" that does 8 base damage with a +3 magic bonus.
print(weapon_summary("Flaming Sword", 8, 3))