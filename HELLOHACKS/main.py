import random

class Student:
    group = []
    points = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email

def makeQuiz(op, num, b1, b2): 
    res = []
    for i in range(num):
        n1 = random.randint(b1, b2)
        n2 = random.randint(b1, b2)
        res.append(str(n1) + " " + op + " " + str(n2))
    return res

def doQuiz(student, quiz):
    score = 0
    for i in range(len(quiz)):
        print(quiz[i] + " = ?")
        try:
            inp = input("Enter your answer: ")
            if int(inp) == eval(quiz[i]):
                print("Correct!")
                print("")
                student.points+=1
                score+=1
            else:
                print("So Close.")
                print("")
        except:
            print("Invalid Answer")
    
    return int(100 * (round((score / len(quiz)), 2)))

def doTest(student):
    numQ = 3
    b1 = 0
    b2 = 12
    print("Welcome " + student.name + ", To Your Diagnostic Test!")
    print("")
    input("Press Enter To Start")
    addition = makeQuiz("+", numQ, b1, b2)
    print("")
    print("---Addition---")
    print("")
    mark = doQuiz(student, addition)
    print("")
    print("You earned a " + str(mark) + "% in this section.")
    if mark < 50:
        student.group.append("Addition")
        print("You have been added to the addition group.")
        print("")
    else:
        print("You passed this section!")
        print("")
    subtraction = makeQuiz("-", numQ, b1, b2)
    print("---Subtraction---")
    print("")
    mark = doQuiz(student, subtraction)
    print("")
    print("You earned a " + str(mark) + "% in this section")
    if mark < 50:
        student.group.append("Subtraction")
        print("You have been added to the subtraction group.")
        print("")
    else:
        print("You passed this section!")
        print("")
    multiplication = makeQuiz("*", numQ, b1, b2)
    print("---Multiplication---")
    print("")
    mark = doQuiz(student, multiplication)
    print("")
    print("You earned a " + str(mark) + "% in this section")
    if mark < 50:
        student.group.append("Multiplication")
        print("You have been added to the multiplication group")
        print("")
    else:
        print("You passed this section!")
        print("")

def printProfile(student):
    print("Name: " + student.name)
    print("Email: " + student.email)
    print("Points: " + str(student.points))
    print("Groups: " + ', '.join([str(elem) for elem in student.group]))




s1 = Student("Troy Wu", "troywu5@gmail.com")
s2 = Student("Jason Kuo", "jkuo@gmail.com")
s2.points = 9
s2.group = ["Addition"]
s3 = Student("Alia Xu", "axu49@gmail.com")
s3.points = 4
s3.group = ["Subtraction", "Multiplication"]

sArr = [s1, s2, s3]

doTest(s1)

for i in range(len(sArr)):
    printProfile(sArr[i])
    print("")

pointArr = []
if s1.points < s3.points:
    pointArr.append(s1)
    pointArr.append(s3)
else: 
    pointArr.append(s3)
    pointArr.append(s1)

pointArr.append(s2)
pointArr.reverse()

print("---POINT LEADERBOARD---")
for i in range(len(pointArr)):
    print(str((i+1))+ ". " + pointArr[i].name + " (" + str(pointArr[i].points) + ")")





