def solution(line):
    ''' Summing up entries from line '''
    
    red, green, blue = [], [], []

    split_line = line.split(' ')

    ID = split_line[1][0:-1]
    for i, x in enumerate(split_line):
        if x.startswith('red'):
            red.append(int(split_line[i-1]))
        if x.startswith('blue'):
            blue.append(int(split_line[i-1]))
        if x.startswith('green'):
            green.append(int(split_line[i-1]))
            
    power = max(red) * max(green) * max(blue)
    return power

def day2():
    ''' Main Function '''
    
    with open('Day2_input.txt', 'r') as f:
        suma = 0
        for line in f:            
            power = solution(line)
            suma += power
    return suma
            
day2()
