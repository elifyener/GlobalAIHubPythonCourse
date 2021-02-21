# ==========================================
#  Title:  Question 2
#  Author: elifyener
#  Date:   18 Feb 2021
# ==========================================

# Question 2
# Write a program that includes information about the grades of 5 students in a school.
#   -Keep these students' grades in a list. (Midterm, final, homework)
#   -Keep students' names in a list. (Name, surname)
#   -Create a dictionary name info and put all the information of students in a dictionary.
#   -Sort and list the students' grades here in descending order and congratulate the student with the highest score.

# List of names and surnames
nameInfos=[[],[]], [[],[]], [[],[]], [[],[]], [[],[]]

# With the information received from the user, names are assigned to index 0 and surnames to index 1
for i in range(5):
    print(f"{i+1}. student's name : ", end= " ")
    nameInfos[i][0] = input()
    print(f"{i+1}. student's surname : ", end= " ")
    nameInfos[i][1] = input()

# List with midterms, finals and homeworks    
noteInfos=[[],[],[]], [[],[],[]], [[],[],[]], [[],[],[]], [[],[],[]]

# With the information received from the user, midterms are assigned to index 0, finals to index 1 and homeworks to index 2
print("Please enter the values as integers otherwise all grades of the student will be evaluated as '0'!")

for i in range(5):
    try:
        print(f"{nameInfos[i][0]} {nameInfos[i][1]}'s midterm : ", end= " ")
        noteInfos[i][0] = int(input())
        print(f"{nameInfos[i][0]} {nameInfos[i][1]}'s final : ", end= " ")
        noteInfos[i][1] = int(input())
        print(f"{nameInfos[i][0]} {nameInfos[i][1]}'s homework: ", end= " ")
        noteInfos[i][2] = int(input())
    # If any value other than integer is entered, grades will be entered as 0    
    except ValueError:
        noteInfos[i][0] = 0
        noteInfos[i][1] = 0
        noteInfos[i][2] = 0

# When the information is put into dictionary, there will be a structure in the form of {"name surname": [midterm, final, homework]}.
information = {}
for i in range(5):
    information[nameInfos[i][0] + " " +nameInfos[i][1]] = noteInfos[i]
print(information)

maxi = 0
maxstd = ""
# The key is assigned to the variable k and the value to the variable v
for k,v in information.items():
    # All grades in the values are added up and divided into three to find the average.
    average = (v[0] + v[1] + v[2])/3
    # The highest grade and who got the highest grade (key) are found with the following condition statement
    if (maxi < average):
        maxi = average
        maxstd = k
print(f"Congratulations!!! {maxstd} got the highest score with {maxi}.")
