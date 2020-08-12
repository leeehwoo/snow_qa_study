number = 0
sum = 0
while number <= 1000:
    number = number + 1
    if number % 3 == 0:
        sum = sum + number
    else:
        continue

print (sum)

a = 0
while a < 5:
    a = a+1   
    print ("*" * a)

b = range(0,100)
num = 0
for num in b:
    num = num + 1
    print (num, end = " ")


