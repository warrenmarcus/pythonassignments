#Warren Green
#006314031


#function declarations
#This function is used to convert scores into GPA
def gpa(score):
    # grade A
    if x >= 93:
        gpa = 4.0
    # grade A-
    elif x <= 92 and x >= 90:
        gpa = 3.7
    # grade B+
    elif x <= 89 and x >= 87:
        gpa = 3.3
    # grade B
    elif x <= 86 and x >= 83:
        gpa = 3.0
    # grade B-
    elif x <= 82 and x >= 80:
        gpa = 2.7
    # grade C+
    elif x <= 79 and x >= 77:
        gpa = 2.3
    # grade C
    elif x <= 76 and x >= 73:
        gpa = 2.0
    # grade C-
    elif x <= 72 and x >= 70:
        gpa = 1.7
    # grade D+
    elif x <= 69 and x >= 67:
        gpa = 1.3
    # grade D
    elif x <= 66 and x >= 63:
        gpa = 1.0
    # grade D-
    elif x <= 62 and x >= 60:
        gpa = 0.7
    # grade F
    else:
        gpa = 0.0
    return gpa

# This function calculates total GPA
def gpaAll(gradelist):
    i = 0
    total = 0.0
    while i < numofclasses:
        total += gradelist[i]
        i += 1
    print("\nQuarter GPA: ", total / numofclasses, "\n")



# declaring lists/arrays to store different information
score = []
gradelist = []
courses = []

# different variables to keep track positions
name = input("Enter Student's Name: ")
numofclasses = int(input("enter number of classes? "))
i = 0
j = 0



#loop for inputing information into the list
# the function gpa(score) is used inside the append function for gradelist
while i < numofclasses:
    print("Course#",i+1, end = '? ')
    course = input()
    x = int(input("Course Grade (0-100) "))

    score.append(x)
    gradelist.append(gpa(score))
    courses.append(course)
    i += 1



#printing header for report card
print("\nHere is :", name,"\b's Report Card")
print("--------------------------------------------")
print ("Course:\t Grade:\t GPA")
print("--------------------------------------------")


# loop for printing the course name, score, and gpa
while j < numofclasses:
    print(courses[j], " :\t",score[j], " :\t", gradelist[j])
    j += 1

# prints the total GPA for the quarter
gpaAll(gradelist)
