import re

def solution(line):
    ''' Summing up entries from line '''

    left, right = line.split(':')[1].split('|')
    winning_cards = {int(number) for number in re.findall(r'\d+', left)}
    my_cards = {int(number) for number in re.findall(r'\d+', right)}
    
    num_matches = len(winning_cards & my_cards)
    points = 2 ** (num_matches - 1) if num_matches > 0 else 0
            
    #print(winning_cards, my_cards, ans, '\n')
    return points

def day4():
    ''' Main Function '''
    
    with open('Day4_input.txt', 'r') as f:
        suma = 0
        for line in f:            
            ans = solution(line)
            suma += ans
    return suma
            
day4()