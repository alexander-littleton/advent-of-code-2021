crab_positions = []
positions_count = [0] * (max(crab_positions)+1)
for crab in crab_positions:
    positions_count[crab] += 1

amount_changed = []
for x in range(len(positions_count)):
    total_change = 0
    if x == 1935:
        print(x)
    for y in range(len(positions_count)):
        n = max(x, y) - min(x, y)
        total_change += n*(n+1)/2 * positions_count[y]
    amount_changed.append(total_change)

print(min(amount_changed))
