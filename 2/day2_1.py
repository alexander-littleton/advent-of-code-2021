input=[]
depth=0
pos=0
for x in input:
    move, distance = x.split(" ")
    distance = int(distance)
    if move == "down":
        depth += distance
    elif move == "up":
        depth -= distance
    elif move == "forward":
        pos += distance
print(depth * pos)