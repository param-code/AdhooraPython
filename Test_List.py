'''
if __name__ == '__main__':
    N = int(input())
    my_list = []
    for x in range(N):
        c = input()
        if c == "insert":
            i = int(input())
            e = int(input())
            my_list.insert(i,e)
        elif c == "print":
            print(my_list)
        elif c == "remove":
            e = int(input())
            my_list.remove(e)
        elif c == "append":
            e = int(input())
            my_list.append(e)
        elif c == "sort":
            my_list.sort()
        elif c == "pop":
            my_list.pop()
        elif c == "reverse":
            my_list.reverse()
        x = x + 1
'''
if __name__ == '__main__':
    N = int(input())
    my_list = []
    for x in range(N):
        command = input().split()
        if command[0] == "insert":
            i = int(command[1])
            e = int(command[2])
            my_list.insert(i,e)
        elif command[0] == "print":
            print(my_list)
        elif command[0] == "remove":
            e = int(command[1])
            my_list.remove(e)
        elif command[0] == "append":
            e = int(command[1])
            my_list.append(e)
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "pop":
            if my_list:
                my_list.pop()
        elif command[0] == "reverse":
            my_list.reverse()
        x = x + 1
