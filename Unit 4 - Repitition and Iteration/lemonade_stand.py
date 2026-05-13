import random
from time import sleep
from os import system

WEATHERS = ["Sunny", "Cloudy", "Hot and Dry", "Thunderstorms"]

day = 1
cost = 0.02
sign_cost = 0.15
assets = 2
expenses = 0
profit = 0
zero_counter = 0
done_choosing = False

total_expenses = 0
total_glasses_made = 0
total_glasses_sold = 0



# ======================
#         Text
# ======================

def welcome():
    print("Welcome to Lemonsville!\n"
          "You are in charge of running a lemonade stand.\n")
    sleep(2)
    print("To manage your lemonade stand, you will need to make these decisions every day:\n"
          "1. How many glasses to make\n2. How many advertisements to make\n3. How much you want each glass to cost\n")
    sleep(2)
    print("\nYou will start with $2.00. Your cost to make lemonade is 2 cents.\n")
    sleep(2)
    print("Your expenses are the sum of the cost of the lemonade, and the cost of the signs.\n")
    sleep(2)
    print("How much you sell each day depends on the price you charge, and on the number of advertising signs you use, as well as the weather.\n")
    
    pause()

def pause():
    input("Press enter to continue: ")
    print()

# ======================
#         Game
# ======================

def choose_weather():
    weather = random.randint(0, 100)

    if weather <= 40:
        return WEATHERS[0], 2 # Returning the weather and a multiplier
    elif weather <= 80:
        return WEATHERS[1], 1
    elif weather <= 95:
        return WEATHERS[2], 3
    else:
        return WEATHERS[3], 0

def day_summary(glasses_made, glasses_sold, amt_customers, expense, profits):
    print(f"\n{"-"*60}\n"
          f"\nGlasses made: {glasses_made}\n"
          f"Glasses sold: {glasses_sold}\n"
          f"Number of potential customers: {amt_customers}"
          f"\nExpenses: {round(expense, 2)}\n"
          f"Profit: {round(profits, 2)}\n")
    print("-"*60 + "\n")
    pause()

def cost_summary(day_num, weather, money, glass_cost):
    print("-"*60)
    print(f"\nDay {day_num}")
    print(f"Today's weather is {weather}")
    print(f"Assets: ${round(money, 2)}")
    print(f"\nThe cost to make a glass of lemonade is: ${round(glass_cost, 2)}\n")
    print("-"*60)

# ======================
#         Main
# ======================

welcome()

while True:
    system("cls")

    todays_weather, multipler = choose_weather() # Multiplier used for # of customer
    assets_before = assets

    if todays_weather == WEATHERS[3]:
        print("Unfortunately, a thunderstorm hit Lemonsville earlier today, causing everything to be ruined!\n")
        assets -= 0.5
        pause()
    else:
        # Choosing values
        while not done_choosing:
            cost_summary(day, todays_weather, assets, cost)
            sleep(0.5)
            try:
                while True:
                    glass_made = int(input("\nHow many glasses would you like to make? "))
                    if assets - glass_made * cost < 0:
                        print("You don't have enough money")
                    else:
                        total_glasses_made += glass_made
                        assets -= glass_made * cost
                        break
                
                sleep(0.5)
                
                while True:
                    signs = int(input(f"How many signs would you like to make (${sign_cost} each)? "))
                    if assets - signs * 0.15 < 0:
                        print("You don't have enough money")
                    else:
                        assets -= signs * 0.15
                        break
                
                sleep(0.5)

                glass_price = int(input("How much do you want to sell each glass for (in cents)? ")) / 100

            except ValueError:
                sleep(0.5)
                print("Invalid input, try again from the beginning")
                assets = assets_before
                sleep(0.5)
                continue
            
            # Double checking to see if they want to change their inputs
            sleep(0.5)
            confirm = input("Do you want to change anything (type yes or press enter)? ").lower()
            if confirm == "yes":
                assets = assets_before
                continue
            else:
                done_choosing = True

        # Sales calculation
        expenses = round(glass_made * cost + signs * 0.15, 2)
        total_expenses += round(glass_made * cost + signs * 0.15, 2)
        
        multipler += signs / 6 # Including the amount of advertising signs purchased into customer amt
        
        # Determining # of customers including multi
        customers = int(random.randint(4, 8) * multipler - (glass_price))
        
        if glass_price >= 0.4 * multipler:
            customers = random.randint(0, 1)
            sleep(0.25)
            print("Your prices are way too high, think harder next time...\n")
        elif glass_price >= 0.15 * multipler:
            customers = int(random.randint(0, 5) * (multipler / 2))
            sleep(0.25)
            print("Your prices are a tad too high...\n")

        glass_sold = 0

        for i in range(customers):
            if i < glass_made:
                profit += glass_price
                glass_sold += 1
                total_glasses_sold += 1
        
        profit -= expenses
        assets += profit + expenses

        day_summary(glass_made, glass_sold, customers, expenses, profit)       
        
        # Resetting values
        profit = 0
        expenses = 0
        done_choosing = False

        day += 1
        
    # Price raising events
    event_chance = random.randint(1, 8)

    if event_chance == 1:
        options = ["Inflation", "Lemon Shortage", "Cardboard Shortage"]
        option = random.choice(options)

        if option == options[0]:
            sleep(0.5)
            print("Inflation has caused prices to skyrocket!\n")
            cost += 0.1
            pause()
        elif option == options[1]:
            sleep(0.5)
            print("Lemonsville has a lemon shortage! Lemons are now crazy expensive!\n")
            cost += 0.05
            pause()
        else:
            sleep(0.5)
            print("The local cardboard factory has been shut down! New cardboard factories are now charging more!\n")
            sign_cost += 0.1
            pause()           
    
    # Checking if assets are 0
    if assets <= 0:
        if zero_counter < 1:
            zero_counter += 1
            print("Manage your money better! Your lucky your mom gave you more money...\n")
            assets += 2
            pause()
        else:
            break

print("Your mom refuses to give you more money!\nManage your money better next time...\n")
pause()

print(f"GAME SUMMARY")
print("-"*60)
print(f"Assets: {assets}\n"
      f"Days: {day}\n"
      f"Total glasses sold: {total_glasses_sold}\n"
      f"Total glasses made: {total_glasses_made}\n"
      f"Total expenses: {total_expenses}\n")

