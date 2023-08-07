def reverse(str):
    if len(str) == 1:
        return str[0]    
    else:
        print(reverse(str[1:]) + str[0])
        return reverse(str[1:]) + str[0]

flower = 'lavender'

print(reverse(flower))