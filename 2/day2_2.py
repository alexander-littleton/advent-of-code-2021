input=[]
depth=0
pos=0
aim=0
for x in input:
    move, distance = x.split(" ")
    distance = int(distance)
    if move == "down":
        aim += distance
    elif move == "up":
        aim -= distance
    elif move == "forward":
        pos += distance
        if aim > 0:
            depth+= distance * aim
        if aim < 0:
            depth-= distance * aim
print(depth * pos)