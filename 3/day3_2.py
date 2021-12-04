input = []
input1 = input
input2 = input


def process_greater(list, i=0):
    while len(list) > 1:
        count0 = [0] * 5
        count1 = 0
        for num in list:
            if num[i] == '0':
                count0 += 1
            else:
                count1 += 1

        greater = '1' if count1 >= count0 else '0'
        list = [x for x in list if x[i] == greater]
        i += 1
    return int(list[0], 2)


def process_lesser(list, i=0):
    while len(list) > 1:
        count0 = 0
        count1 = 0
        for num in list:
            if num[i] == '0':
                count0 += 1
            else:
                count1 += 1

        lesser = '1' if count1 < count0 else '0'
        list = [x for x in list if x[i] == lesser]
        i += 1
    return int(list[0], 2)


print(process_greater(input1)*process_lesser(input2))
