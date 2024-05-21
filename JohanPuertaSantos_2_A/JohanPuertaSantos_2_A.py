# Comments.

def create_readable_list():
    # Create a document with all 30 phrases.
    common_phrases = [
        "Amazing",
        "Bonus",
        "Certified",
        "Cheap",
        "Congratulations",
        "Consultation",
        "Deal",
        "Discount",
        "Expires",
        "Fantastic",
        "Free",
        "Gift",
        "Guaranteed",
        "Hesitate",
        "Hundred",
        "Instant",
        "Lifetime",
        "Limited",
        "Membership",
        "Millions",
        "New",
        "Now",
        "Offer",
        "Sample",
        "Start",
        "Supplies",
        "Trial",
        "Unlimited",
        "Urgent",
        "Winner",
    ]

    # Create a file from the list.
    with open("spam_checker.txt", 'w') as file:
        for i, phrase in enumerate(common_phrases):
            if i < len(common_phrases) - 1:
                file.write(phrase + "\n")
            else:
                file.write(phrase)

# Get user's e-mail for spam checking.
def get_email():
    print("This is a script that checks for spam likelihood in pasted e-mails.")
    print()
    print("Please paste your e-mail on a blank line and press ENTER thrice: ")

    # List used for appending to final version: email_content.
    lines = []

    # Loop to fix premature ending of input found in previous versions.
    while True:
        line = input()
        lines.append(line)
        # Forces input to wait for two consecutive linebreaks, instead of one.
        if line.strip() == "" and lines[-2].strip() == "":
            break

    email_content = "\n".join(lines)
    return email_content

# Function used for likelihood calculation. Separates words into a list and uses len for total count.
def count_words(email_content):
    words = [word for word in email_content.split() if len(word) > 1]
    total_words = len(words)
    return total_words

# Function used for comparing the e-mail to the list of spam words.
def compare_email(email_content):
    # Opens file.
    with open("spam_checker.txt", 'r') as file:
        common_phrases = [line.strip().lower() for line in file]

    # Makes email_content lowercase in case of case-sensitivity.
    email_content = email_content.lower()

    # Initializing spam counter and phrase list.
    spam_count = 0
    spam_phrases = []

    # For each phrase in common_phrases, if also found in email_content, add 1 to spam_count and append spam_phrases.
    for phrase in common_phrases:
        if phrase in email_content:
            spam_count += 1
            spam_phrases.append(phrase)

    return spam_count, spam_phrases

# Calculates likelihood of e-mail being spam.
def calculate_likelihood(total_words, spam_count, spam_words):
    if total_words == 0: # Fixes probable bug when dividing by zero.
        likelihood = 0
    else:
        likelihood = spam_count / total_words * 100
    print()
    print(f"Spam likelihood: {likelihood:.2f}%")
    print(f"Amount of words marked as spam: {spam_count}")
    print("Words found: " + ", ".join(spam_words))

def main():
    create_readable_list()
    email_content = get_email()
    total_words = count_words(email_content)
    spam_count, spam_words = compare_email(email_content)
    calculate_likelihood(total_words, spam_count, spam_words)

if __name__ == "__main__":
    main()