# Displays the header for the stat tracker
# Parameters: none
# Returns: nothing
def show_tracker_header():
    print("Baseball Performance Tracker")
# Calculates batting average
# Parameters: hits (int), at_bats (int)
# Returns: batting average (float)
def get_batting_average(hits, at_bats):
    return hits / at_bats
# Prints a summary of a player's game stats
# Parameters: name (string), hits (int), at_bats (int)
# Returns: nothing
def print_game_summary(name, hits, at_bats):
    print(name + " had " + str(hits) + " hits in " + str(at_bats) + " at-bats.")
# Returns total bases and slugging percentage
# Parameters: singles (int), doubles (int), triples (int), home_runs (int), at_bats (int)
# Returns: (total bases (int), slugging (float))
def get_power_stats(singles, doubles, triples, home_runs, at_bats):
    total_bases = singles + 2 * doubles + 3 * triples + 4 * home_runs
    slugging = total_bases / at_bats
    return total_bases, slugging
# Converts a speed from miles per hour to kilometers per hour
# Parameters: mph (float)
# Returns: speed in kph (float)
def mph_to_kph(mph):
    return mph * 1.60934
# Prints a player's pitch velocity and location
# Parameters: speed (float), location (string)
# Returns: nothing
def log_pitch(speed, location):
    print("Pitch thrown at " + str(speed) + " mph to " + location + ".")
# Returns the ERA (earned run average) for a pitcher
# Parameters: earned_runs (int), innings_pitched (float)
# Returns: ERA (float)
def calculate_era(earned_runs, innings_pitched):
    return (earned_runs * 9) / innings_pitched
# Returns the strikeout-to-walk ratio
# Parameters: strikeouts (int), walks (int)
# Returns: ratio (float)
def get_kbb_ratio(strikeouts, walks):
    return strikeouts / walks
# Returns player name and position in a formatted string
# Parameters: name (string), position (string)
# Returns: summary string (string)
def format_player_info(name, position):
    return name + " plays " + position
# Displays a closing message
# Parameters: none
# Returns: nothing
def end_tracker():
    print("End of performance report.")

# Tasks
# 1. Call show_tracker_header().
show_tracker_header()
# 2. Call get_batting_average() using 3 hits and 5 at-bats. Store the result in avg and print it.
avg = get_batting_average(3, 5)
print(avg)
# 3. Call print_game_summary() for player 'Jaylen' with 2 hits and 4 at-bats.
print_game_summary("Jaylen", 2, 4)
# 4. Call get_power_stats() using: 1 single, 1 double, 0 triples, 1 home run, 4 at-bats. Store total bases and slugging.
get_power_stats(1, 1, 0, 1, 4)
# 5. Call mph_to_kph() with 92.5 mph and store result in kph. Print it.
kph = mph_to_kph(92.5)
print(kph)
# 6. Call log_pitch() with speed 89.6 and location 'outside corner'.
log_pitch(89.6, "outside corner")
# 7. Call calculate_era() with 2 earned runs over 6.2 innings. Store and print ERA.
era = calculate_era(2, 6.2)
print(era)
# 8. Call get_kbb_ratio() with 9 strikeouts and 3 walks. Store and print the ratio.
kbb = get_kbb_ratio(9, 3)
print(kbb)
# 9. Call format_player_info() with 'Liam' and 'shortstop'. Store and print the result.
liam = format_player_info("Liam", "shortstop")
print(liam)
# 10. Call end_tracker().
end_tracker()