# This program reads an attached e-mail and scans through the document, rating the likelihood
# of the e-mail being spam based on the recurrence of thirty common words and phrases found in
# spam messages. Each occurrence of a word adds a point to a spam score, which is then
# displayed for the user to read, along with the likelihood that the message is spam
# and the words and/or phrases that caused it to be marked as such.
import sys

def create_readable_list():
    # Create a document with all the phrases.
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

    with open("spam_checker.txt", 'w') as file:
        for i, phrase in enumerate(common_phrases):
            if i < len(common_phrases) - 1:
                file.write(phrase + "\n")
            else:
                file.write(phrase)

def get_email():
    print("This is a script that checks for spam likelihood in e-mails.")
    print()
    print("Please paste your e-mail and, on a BLANK LINE, press CTRL+Z (CMD+D on MAC) when done: ")
    email_content = sys.stdin.read()
    return email_content

def count_words(email_content):
    # Used for likelihood calculator. Does not include single-character words (like a, or I).
    words = [word for word in email_content.split() if len(word) > 1]
    total_words = len(words)
    return total_words

def compare_email(email_content):
    # Read the list of common phrases from the file
    with open("spam_checker.txt", 'r') as file:
        common_phrases = [line.strip().lower() for line in file]

    # Convert email content to lowercase
    email_content = email_content.lower()

    # Initialize variables for amount of spam words and what phrases they are.
    spam_count = 0
    spam_phrases = []

    # Check each phrase from the list against the email content
    for phrase in common_phrases:
        if phrase in email_content:
            spam_count += 1
            spam_phrases.append(phrase)

    return spam_count, spam_phrases

def calculate_likelihood(total_words, spam_count, spam_words):
    if total_words == 0:
        likelihood = 0
    else:
        likelihood = spam_count / total_words * 100
    print()
    print(f"Spam likelihood: {likelihood:.2f}%")
    print(f"Amount of words marked as spam: {spam_count}")
    print("Spam words:", ", ".join(spam_words))

def main():
    create_readable_list()
    email_content = get_email()
    total_words = count_words(email_content)
    spam_count, spam_words = compare_email(email_content)
    calculate_likelihood(total_words, spam_count, spam_words)

if __name__ == "__main__":
    main()