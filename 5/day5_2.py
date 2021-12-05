input = [
]
map = []
for num in range(1000):
    map.append([0]*1000)
for row in input:
    [x1, y1, x2, y2] = row
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            map[y][x1] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            map[y1][x] += 1
    elif y2-y1 == x2-x1 and y2-y1 > 0:
        y = y1
        for x in range(x1, x2+1):
            map[y][x] += 1
            y += 1
    elif y1-y2 == x2-x1 and y1-y2 > 0:
        y = y1
        for x in range(x1, x2+1):
            map[y][x] += 1
            y -= 1
    elif y2-y1 == x1-x2 and y2-y1 > 0:
        x = x1
        for y in range(y1, y2+1):
            map[y][x] += 1
            x -= 1
    elif y1-y2 == x1-x2 and y1-y2 > 0:
        y = y2
        for x in range(x2, x1+1):
            map[y][x] += 1
            y += 1
total = 0
for row in map:
    for coord in row:
        if coord > 1:
            total += 1
print(total)
