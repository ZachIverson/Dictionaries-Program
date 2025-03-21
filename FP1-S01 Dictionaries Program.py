# Name: Zach Ignacio
# Program: Student Grading System
# Description: This program manages student's grades using lists and dictionaries.

# List to store student names
students = ["Zach", "Carter", "David"]

# Grades and subjects dictionary for each students.
grades = {
    "Zach": {"Math": 85, "English": 78},
    "Carter": {"Math": 90, "English": 82},
    "David": {"Math": 76, "English": 88}
}

# 1. Append a new student
students.append("Hailey")
grades["Hailey"] = {"Math": 92, "English": 81}

# 2. edit a value (Updating a grade)
grades["Zach"]["Math"] = 89

# 3. Add a key:value pair (Adding a new subject for a student)
grades["Carter"]["Science"] = 87

# 4. Delete a student
students.remove("David")
grades.pop("David", None)

# 5. Get the length (number of students)
num_students = len(students)

# 6. Return values (All grades of a student)
zach_grades = grades["Zach"].values()

# 7. Add values (Adding a new subject for all students)
for student in grades:
    grades[student]["History"] = 80  # Default value

# 8. Return keys (Subjects for a student)
carter_subjects = grades["Carter"].keys()

# 9. Return items (Student name and their grades)
all_students_data = grades.items()

# 10. Get (Retrieve a student's grade safely)
hailey_math_grade = grades.get("Hailey", {}).get("Math", "No grade found")

# Display results
print("Students:", students)
print("Grades:", grades)
print("Number of students:", num_students)
print("Zach's Grades:", list(zach_grades))
print("Carter's Subjects:", list(carter_subjects))
print("Hailey's Math Grade:", hailey_math_grade)
