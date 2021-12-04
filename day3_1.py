input = []
count0 = [0] * len(input[0])
count1 = [0] * len(input[0])
for num in input:
    for i in range(len(num)):
        if num[i] == '0':
            count0[i]+=1
        else:
            count1[i]+=1

output = []
for i in range(len(count0)):
    if count0[i] > count1[i] :
        output.append('0')   
    else:
        output.append('1')

print(''.join(output))