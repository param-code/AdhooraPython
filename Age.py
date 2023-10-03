#Check if the clients"s age is eligible to drive or not
age = int(input("Enter Your Current Age"))
if age > 18 and age < 80:
    print("Yeah! you are Eligible to Drive , come for the Test after Payment")
elif age < 18 or age > 80:
    print("Ricks hai.. You are legally ineligible for this Test")
elif age == 18:
    print("Can't say more.. you need to come here for valid verification..")
else:
    print("kripya Punha prayas kare")