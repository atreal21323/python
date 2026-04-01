def add (P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q

print('please select the operation')
print('a. Add')
print('b. Subtract')
print('c. multiply')
print('d. Divide')

choice = input('please enter choice(a/ b/ c/ d/)>')


num_1 = int (input ('please enter the first number>'))
num_2 = int (input ('please enter the second number>'))


if choice == 'a':
    print(add(num_1, num_2))

elif choice == 'b':
    print(subtract(num_1, num_2))

elif choice == 'c':
    print(multiply(num_1, num_2))

elif choice == 'd':
    print(divide(num_1, num_2))
else:
    print('Invalid choice')


