print("Enter the length of one wall (in meters)")
wallLength = (float)(input())

print("Enter the width of one wall (in meters)")
wallWidth = (float)(input())

print("Enter the height of the house (in meters)")
houseHeight = (float)(input())

print("Enter the cost per brick (in dollars)")
brickCost = (float)(input())

print("Enter the dimensions of standard brick (length width height, split by space, in meters)")
brick_length, brick_width, brick_height = input().split()

saWall = wallLength * houseHeight
saBrick = (float)(brick_length) * (float)(brick_height)

brickNeed = saWall / saBrick
totalBrickCost = brickCost * brickNeed

print(f"House Details:\nWall surface area: {saWall}\nBricks needed: {brickNeed}\nBrick cost: {totalBrickCost}")