l1 = ["Bhindi","Aaloo","Chopsticks","Chow-mein"]
i = 1
for item in l1: # it will not print every 2nd element in the list
    if i % 2 != 0:
        print(f"Jarvis , Please buy {item}")
    i += 1

# using enumerate funtion doing the same as above
for index,item in enumerate(l1):
    if index % 2 == 0: # here i will start from 0 as default but above we had started it from 1 by assigning i = 1
        print(f"Jarvis , Please buy {item}")