# This program simulates a Magic 8 Ball, a toy that generates a random response to a yes/no question.
# The first part of this program should create a txt file titled '8ball_responses', with 12 responses.
# The second part of this program reads the responses from the file into a list.
# It then prompts the user for a yes/no question and randomly selects from the responses.
# The program loops until the user is ready to quit.

import random # Necessary for output responses.

# Part 1: creates 8ball_responses.txt and the subsequent list.
def write_responses_to_file():
    responses = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "I'll tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]

    with open("8ball_responses.txt", "w") as file:
        for response in responses:
            file.write(response + "\n")

# Part 2: Reads responses from the file.
def read_responses_from_file():
    with open("8ball_responses.txt", "r") as file: # Opens in read mode.
        return file.readlines()

# Part 3 (technically): Output function.
def magic_8_ball():
    responses = read_responses_from_file()
    while True:
        user_input = input("Ask a yes-or-no question (or type quit to exit): ")
        if user_input.lower().strip() == 'quit': # End if user wishes by typing quit.
            break
        else:
            random_response = random.choice(responses).strip()
            print(random_response)

write_responses_to_file()
magic_8_ball()