import functools

school = []
day = 0

while day < 256:
    new_fish = []
    new_school = []
    for fish in school:
        if fish == 0:
            new_school.append(6)
            new_fish.append(8)
        else:
            new_school.append(fish-1)
    new_school.extend(new_fish)
    school = new_school
    day += 1

print(len(school))
