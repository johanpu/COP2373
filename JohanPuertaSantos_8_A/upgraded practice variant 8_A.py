# This program is a simple grade recorder. It takes five inputs (First/Last name and three exam scores).
# It stores these inputs into a CSV file, which is then read and reformatted into a table automatically.

import csv
import os


def existing_data():
    # Check if 'grades.csv' exists.
    if os.path.exists('grades.csv'):
        print("Existing data found in 'grades.csv'.")
        while True:
            ask_to_rewrite = input("Would you like to overwrite the existing data? (y/n): ").lower()
            if ask_to_rewrite in {'y', 'n'}:
                append_file = ask_to_rewrite == 'n'
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    else:
        append_file = False

    return append_file


def create_data(append_file):
    # Get student count.
    student_count = int(input("How many students would you like to input? "))

    # Adds headers for CSV file.
    headers = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]

    # Get student data.
    students = []
    for i in range(student_count):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        exam1 = int(input("Enter student's score for Exam 1: "))
        exam2 = int(input("Enter student's score for Exam 2: "))
        exam3 = int(input("Enter student's score for Exam 3: "))
        print()  # Prints blank line for easier readability.
        students.append([first_name, last_name, exam1, exam2, exam3])

    # Write or append student data to CSV file.
    if append_file:
        with open("grades.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(students)
    else:
        with open("grades.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(students)

    # Print confirmation.
    print("Student data has been recorded to 'grades.csv'.")


def format_data():
    # Open 'grades.csv' file.
    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)
        data = list(reader)

    # Print data in tabular format.
    for row in data:
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))


# Cleans up the ends of each row. Strips trailing commas that sometimes popped up and messed with week 11's assignment.
def cleanData():
    with open("grades.csv", "r", newline="") as file:
        lines = file.readlines()

    cleaned_lines = [line.rstrip(",\n") + "\n" for line in lines]

    with open("grades.csv", "w", newline="") as file:
        file.writelines(cleaned_lines)


def main():
    append_file = existing_data()
    create_data(append_file)
    format_data()


main()