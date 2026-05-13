p = int(input())
over40 = 0

for i in range(p):
    playerpoints = int(input())
    playerfouls = int(input())
    
    if playerpoints * 5 - playerfouls * 3 > 40:
        over40 += 1

if over40 == p:
    print(f"{over40}+")
else :
    print(over40)