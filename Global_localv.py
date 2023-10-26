'''
l = 10 #Global
def function1(n):
    # l = 5 #Local
    # l = l + 10 #error ayega l = 10 ko local change nhi kr skta pr global l likh ke change kr skte h
    global l
    l = l + 45
    print(l)
    print(n,"I have Printed")
function1("This is me")
'''
def Harry():
    x = 20
    def Rohan():
        global x #pura bahar jata h na ki Harry ke local samjho bro
        x = 88 #ekdum bhar ek x variable bna dega
    print("Before Calling Rohan",x)
    Rohan()
    print("After Calling Rohan",x)

Harry()
print(x) #88 aayega dekhna 