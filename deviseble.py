print('Enter a Number (numerator): ')
numn = int(input())
print('Enter a Number (denominator): ')
numb = int(input())

if numn%numb == 0:
  print(str(numn) + " is divisible by " + str(numb))
else:
  print(str(numn) + " is not divisible by " + str(numb))