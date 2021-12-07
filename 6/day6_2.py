school = []
passing_days = 256
total = len(school)

birthdays = [0] * 256
for day in range(passing_days):
    birthdays[day] = 0

for fish in school:
    day = fish
    while day < passing_days:
        birthdays[day] += 1
        day += 7

for day in range(passing_days):
    babies = birthdays[day]
    day_iter = day + 9
    while day_iter < passing_days:
        birthdays[day_iter] += babies
        day_iter += 7
    total += babies
print(total)
