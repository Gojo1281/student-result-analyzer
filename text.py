NAME = input("Enter The Student: ")
MATHS = int(input("Enter The Maths Marks: "))
SCIENCE = int(input("Enter The Science Marks: "))
ENGLISH = int(input("Enter The English Marks: "))
TOTAL = MATHS + SCIENCE + ENGLISH
PERCENTAGE = (TOTAL / 300) * 100
GRADE = ""
if PERCENTAGE >= 90:
    GRADE = "A"
elif PERCENTAGE >= 80:
    GRADE = "B"
elif PERCENTAGE >= 70:
    GRADE = "C"
elif PERCENTAGE >= 60:
    GRADE = "D"
else:
    GRADE = "F"

if PERCENTAGE >= 40:
    RESULT = "PASS"
else:
    RESULT = "FAIL"
    

Subjects = {MATHS, SCIENCE, ENGLISH}
maximum_marks = max(Subjects)
minimum_marks = min(Subjects)
print("-----Report Card-----")
print("Name:", NAME)
print("Maths Marks:", MATHS)
print("Science Marks:", SCIENCE)
print("English Marks:", ENGLISH)
print("Total Marks:", TOTAL)
print("Percentage:", PERCENTAGE)
print("Grade:", GRADE)
print("Result:", RESULT)
print("Maximum Marks:", maximum_marks)
print("Minimum Marks:", minimum_marks)
    
