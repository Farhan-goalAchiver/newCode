# Python program to calculate student result

name = "Rahul"

maths = 85
science = 78
english = 90
computer = 88
social = 75

total = maths + science + english + computer + social
average = total / 5

print("Student Name:", name)
print("Maths:", maths)
print("Science:", science)
print("English:", english)
print("Computer:", computer)
print("Social:", social)

print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
