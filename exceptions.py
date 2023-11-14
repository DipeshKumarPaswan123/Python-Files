# a = input("Enter a")
# print(f"Multiplications of {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# except:
#     print("Invalid Input")
# print("Some lines aof code")
# print("End of code


# try:
#     num = int(input("Enter number"))
#     a = [4,5]
#     print(a[num])
# except ValueError:
#     print("Inavlid integer value")
# except IndexError:
#     print(" Invalid Index ")
# finally:
#     print("It always executed")


# def func1():
#     try:
#         l = [1,2,3,4,5]
#         i = int(input("Enter an index"))
#         print(l[i])
#         return 1
#     except:
#         print("Some error occured")
#         return 0
#     finally:
#         print("It always executed")
# x = func1()
# print(x)

# num  = int(input("Enter value between 10 and 20"))
# if  num<20 or num>20:
#     raise ValueError("value Error its not bewteen 10 and 20")

# def multiply(*args):
#     product = 1
#     for i in range:
#         product = product+1
#         return product

def display(**kwrgs):
    for (key,value)in kwargs.item():
        print(key,'->',value)



