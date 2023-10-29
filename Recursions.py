# def print2(str1):
#     # print2(str1) #apne hi andar jata rhega
#     print("This is\t" + str1)
# print2("Harry")
# def factorial(n): #Iterative Approach 
#     """
#     parameters - (n) integer
#     return - n * n-1 * n-2 ... * 1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
# number = int(input("Enter Your Number :"))
# print("Factorial Using Iterative method :",factorial(number))
# def factorial(n): #Recursive Approach
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# number = int(input("Enter your Number :"))
# print("Factorial Using Recursive Approach :",factorial(number))

# Quiz - Create a Function to create Fibonacci SERIES i.e. 0 1 1 2 3 5...
def fibonacci(n):#n is the index
    if n == 1:
        return 0
    elif n == 2: 
        return 1
    else:
        return  fibonacci(n-1) + fibonacci(n-2)
number = int(input("Enter your Number"))
print(fibonacci(number))