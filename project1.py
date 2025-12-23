# -------------------------------
# Student Grade Management System
# -------------------------------

# List to store all students
students = []

# Set to track unique subjects
unique_subjects = set()

# Function to calculate average marks
def calculate_average(marks):
    return sum(marks.values()) / len(marks)

# Function to assign grade
def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

# Function to add a new student
def add_student(name, age, subjects, marks):
    student = {
        "name": name,
        "age": age,
        "subjects": subjects,
        "marks": marks
    }
    students.append(student)

    # Update unique subjects set
    unique_subjects.update(subjects)

# Function to update student marks
def update_marks(student_name, subject, new_marks):
    for student in students:
        if student["name"] == student_name:
            if subject in student["marks"]:
                student["marks"][subject] = new_marks
                print("Marks updated successfully!")
                return
            else:
                print("Subject not found!")
                return
    print("Student not found!")

# Function to generate report card
def generate_report_card(student):
    average = calculate_average(student["marks"])
    grade = assign_grade(average)

    print("\n----- REPORT CARD -----")
    print(f"Name    : {student['name']}")
    print(f"Age     : {student['age']}")
    print("Marks   :")

    for subject, mark in student["marks"].items():
        print(f"  {subject.capitalize()} : {mark}")

    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}")
    print("------------------------")

# -------------------------------
# Adding students
# -------------------------------

add_student(
    "Krishna Nagini",
    27,
    ["english", "maths", "science"],
    {"english": 67, "maths": 74, "science": 58}
)

add_student(
    "Palani",
    30,
    ["english", "maths", "science"],
    {"english": 82, "maths": 85, "science": 91}
)

# -------------------------------
# Update marks
# -------------------------------

update_marks("Krishna Nagini", "maths", 85)

# -------------------------------
# Display all students with grades
# -------------------------------

print("\nALL STUDENT DETAILS")
print("====================")

for student in students:
    average = calculate_average(student["marks"])
    grade = assign_grade(average)

    print(f"Name: {student['name']}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print("-" * 30)

# -------------------------------
# Show unique subjects
# -------------------------------

print("\nUnique Subjects Offered:")
print(unique_subjects)

# -------------------------------
# Generate individual report card
# -------------------------------

generate_report_card(students[0])
