# This is a simple program that takes 'grades.csv' and displays the data in tabular format.

import csv

def main():
    # Open 'grades.csv' file.
    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)
        data = list(reader)

    # Print data in tabular format.
    for row in data:
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))

main()