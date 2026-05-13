print("Enter your drink cost: ")
drinkCost = input()
cost1 = (float)(drinkCost.replace("$", ""))

print("Enter your appetizer cost: ")
appetizer = input()
cost2 = (float)(appetizer.replace("$", ""))

print("Enter your entree cost: ")
entree = input()
cost3 = (float)(entree.replace("$", ""))

print("Enter your dessert cost: ")
dessert = input()
cost4 = (float)(dessert.replace("$", ""))

print("Enter your tip percentage: ")
tipPercent = (float)(input().replace("%", ""))

subTotal = cost1 + cost2 + cost3 + cost4
tip = subTotal * (tipPercent/100)
tax = subTotal * 0.13
total = subTotal + tip + tax

print(f"Bill summary:\nSubtotal: ${subTotal}\nTip: ${tip}\nTax: ${tax}\nTotal: ${total}")