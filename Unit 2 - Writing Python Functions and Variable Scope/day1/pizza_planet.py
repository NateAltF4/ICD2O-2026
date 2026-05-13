# Prints a welcome message
# Parameters: none
# Returns: nothing
def greet_customer():
    print("Welcome to Pizza Planet! 🍕🚀")

# Calculates total price of a pizza
# Parameters: base_price (float), extra_toppings (int)
# Returns: total price (float)
def get_total(base_price, extra_toppings):
    return base_price + (extra_toppings * 1.25)

# Prints a thank-you message
# Parameters: name (string)
# Returns: nothing
def thank_you(name):
    print("Thanks for ordering, " + name + "! Enjoy your pizza.")

# Returns number of slices based on pizza size
# Parameters: size (string)
# Returns: number of slices (int)
def slices_for_size(size):
    if size == "small":
        return 6
    elif size == "medium":
        return 8
    elif size == "large":
        return 10
    else:
        return 0




# 1. Call greet_customer().
greet_customer()
# 2. Set customer to your name.
customer = "Nathan"
# 3. Set size to "medium".
size = "medium"
# 4. Set price by calling get_total(10.00, 2).
get_total(10.00, 2)
# 5. Call thank_you(customer).
thank_you(customer)
# 6. Use slices_for_size(size) and store in slice_count.
slice_count = slices_for_size(size)
# 7. Print how many slices the customer will receive.
print(f"{customer} will get {slice_count} slices")

