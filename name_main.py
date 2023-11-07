def printstr(string):
    return f"Ye string Harry ko de de thakur {string}"
def add(num1,num2):
    return num1 + num2 + 5
# print(printstr("Harry"))
# o = add(2,3)
# print(o)
print(f"And the name is {__name__}")
if __name__ == '__main__': # isse hoga ye ki jab dusre file mein is file ko import krenge to iske neeche(andar) wala execute nhi hoga
    print(printstr("Harry"))
    o = add(2,3)
    print(o)