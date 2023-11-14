'''a = 1
while a <= 10:
    print(a)
    a = a+1'''

a = 1
number = 0
number = int(input("Enter a number which you want to print table..."))
while a <= 10:
    print("%d X %d = %d \n" % (number, a, number*a))
    a = a+1;
