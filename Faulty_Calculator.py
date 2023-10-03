# 45 *3 = 555 ,56+9 = 77 , 56/6 = 4
first_num = int(input("Enter your First Number"))
operator = input("choose - ,+ ,- ,* ,/")
second_num = int(input("Enter your Second Number"))
if operator == "+":
    print(first_num + second_num)
elif first_num == 45 and operator == "*" and second_num == 3:
    print("555")
elif first_num == 56 and operator == "+" and second_num == 9:
    print("77")
elif first_num == 56 and operator == "/" and second_num == 6:
    print("4")
elif operator == "-":
    print(first_num - second_num)
elif operator == "*":
    print(first_num * second_num)
elif operator == "/":
    print(first_num / second_num)
else:
    print("Enter a valid operator")