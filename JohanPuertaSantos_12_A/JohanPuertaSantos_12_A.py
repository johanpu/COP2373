# This program utilizes the numpy library to calculate several operations for the 'grades.csv' file.
# This calculates the mean, median, std. dev., minimum, and the maximum of each exam,
# and then the combination of all three.

# Importing the library as np improves readability and shortens line length.
import numpy as np


# Load data from the 'grades.csv' file.
def get_data():
    # Separate exam data into variables.
    dtype = [('first_name', 'U10'), ('last_name', 'U10'), ('exam1', 'i4'), ('exam2', 'i4'), ('exam3', 'i4')]

    while True:
        try:
            # Removes header and opens 'grades.csv'.
            grades = np.genfromtxt('grades.csv', delimiter=',', skip_header=1, dtype=dtype)
            if grades.size == 0:
                # Not necessarily needed, but there in case it happens.
                print("This file seems empty. Try again.")
            break
        except FileNotFoundError:
            # File not found. Either not named right or not in right directory. Will end script.
            print("\nFile Not Found. Ensure 'grades.csv' is in the same directory as this program.")
            break
    return grades


class CalculateExams:
    def __init__(self, grades):
        self.grades = grades

    def mean(self):
        # Individually calculates mean for each exam, then combines them for combined_mean. Divides by 3 for average.
        exam1_mean = np.mean(self.grades['exam1'])
        exam2_mean = np.mean(self.grades['exam2'])
        exam3_mean = np.mean(self.grades['exam3'])

        combined_mean = (exam1_mean + exam2_mean + exam3_mean) / 3

        return combined_mean, exam1_mean, exam2_mean, exam3_mean

    def median(self):
        # Same method as mean, but uses np.median.
        exam1_median = np.median(self.grades['exam1'])
        exam2_median = np.median(self.grades['exam2'])
        exam3_median = np.median(self.grades['exam3'])

        combined_median = np.median(np.array([exam1_median, exam2_median, exam3_median]))

        return combined_median, exam1_median, exam2_median, exam3_median

    def std_dev(self):
        exam1_std_dev = np.std(self.grades['exam1'])
        exam2_std_dev = np.std(self.grades['exam2'])
        exam3_std_dev = np.std(self.grades['exam3'])

        # Method is different compared to others because of how std. dev. is calculated.
        combined_std_dev = np.std(np.array([self.grades['exam1'], self.grades['exam2'], self.grades['exam3']]))

        return combined_std_dev, exam1_std_dev, exam2_std_dev, exam3_std_dev

    def minimum(self):
        # Same method as mean, but uses np.minimum.
        exam1_minimum = np.minimum(self.grades['exam1'])
        exam2_minimum = np.minimum(self.grades['exam2'])
        exam3_minimum = np.minimum(self.grades['exam3'])

        combined_minimum = np.minimum(np.array([exam1_minimum, exam2_minimum, exam3_minimum]))

        return combined_minimum, exam1_minimum, exam2_minimum, exam3_minimum

    def maximum(self):
        # Self-explanatory. Uses np.maximum.
        exam1_maximum = np.maximum(self.grades['exam1'])
        exam2_maximum = np.maximum(self.grades['exam2'])
        exam3_maximum = np.maximum(self.grades['exam3'])

        combined_maximum = np.maximum(np.array([exam1_maximum, exam2_maximum, exam3_maximum]))

        return combined_maximum, exam1_maximum, exam2_maximum, exam3_maximum

    def determine_passing(self):
        # Calculates passing scores using np.sum. Marks true for passing, false for under 60.
        exam1_passes = np.sum([self.grades['exam1'] >= 60])
        exam2_passes = np.sum(self.grades['exam2'] >= 60)
        exam3_passes = np.sum(self.grades['exam3'] >= 60)

        # Divides by 0.3 because of 30 original scores, then multiplied by 100 for percentage.
        pass_percentage = ((exam1_passes + exam2_passes + exam3_passes) / 0.3)

        return exam1_passes, exam2_passes, exam3_passes, pass_percentage


def main(grades):
    calculate = CalculateExams(grades)
    mean = calculate.mean()
    median = calculate.median()
    std_dev = calculate.std_dev()
    minimum = calculate.minimum()
    maximum = calculate.maximum()
    exam1_passes, exam2_passes, exam3_passes, pass_percentage = calculate.determine_passing()

    # Prints out all statistics. Looks messy, but it works.
    print(f"\nIndividual Exam Data (Exam1, Exam2, Exam3):\n"
          f"Mean: {mean[1]:.2f}%, {mean[2]:.2f}%, {mean[3]:.2f}%\n"
          f"Median: {median[1]:.2f}%, {median[2]:.2f}%, {median[3]:.2f}%\n"
          f"Standard Deviation: {std_dev[1]:.2f}%, {std_dev[2]:.2f}%, {std_dev[3]:.2f}%\n"
          f"Min: {minimum[1]:.2f}%, {minimum[2]:.2f}%, {minimum[3]:.2f}%\n"
          f"Max: {maximum[1]:.2f}%, {maximum[2]:.2f}%, {maximum[3]:.2f}%\n\n"
          f"Combined Exam Data:\n"
          f"Mean: {mean[0]:.2f}%\n"
          f"Median: {median[0]:.2f}%\n"
          f"Standard Deviation: {std_dev[0]:.2f}%\n"
          f"Min: {minimum[0]:}%\n"
          f"Max: {maximum[0]:}%\n\n"
          # Uses grades.size to subtract from total students, thus finding fails without needing a new variable.
          f"Exam1: {exam1_passes} students passed and {grades.size - exam1_passes} students failed.\n"
          f"Exam2: {exam2_passes} students passed and {grades.size - exam2_passes} students failed.\n"
          f"Exam3: {exam3_passes} students passed and {grades.size - exam3_passes} students failed.\n"
          f"Across all exams, the overall pass percentage was {pass_percentage:.2f}%.")


if __name__ == '__main__':
    grades = get_data()
    main(grades)
