def my_min(lists):
    
    minimum = 100
    for x in lists:
        if x > -1 and x < minimum:
            minimum = x  
    return minimum

def solution(line):

    first, last = '', ''
    suma = ""
    
    valid_words = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    valid_numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    vw_first = [line.find(x) for x in valid_words]
    vw_last = [line.rfind(x) for x in valid_words]
    
    vn_first = [line.find(x) for x in valid_numbers]
    vn_last = [line.rfind(x) for x in valid_numbers]
    
    #print("vw_first, vw_last", vw_first, vw_last)
    #print("vn_first, vn_last", vn_first, vn_last)

    if my_min(vw_first) < my_min(vn_first):
        first = vw_first.index(my_min(vw_first))
    elif my_min(vw_first) > my_min(vn_first):
        first = vn_first.index(my_min(vn_first)) 

    if max(vn_last) < max(vw_last):
        last = vw_last.index(max(vw_last))
    elif max(vn_last) > max(vw_last):
        last = vn_last.index(max(vn_last))
        

    #print(my_min(vw_first), my_min(vn_first))
    
    suma = str(first) + str(last)
    #print("first, last: ", first, last)
    suma = int(suma)
    #print('suma', suma)
    return suma

def Day1():
    with open('input.txt', 'r') as openfileobject:
        suma = 0
        for line in openfileobject:
            #print('linia', line)
            wynik = solution(line)
            suma += wynik
            #rint(wynik)
    
    return suma
    
Day1()
