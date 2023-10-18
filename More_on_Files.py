f = open("hello.txt","r")
print(f.readline())
print(f.tell())#Btata h file pointer kha h
f.seek(10)#file pointer ka location change kr deta h
print(f.tell())
f.close()