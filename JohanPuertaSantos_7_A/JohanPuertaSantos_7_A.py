# This program takes a user's input and separates each sentence, including sentences that begin with numbers.
# Then, the program will print each sentence it found and tally them up.

import re

# Function takes user's input and separates each sentence by using regular expressions.
def main():
    # Takes user's input and stores it.
    text = input("Please enter your text (press ENTER when finished):\n")

    # Separates each sentence by using reg. expression. Follows pattern as criteria.
    # Requires accurate grammar for accurate results.
    pattern = r'[A-Z].*?[.!?](?= [A-Z]|$)'
    sentences = re.findall(pattern, text, flags=re.DOTALL)

    # Initializes count variable, then counts each sentence found.
    count = 0
    for i in range(len(sentences)):
        count += 1

    # Prints each sentence and total number of sentences found.
    print()
    print("Found sentences: ", sentences)
    print("The total number of sentences found is: ", count)

# Calls main.
main()