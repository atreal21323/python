height = float(input('enter your height in cm'))
weight = float(input('enter your weight in KG'))


BMI = weight / (height/100)**2

print('your BMI is', BMI)


if BMI <= 18.4:
    print('you ARE UNDER WEIGHT.')

elif BMI <= 24.9:
    print ('YOU ARE HEALTHY.')
    
elif BMI <= 29.9:
    print ('YOU are OVER WEIGHT.')

elif BMI <= 34.9:
    print ('YOU ARE SEVERELY OVER WEIGHT.')

elif BMI <= 39.9:
    print ('YOU ARE OBESE.')

else:
    print('STOP IT HOW ARE YOU SO OVERWEIGHT GO TO THE GYM PLEASE')
