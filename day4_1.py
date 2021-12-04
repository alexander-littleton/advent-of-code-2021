calls = []

bingo = []
with open("day4_bingo.txt") as f:
    lines = f.readlines()
    card = [[], []]
    j = 0
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip('\n')
        if len(line):
            card[0].append(line.split(" "))
            card[0][j] = [int(x) for x in card[0][j] if x]
            j += 1
        else:
            for x in range(5):
                card[1].append([0]*5)
            bingo.append(card)
            card = [[], []]
            j = 0


def process_calls():
    for call in calls:
        for card in bingo:
            i = 0
            for row in card[0]:
                if call in row:
                    c = row.index(call)
                    card[1][i][c] = call
                    if all(card[1][i]):
                        return card, call, "row"
                    elif all([r[c] for r in card[1]]):
                        return card, call, "column"
                i += 1


[card, called], last_called, win_type = process_calls()
sum = 0
for row in card:
    for num in row:
        sum += num
for row in called:
    for num in row:
        sum -= num
print(sum*last_called)
