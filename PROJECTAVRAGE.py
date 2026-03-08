a = int(input("enter a value: "))
b = int(input("enter the second value :"))
c = int(input("enter the third value: "))

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %(avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" %(avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" %(avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" %(avg, b, c))
elif avg > a:
    print("%d IS DEFINATLY HIGHER THAN %d" %(avg, a))
elif avg > b:
    print("%d IS DEFINATLY HIGHER THAN %d" %(avg, b))
elif avg > c:
    print("%d IS DEFINATLY HIGHER THAN %d" %(avg, c))
else:
  print("YOU HAVE PUT A INVALED NUMBER PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE CHECK YOUR NUMBERS AND TRY AGAIN")