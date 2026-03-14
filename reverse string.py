string = input('Please enter ur OWN string :')


string2 = ('')


for i in string:
    string2 = i + string2


print('\nThe original string =', string)
print('the reversed string =', string2)