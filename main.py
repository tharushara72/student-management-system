# main.py

# Main program file.
# Handles user input and program flow.


import utils
# File name used to store student data

FILE_NAME = "students.txt"

# Function to display all students and class statistics
def display_students():
     # Read student records from the file
    students = utils.read_students(FILE_NAME)
    # Check if there are any student records

    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
     # Loop through each student and display their marks, average, and grade
    for s in students:
        marks = [s["math"], s["science"], s["english"]]
        avg = utils.calculate_average(marks)
        grade = utils.assign_grade(avg)

        print(
            f"{s['id']} | {s['name']} | "
            f"Math: {s['math']} Science: {s['science']} English: {s['english']} | "
            f"Avg: {avg:.2f} | Grade: {grade}"
        )

    highest, lowest = utils.get_highest_lowest(students)
    # Get students with highest and lowest averages

    print("\n--- Class Statistics ---")
    print("Highest Average:", highest["name"])
    print("Lowest Average:", lowest["name"])
    # loop of main program 


def main():
    while True:
         # Display the main menu
        print("\n===== Student Marks Management System =====")
        print("1. Add student")
        print("2. View students")
        print("3. Search student by ID")
        print("4. Update student")
        print("5. Delete student")
        print("6. Generate summary report")
        print("7. Exit")

        choice = input("Enter choice: ")

        try:
            # Add a new student
            if choice == "1":
                sid = input("Student ID: ")
                name = input("Student Name: ")

                math = int(input("Math marks: "))
                science = int(input("Science marks: "))
                english = int(input("English marks: "))
                #using utils function Add student to the file

                utils.add_student(
                    FILE_NAME,
                    sid,
                    name,
                    [math, science, english]
                )
# View all student records
            elif choice == "2":
                display_students()

                # Search for a student by ID

            elif choice == "3":
                sid = input("Enter Student ID: ")
                student = utils.search_student(FILE_NAME, sid)

                if student:
                    marks = [student["math"], student["science"], student["english"]]
                    avg = utils.calculate_average(marks)
                    grade = utils.assign_grade(avg)
                    print(student, "Average:", avg, "Grade:", grade)
                else:
                    print("Student not found.")

                    # Update marks of an existing student

            elif choice == "4":
                sid = input("Student ID: ")
                math = int(input("New Math marks: "))
                science = int(input("New Science marks: "))
                english = int(input("New English marks: "))
                utils.update_student(FILE_NAME, sid, [math, science, english])

                # Delete a student record

            elif choice == "5":
                sid = input("Student ID: ")
                utils.delete_student(FILE_NAME, sid)

                # Generate a summary report of all students

            elif choice == "6":
                utils.generate_summary_report(FILE_NAME, "summary_report.txt")

                # Exit the program

            elif choice == "7":
                print("Program exited.")
                break
# Handle invalid menu option
            else:
                print("Invalid option.")

                # Handle invalid marks entered by the user

        except utils.InvalidMarksError as e:
            print("Error:", e)
 # Handle invalid student ID format
        except AssertionError as e:
            print("Invalid Student ID:", e)
            
            # Handle non-numeric input for marks

        except ValueError:
            print("Please enter numeric values only.")


if __name__ == "__main__":
    main()
