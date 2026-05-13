N = int(input())
name = input()
bid = int(input())

for i in range(N - 1):
    name2 = input()
    bid2 = int(input())

    if bid2 > bid:
        bid = bid2
        name = name2

print(name)