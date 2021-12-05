input = [
]
map = []
for num in range(1000):
    map.append([0]*1000)
for row in input:
    [x1, y1, x2, y2] = row
    if x1 == x2:
        for coord in range(min(y1, y2), max(y1, y2)+1):
            map[coord][x1] += 1
    elif y1 == y2:
        for coord in range(min(x1, x2), max(x1, x2)+1):
            map[y1][coord] += 1
total = 0
for row in map:
    for coord in row:
        if coord > 1:
            total += 1
print(total)
