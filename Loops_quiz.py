#Check wheather the element in the list is a number or not and if yes is it > 6 or not and print it
# L1 = []
# for i in range(0,5):
#     s = input("Enter Something")
#     L1.append(s)
L1 = [ "Hello","Good",74, "$" , 2 , 5]
for element in L1:
    if type(element) == int and element > 6:
        print(element)