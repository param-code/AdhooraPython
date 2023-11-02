# def add(a,b):
#     return a+b
# minus = lambda x,y : x-y #it's similar to above which means defining a funtion minus
# print(minus(4,5))
# def a_first(a):
#     return a[1]
# a_first = lambda a:a[1]
a = [[1,12],[0,4],[8,23]]
# a.sort(key=a_first) #upar wala function ke hisab se sort krega
a.sort(key=lambda x:x[1]) #key mtlb kis tarike se sort krna h
print(a)