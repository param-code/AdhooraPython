# def function_name_print(a,b,c,d):
#     print(a,b,c,d)
# function_name_print("Harry","Rohan","Skillf","Hammad")
def funargs(normal,*args,**kwargs):#* ke baad args ke jagah par kuch aur bhi likh skte hai aur normal arguments ko pehle pass krna hai , * wale ko baad me aur ** ko uske bhi baad mein [args aur kwargs optional hote hai.. agr arguments call krte waqt pass nhi bhi krenge toh bhi koi dikkat nhi hoga]
    # print(args[0])
    print(normal)
    for something in args:
        print(something)
    for key,value in kwargs.items():
        print(key,value)
har = ["Harry","Rohan","Skillf","Hammad","Shivam"]
kw = {"Rohan":"Macch","Harry":"Biryani","skillf":"digital-bits"} 
funargs("Helllo",*har,**kw) 