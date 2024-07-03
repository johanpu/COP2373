# This program utilizes the numpy library to calculate several operations for the 'grades.csv' file.
# This calculates the mean, median, std. dev., min, and the max of each exam, and then the combination of all three.

import numpy as np


# Load data from the 'grades.csv' file.
def get_data():
    # Separate exam data into variables.
    dtype = [('first_name', 'U10'), ('last_name', 'U10'), ('exam1', 'i4'), ('exam2', 'i4'), ('exam3', 'i4')]

    while True:
        try:
            grades = np.genfromtxt('grades.csv', delimiter=',', skip_header=1, dtype=dtype)
            if grades.size == 0:
                print("This file seems empty. Try again.")
            break
        except FileNotFoundError:
            print("\nFile Not Found. Ensure 'grades.csv' is in the same directory as this program.")
            break
    return grades


class CalculateExams:
    def __init__(self, grades):
        self.grades = grades

    def mean(self):
        exam1_mean = np.mean(self.grades['exam1'])
        exam2_mean = np.mean(self.grades['exam2'])
        exam3_mean = np.mean(self.grades['exam3'])

        combined_mean = np.mean(self.grades['exam1'] + self.grades['exam2'] + self.grades['exam3']) / 3

        return combined_mean, exam1_mean, exam2_mean, exam3_mean

    def median(self):
        exam1_median = np.median(self.grades['exam1'])
        exam2_median = np.median(self.grades['exam2'])
        exam3_median = np.median(self.grades['exam3'])

        combined_median = np.median(np.array([self.grades['exam1'], self.grades['exam2'], self.grades['exam3']]))

        return combined_median, exam1_median, exam2_median, exam3_median

    def std_dev(self):
        exam1_std_dev = np.std(self.grades['exam1'])
        exam2_std_dev = np.std(self.grades['exam2'])
        exam3_std_dev = np.std(self.grades['exam3'])

        combined_std_dev = np.std(np.array([self.grades['exam1'], self.grades['exam2'], self.grades['exam3']]))

        return combined_std_dev, exam1_std_dev, exam2_std_dev, exam3_std_dev

    def min(self):
        exam1_min = np.min(self.grades['exam1'])
        exam2_min = np.min(self.grades['exam2'])
        exam3_min = np.min(self.grades['exam3'])

        combined_min = np.min(np.array([self.grades['exam1'], self.grades['exam2'], self.grades['exam3']]))

        return combined_min, exam1_min, exam2_min, exam3_min

    def max(self):
        exam1_max = np.max(self.grades['exam1'])
        exam2_max = np.max(self.grades['exam2'])
        exam3_max = np.max(self.grades['exam3'])

        combined_max = np.max(np.array([self.grades['exam1'], self.grades['exam2'], self.grades['exam3']]))

        return combined_max, exam1_max, exam2_max, exam3_max

    def determine_passing(self):
        exam1_passes = np.sum([self.grades['exam1'] >= 60])
        exam2_passes = np.sum(self.grades['exam2'] >= 60)
        exam3_passes = np.sum(self.grades['exam3'] >= 60)
        pass_percentage = ((exam1_passes + exam2_passes + exam3_passes) / 0.3)

        return exam1_passes, exam2_passes, exam3_passes, pass_percentage


def main(grades):
    calculate = CalculateExams(grades)
    mean = calculate.mean()
    median = calculate.median()
    std_dev = calculate.std_dev()
    min = calculate.min()
    max = calculate.max()
    exam1_passes, exam2_passes, exam3_passes, pass_percentage = calculate.determine_passing()

    print(f"\nIndividual Exam Data (Exam1, Exam2, Exam3):\n"
            f"Mean: {mean[1]:.2f}%, {mean[2]:.2f}%, {mean[3]:.2f}%\n"
            f"Median: {median[1]:.2f}%, {median[2]:.2f}%, {median[3]:.2f}%\n"
            f"Standard Deviation: {std_dev[1]:.2f}%, {std_dev[2]:.2f}%, {std_dev[3]:.2f}%\n"
            f"Min: {min[1]:.2f}%, {min[2]:.2f}%, {min[3]:.2f}%\n"
            f"Max: {max[1]:.2f}%, {max[2]:.2f}%, {max[3]:.2f}%\n\n"
            f"Combined Exam Data:\n"
            f"Mean: {mean[0]:.2f}%\n"
            f"Median: {median[0]:.2f}%\n"
            f"Standard Deviation: {std_dev[0]:.2f}%\n"
            f"Min: {min[0]:}%\n"
            f"Max: {max[0]:}%\n\n"
            f"Exam1: {exam1_passes} students passed and {grades.size - exam1_passes} students failed.\n"
            f"Exam2: {exam2_passes} students passed and {grades.size - exam2_passes} students failed.\n"
            f"Exam3: {exam3_passes} students passed and {grades.size - exam3_passes} students failed.\n"
            f"Across all exams, the overall pass percentage was {pass_percentage:.2f}%.")


if __name__ == '__main__':
    grades = get_data()
    main(grades)