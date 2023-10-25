def gettime():
    import datetime
    return datetime.datetime.now()
def prompt():
    Job = int(input("Enter 1 to Lock or 2 to Retrieve\n"))
    name = input("Enter Your Name").lower()
    Action = int(input("Enter 1 for Exercise and 2 for Diet"))
    if Job == 1 and name == "harry" and Action == 1:
        with open("HarryE.txt","a") as f:
            f.write(gettime,input())
    elif Job == 1 and name == "hamad" and Action == 1:
        with open("HamadE.txt","a") as f:
            f.write(input())
    elif Job == 1 and name == "rohan" and Action == 1:
        with open("RohanE.txt","a") as f:
            f.write(gettime,input())
    elif Job == 1 and name == "harry" and Action == 2:
        with open("HarryF.txt","a") as f:
            f.write(gettime,input())
    elif Job == 1 and name == "hamad" and Action == 2:
        with open("HamadF.txt","a") as f:
            f.write(gettime,input())
    elif Job == 1 and name == "rohan" and Action == 2:
        with open("RohanF.txt","a") as f:
            f.write(gettime,input())
    elif Job == 2 and name == "harry" and Action == 1:
        with open("HarryE.txt","r") as f:
            f.read()
    elif Job == 2 and name == "hamad" and Action == 1:
        with open("HamadE.txt","r") as f:
            f.read()
    elif Job == 2 and name == "rohan" and Action == 1:
        with open("RohanE.txt","r") as f:
            f.read()
    elif Job == 2 and name == "harry" and Action == 2:
        with open("HarryF.txt","r") as f:
            f.read()
    elif Job == 2 and name == "hamad" and Action == 2:
        with open("HamadF.txt","a") as f:
            f.read()
    elif Job == 2 and name == "rohan" and Action == 2:
        with open("RohanF.txt","a") as f:
            f.read()

while True:
    condition = input("Press Enter to start or Type Exit\n").lower()
    if condition == "exit":
        break
    prompt()