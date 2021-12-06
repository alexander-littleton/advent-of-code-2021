import functools

school = []
passing_days = 256
total = len(school)

birth_map = {}
for day in range(passing_days):
    birth_map[day] = 0

for fish in school:
    day = fish
    while day < passing_days:
        birth_map[day] += 1
        day += 7

for day in range(passing_days):
    babies = birth_map[day]
    day_iter = day + 9
    while day_iter < passing_days:
        birth_map[day_iter] += babies
        day_iter += 7
    total += babies
print(total)
