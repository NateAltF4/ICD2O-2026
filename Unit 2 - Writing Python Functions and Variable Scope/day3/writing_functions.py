import math

def printMessage():
    print("Welectome")

def subtract(x, y):
    return x - y

# print(subtract(5,2))
# printMessage()

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))

# print(subtract(x, y))

def greet(name):
    return f"Hello, {name}"

def cube(num):
    return num**3

def area_rectangle(x, y):
    return x*y

def format_pi(decimals):
    return f"Pi is {math.pi:.{decimals}f}"

def seconds(hours):
    return hours*3600

#-------------------------------------------------------------------

def total_with_tax(price, tax_rate):
    price += price*tax_rate
    return round(price,2)

def bmi(weight, height):
    return f"{weight/height**2:.2f}"

def greeting_with_age(name, age):
    return f"Hi {name}, you are {age} years old"

def pay(hours, rate):
    return f"Pay: ${hours * rate:.2f}"

def format_score(score, decimals):
    f"Score: {score:.{decimals}f}"

#----------------------------------------------------------

def format_circle(radius, decimals):
    return f"{math.pi*radius**2:.{decimals}f}"

def velocity(distance, time, decimals):
    speed = distance/time
    return f"Speed: {speed:.2f} m/s"

def format_total_price(price, quantity, tax, decimals):
    return f"Total: {(price*quantity)+(price*quantity*tax):.{decimals}f}"

def temperature_report(celsius, decimals):
    return f"Temp is: {celsius*(9/5)+32:.{decimals}f}"

def travel_summary(distance, hours, decimals):
    print(f"You travelled {distance}km in {hours} hours. Avg speed of {distance/hours:.{decimals}f}")
    

print(greet("Steve"))
print(cube(2))
print(area_rectangle(5, 2))
print(format_pi(3))
print(seconds(1))

print(total_with_tax(67.67, 0.13))
print(bmi(100, 1.7))
print(greeting_with_age("Gordon", 9))
print(pay(8, 17.6))
print(format_score(87.456789, 3))