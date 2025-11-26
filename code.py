# Student Grade Calculator

print("===== Student Grade Calculator =====")

# Taking inputs
name = input("Enter student name: ")
math = float(input("Enter Math marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

# Calculating total and average
total = math + science + english
average = total / 3

# Determining grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

# Displaying results
print("\n===== Result =====")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
