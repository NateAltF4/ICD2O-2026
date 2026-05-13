print ("Upper School Resource Density Calculator")
print ("----------------------------------------")

# Input
classrooms = int(input("How many classrooms are in the Upper School? ")) # Getting the # of classrooms
fountains = int(input("How many student water fountains? ")) # Getting the # of fountains
bathroom = int(input("How many student restrooms? ")) # Getting the # of bathrooms
extraItem = input("Enter ONE additional resource to track (e.g., vending machines): ") # Getting what extra item the user wants
item = int(input(f"How many {extraItem} are there? ")) # Getting the # of item

condFount = input("Condition of fountains: ") # Getting fountain condition
condBath = input("Condition of restrooms: ") # Getting bathroom condition
condItem = input(f"Condition of {extraItem}: ") # Getting the extra item condition

# Output
fountPerClass = round(fountains / classrooms, 2) # Getting fountain density and round
itemPerClass = round(item / classrooms, 2) # Getting item density and round
bathroomPerClass = round(bathroom / classrooms, 2) # Getting bathroom density and round

# Print
print("\nResults")
print("-------")
print(f"Fountains per classroom: {fountPerClass} (Condition: {condFount})") # Outputting the fountain density and its condition
print(f"Restrooms per classroom: {bathroomPerClass} (Condition: {condBath})") # Outputting the bathroom density and its condition
print(f"{extraItem.title()} per classroom: {itemPerClass} (Condition: {condItem})") # Outputting the items density and its condition
print("\nThanks for helping map our Upper School resources!")

# Reflection questions
# 1. It shows how many resources we have in our school, and allows others to use our program if it changed
# 2. I would add a feature which allows you to change what variables you want to track, allowing you to further customize your results for each user