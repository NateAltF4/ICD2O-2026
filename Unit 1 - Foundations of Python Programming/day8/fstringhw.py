import math;

#HW 1
print(f"{math.pi:.3f}")
price = 29.99
print(f"${price}\n")

#HW 2
tax_rate = 0.075
print(f"{tax_rate:.2%}")

discount = 0.25
print(f"{discount:.1%}\n")

#HW 3
city = "New York"
print(f"{city:<15}")
temp = 72.5
print(f"{temp:^10}\n")

#HW 4
item = "Product"
price = 25.99
quantity = 3
total = price * quantity

print(f"{"Item":<9}{"Price":<10}{"Quantity":>10}{"Total":>10}")
print(f"{item:<9}{price:<10}{quantity:>10}{total:>10}\n")

#HW 5
city = "City"
population = "Population"
area = "Area (sq km)"

print(f"{city:<10}{population:<15}{area:<10}")
print(f"{"New York":<10}{"8,398,748":<15}{"468.19":<10}")
print(f"{"LA":<10}{"3,990,456":<15}{"503.79":<10}")
print(f"{"Chicago":<10}{"2,693,976":<15}{"227.63":<10}")

