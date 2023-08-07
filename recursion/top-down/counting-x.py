def count_x(str):
    str = str.lower()

    #case: if there is no more string left to count, then it returns 0
    if len(str) == 0:
        return 0
        
    if str[0] == 'x':
        return 1 + count_x(str[1:])
    
    else:
        return count_x(str[1:])


string = 'xRDxSXX' 

print(count_x(string)) # 4  