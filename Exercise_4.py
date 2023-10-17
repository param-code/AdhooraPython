# Pattern Printing
n = int(input("O for Ulta or 1 for Seedha"))
r = int(input("No. of Rows"))
b = bool(n)
i = 1
if b == True:
    for i in range(r):
        print("*" * i)
        i += 1
else:
    for i in range(r):
        print("*" * r)
        r -= 1