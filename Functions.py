#In-built Function
a = 10
b = 20
summ = sum((a,b))
# print(summ)
#User-Defined Functions
def func1(c,d):
    """This is a function which calculates the sum of two numbers"""
    return c + d
print(func1(10,20))
print(func1.__doc__)