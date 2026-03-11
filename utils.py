# utils.py

# This module contains helper functions for:
#  File handling
#  Validation
#  Calculations
# Recursion & lambda usage
# Exception handling



#  Custom Exception 
class InvalidMarksError(Exception):
    """Raised when marks are not in the range 0–100."""
    pass


# Validation Functions 
def validate_student_id(student_id):
    """
    Uses assert to validate student ID format.
    Example valid ID: S001
    """
    assert student_id.startswith("S") and student_id[1:].isdigit(), \
        "Student ID must start with 'S' followed by digits"


def validate_marks(marks):
    """
    Raises a custom exception if any mark is invalid.
    """
    for m in marks:
        if m < 0 or m > 100:
            raise InvalidMarksError("Marks must be between 0 and 100")


#  File Handling 
def read_students(filename):
    """
    Reads student records from students.txt
    using a context manager (with open).
    """
    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                sid, name, math, science, english = line.split(",")

                students.append({
                    "id": sid,
                    "name": name,
                    "math": int(math),
                    "science": int(science),
                    "english": int(english)
                })

    except FileNotFoundError:
        print("students.txt not found. It will be created automatically.")

    except ValueError:
        print("Invalid data format in students.txt.")

    return students


def write_students(filename, students):
    """
    Writes all student records back to students.txt
    """
    with open(filename, "w") as file:
        file.write("# Student Records File\n")
        file.write("# Format: StudentID,StudentName,Math,Science,English\n\n")
        for s in students:
            file.write(
                f"{s['id']},{s['name']},"
                f"{s['math']},{s['science']},{s['english']}\n"
            )


#  Functional Requirements 
def add_student(filename, student_id, name, marks):
    """
    Adds a new student record.
    Prevents duplicate student IDs.
    """
    validate_student_id(student_id)
    validate_marks(marks)

    students = read_students(filename)

    # Prevent duplicate ID
    for s in students:
        if s["id"] == student_id:
            print("Duplicate student ID. Record not added.")
            return

    students.append({
        "id": student_id,
        "name": name,
        "math": marks[0],
        "science": marks[1],
        "english": marks[2]
    })

    write_students(filename, students)
    print("Student record added successfully.")


def search_student(filename, student_id):
    """
    Searches for a student by ID.
    """
    students = read_students(filename)
    for s in students:
        if s["id"] == student_id:
            return s
    return None


def update_student(filename, student_id, new_marks):
    """
    Updates marks of an existing student.
    """
    validate_marks(new_marks)
    students = read_students(filename)

    for s in students:
        if s["id"] == student_id:
            s["math"], s["science"], s["english"] = new_marks
            write_students(filename, students)
            print("Student record updated.")
            return

    print("Student not found.")


def delete_student(filename, student_id):
    """
    Deletes a student record by ID.
    """
    students = read_students(filename)
    updated = [s for s in students if s["id"] != student_id]

    if len(updated) == len(students):
        print("Student not found.")
    else:
        write_students(filename, updated)
        print("Student record deleted.")


#  Recursive Function 
def calculate_average_recursive(marks, index=0):
    """
    Calculates total marks using recursion.
    """
    if index == len(marks):
        return 0
    return marks[index] + calculate_average_recursive(marks, index + 1)


def calculate_average(marks):
    """
    Calculates average using recursive total.
    """
    total = calculate_average_recursive(marks)
    return total / len(marks)


#  Lambda Functions 
def assign_grade(avg):
    """
    Assigns grade based on average marks.
    """
    if avg >= 75:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"


def get_highest_lowest(students):
    """
    Finds highest and lowest averages using lambda expressions.
    """
    highest = max(
        students,
        key=lambda s: calculate_average(
            [s["math"], s["science"], s["english"]]
        )
    )

    lowest = min(
        students,
        key=lambda s: calculate_average(
            [s["math"], s["science"], s["english"]]
        )
    )

    return highest, lowest


#  Summary Report 
def generate_summary_report(filename, report_file):
    """
    Generates a summary report file.
    """
    students = read_students(filename)

    if not students:
        print("No data available for report.")
        return

    with open(report_file, "w") as file:
        file.write("===== Student Summary Report =====\n\n")
        file.write(f"Total Students: {len(students)}\n\n")

        for s in students:
            avg = calculate_average(
                [s["math"], s["science"], s["english"]]
            )
            grade = assign_grade(avg)
            file.write(
                f"{s['id']} - {s['name']} | "
                f"Average: {avg:.2f} | Grade: {grade}\n"
            )

    print("Summary report generated successfully.")
