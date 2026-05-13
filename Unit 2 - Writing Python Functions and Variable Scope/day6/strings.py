str1 = "hello"
str2 = "alpha"
str3 = "bet"
str4 = "alphabet"

print(len(str1))
print(len(str4))

print(str4[3])
print(str4[-5])

def format_mark(mark, decimals):
    return f"{mark:.{decimals}f}"

print(format_mark(86.2644,2))