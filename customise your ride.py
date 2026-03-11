print('select your ride!:')
print('1. bike')
print('2. car')


choice = int(input('what do you want to ride? (enter your choice) '))
if(choice==1):
    print('what type of bike do you want?')
    print('1. mountain bike\n')
    print('2. road bike\n')

    choice2 = int(input('enter your choice2: '))
    if(choice2==1):
        print('you have selected a mountain bike!')
    elif(choice2==2):
        print('you have selected a road bike!')
    else:
        print('invalid choice!')

elif(choice==2):
    print('what type of car do you want?')
    print('1. sports car\n')
    print('2. suv\n')

    choice3 = int(input('enter your choice3: '))
    if(choice3==1):
        print('you have selected a sports car!')
    elif(choice3==2):
        print('you have selected a suv!')
    else:
        print('invalid choice!')


else:
    print('invalid choice!')