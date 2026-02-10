n = int(input("Enter the number of student marks that clg want to store :"))
marks = []
names = []
valid_students=0
failed_students=0
for i in range(n):
    name = input("Enter name of student " + str(i+1) + ": ")
    names.append(name)
    mark = int(input("Enter mark of the student:  "))
    marks.append(mark)
print("STUDENT NAMES: " ,names)
print("MARKS OF STUDENTS " ,marks)
for i in range(n):
    mark = marks[i]
    name = names[i]
    if 100 >= mark >= 0:
        if 100 >= mark >= 90:
            print(name, ":" ,mark, " -->", "Excellent")
            valid_students += 1
        elif 75 <= mark <= 89:
            valid_students += 1
            print(name , ":", mark, " -->", "Very Good")
        elif 74 >= mark >= 60:
            valid_students += 1
            print(name, ":", mark, " -->", "Good")
        elif 40 <= mark <= 59:
            valid_students += 1
            print(name, ":", mark, " -->", "Average")
        else:
            print(name, ":", mark, " -->", "Fail")
            failed_students += 1
            valid_students += 1

    else:
        print(name, ":", mark, " -->", "Invalid mark")

print("Total valid students",valid_students)
print("Total Failed students",failed_students)