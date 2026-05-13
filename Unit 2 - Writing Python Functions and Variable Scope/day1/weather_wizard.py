# Prints the app title
# Parameters: none
# Returns: nothing
def show_app_title():
    print("🌦️ Weather Wizard – Your Forecast Friend")

# Converts Celsius to Fahrenheit
# Parameters: temp_c (float)
# Returns: Fahrenheit temperature (float)
def to_fahrenheit(temp_c):
    return temp_c * 9 / 5 + 32

# Calculates wind chill based on temp (°C) and wind speed (km/h)
# Parameters: temp (float), wind_speed (float)
# Returns: wind chill value (float)
def wind_chill(temp, wind_speed):
    return 13.12 + 0.6215 * temp - 11.37 * wind_speed**0.16 + 0.3965 * temp * wind_speed**0.16

# Prints weather summary
# Parameters: city (string), temp (float)
# Returns: nothing
def report(city, temp):
    print("The temperature in " + city + " is " + str(temp) + "°C.")




# 1. Call show_app_title().
show_app_title()
# 2. Store "Toronto" in city.
city = "Toronto"
# 3. Store -5 in celsius_temp.
celsius_temp = -5
# 4. Call report(city, celsius_temp).
report(city, celsius_temp)
# 5. Convert temp to Fahrenheit and print it.
print(f"Temperature in F is {to_fahrenheit(celsius_temp)}")
# 6. Store 30 in wind_speed.
wind_speed = 30
# 7. Call wind_chill(celsius_temp, wind_speed) and store result.
windChill = wind_chill(celsius_temp, wind_speed)
# 8. Print the calculated wind chill.
print(f"Wind chill will be {windChill}")
