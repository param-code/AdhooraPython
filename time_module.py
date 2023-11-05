import time
initial = time.time() # this function returns the number of ticks(seconds)
# print(initial)
for i in range(45):
    print("This is Harry Bhai")
print("For loop ran in",time.time() - initial)
initial2 = time.time()
k = 0
while k < 45:
    print("This is harry Bhai")
    time.sleep(2) #2seconds tk rukta h 
    k += 1
print("While loop ran in",time.time() - initial2)
localtime = time.asctime(time.localtime(time.time()))
print(localtime)