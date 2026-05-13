observations = {
    1: {
        "time": "2:38",
        "cars": 107,
        "pedestrians": 7,
        "bikes": 1,
        "intersection_type": "Traffic light",
        "infractions": "None",
        "notes": "Sunny/busy"
    },
    2: {
        "time": "2:40",
        "cars": 73,
        "pedestrians": 7,
        "bikes": 0,
        "intersection_type": "Traffic light",
        "infractions": "None",
        "notes": "Sunny"
    },
    3: {
        "time": "2:42",
        "cars": 97,
        "pedestrians": 11,
        "bikes": 1,
        "intersection_type": "Traffic light",
        "infractions": "Speeding",
        "notes": "Sunny"
    },
    4: {
        "time": "2:44",
        "cars": 71,
        "pedestrians": 5,
        "bikes": 1,
        "intersection_type": "Traffic light",
        "infractions": "No turn signal",
        "notes": "Sunny"
    },
    5: {
        "time": "2:46",
        "cars": 53,
        "pedestrians": 9,
        "bikes": 0,
        "intersection_type": "Traffic light",
        "infractions": "None",
        "notes": "Sunny"
    },
    6: {
        "time": "2:48",
        "cars": 69,
        "pedestrians": 4,
        "bikes": 2,
        "intersection_type": "Traffic light",
        "infractions": "None",
        "notes": "Sunny"
    },
    7: {
        "time": "2:50",
        "cars": 89,
        "pedestrians": 7,
        "bikes": 0,
        "intersection_type": "Traffic light",
        "infractions": "No turn signal",
        "notes": "Sunny"
    }
}


# ===============================
#   ACCESSING A SINGLE OBSERVATION
# ===============================

def get_observation(observations, number):
    # Returns the observation dictionary for a specific observation number.
    # For example: get_observation(observations, 1) returns the first observation.
    # Returns: dict (e.g. {'time': '10:05', 'cars': 14, ...})
    return observations[number]


# ===============================
#   ACCESSING INDIVIDUAL DATA POINTS
# ===============================

def get_observation_time(obs):
    # Returns the time string from a single observation.
    # Returns: str
    return obs["time"]

def get_observation_cars(obs):
    # Returns the number of cars counted during one observation.
    # Returns: int
    return obs["cars"]

def get_observation_pedestrians(obs):
    # Returns the number of pedestrians counted during one observation.
    # Returns: int
    return obs["pedestrians"]

def get_observation_bikes(obs):
    # Returns the number of bikes counted during one observation.
    # Returns: int
    return obs["bikes"]

def get_observation_type(obs):
    # Returns the type of intersection (e.g. '4-way stop', 'Traffic light').
    # Returns: str
    return obs["intersection_type"]

def get_observation_notes(obs):
    # Returns the notes recorded for a single observation.
    # Returns: str
    return obs["notes"]


# ===============================
#   AGGREGATION FUNCTIONS (WORK FOR ANY SIZE DICTIONARY)
# ===============================

def get_num_observations(observations):
    # Returns the total number of observations recorded.
    # Returns: int
    return len(observations)

def get_total_cars(observations):
    # Calculates the total number of cars across all observations.
    # Returns: int
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_cars(obs)
    return total

def get_total_pedestrians(observations):
    # Calculates the total number of pedestrians across all observations.
    # Returns: int
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_pedestrians(obs)
    return total

def get_average_bikes(observations):
    # Calculates the average number of bikes per observation.
    # Returns: float
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_bikes(obs)
    return total / get_num_observations(observations)


# ===============================
#   FORMATTING & PRINTING HELPERS
# ===============================

def format_observation_row(obs_num):
    # Formats a single row of observation data for display in a table.
    # Returns: str (a nicely formatted line of data)
    obslist = get_observation(observations, obs_num)
    return f"{obs_num:<6}|{get_observation_time(obslist):^6}|{get_observation_cars(obslist):^6}|{get_observation_pedestrians(obslist):^6}|{get_observation_bikes(obslist):^7}|{get_observation_type(obslist):^15}| {get_observation_notes(obslist):<6}"

def print_table_header():
    # Prints the header section for the table of observations.
    # Returns: None
    print("INTERSECTION OBSERVATIONS") 
    print("-"*60)
    print(f"{"Obs #":<6}|{"Time":^6}|{"Cars":^6}|{"Peds":^6}|{"Bikes":^7}|{"Type":^15}|{"Notes":>6}")
    print("-"*60)

def print_totals():
    # Prints the total cars, total pedestrians, and average bikes
    # after all observations are displayed.
    # Returns: None
    total_cars = get_total_cars(observations)
    total_peds = get_total_pedestrians(observations)
    avg_bikes = round(get_average_bikes(observations),3)

    print(f"TOTAL CARS: {total_cars}\nTOTAL PEDESTRIANS: {total_peds}\nAVERAGE BIKES: {avg_bikes}")

def print_divider():
    print("-"*60)

print_table_header()

for i in observations:
    print(format_observation_row(i))

print_divider()

print_totals()
