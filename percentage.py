print('enter marks obtained in 4 subjects: ')
math = int(input('maths :'))
english = int(input('english :'))
science = int(input('science :'))
dutch = int(input('dutch :'))


sum = math+english+science+dutch

print('sum of all subjects = ', sum)


perc = (sum/400)*100

print(perc)