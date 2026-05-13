# 1) Temperature classifier (°C):
#    Print one of: cold (<0), cool (0–15), warm (16–25), hot (>25) based on temp_c.
temp_c = 15
if temp_c < 0:
    print("cold")
elif temp_c < 15:
    print("cool")
elif temp_c < 25:
    print("warm")
else:
    print("hot")


# 2) Letter grades:
#    Print A (90+), B (80–89), C (70–79), D (60–69), or F (<60) based on percent.

# 3) Password strength by length:
#    Print weak (<8), ok (8–11), or strong (12+) using len(password).

# 4) Greeting by hour (0–23):
#    Print Good morning (5–11), Good afternoon (12–16), Good evening (17–21), or Good night (other).

# 5) Course code (strings):
#    If it begins with "ics" (case-insensitive) print "Computer Studies".
#    Elif it ends with "py" print "Python file".
#    Else print "Unknown".
#    (Use only lower(), len(), and slicing.)

def course_code(str):
    if len(str) < 2:
        print("unknown")
    elif str.lower()[:3]=="ics":
        print("computer studies")
    elif str.lower()[-2:]=="py":
        print("python file")
    else:
        print("unknown")

# 6) Ticket price category by age:
#    Print child (0–12), student (13–17), adult (18–64), or senior (65+).

def ticket_price(age):
    if age <= 12:
        print("child")
    elif 17 >= age >= 13:
        print("student")
    elif 64 >= age >= 18:
        print("adult")
    else:
        print("senior")

# 7) Shipping fee by weight (kg):
#    Print light (<=1.0), standard (<=5.0), or heavy (>5.0).

def shipping_fee(kg):
    if kg <= 1:
        print("light")
    elif kg <= 5:
        print("standard")
    else:
        print("heavy")


# 8) Honour roll:
#    If gpa >= 3.7 and attendance >= 95, print "Honour Roll".
#    Elif gpa >= 3.0, print "Good Standing".
#    Else print "Keep Going".

def honour_roll(gpa, attendance):
    if (gpa >= 3.7 and attendance >= 95):
        print("honour roll")
    elif (gpa >= 3.0):
        print("good standing")
    else:
        print("keep going")

# 9) File type by extension (strings):
#    If filename ends with ".py" -> print "Python".
#    Elif it ends with ".txt" -> print "Text".
#    Else -> "Other".
#    (Use only lower() and slicing.)

def file_type(filename):
    if filename.lower()[-3:] == ".py":
        print("Python")
    elif filename.lower()[-4:] == ".txt":
        print("Text")
    else:
        print("other")

# 10) Team placement (ints/floats):
#    If age < 13 -> "U13".
#    Elif 13–14 and height_m >= 1.65 -> "U15-Tall".
#    Elif 13–14 and height_m < 1.65 -> "U15".
#    Else -> "U17+".

def team_placement(age, height):
    if 14 >= age >= 13 and height >= 1.65:
        print("U15 tall")
    elif 14 >= age >= 13 and height < 1.65:
        print("U15")
    elif age < 13:
        print("U13")
    else:
        print("U17+")

# Challenge (optional):
#    Rewrite #8 using a nested if inside the gpa >= 3.7 branch (check attendance inside).

