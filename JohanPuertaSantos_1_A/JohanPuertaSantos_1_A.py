# This program prompts the user several times for their desired number of tickets.
# Each time, the remaining number decreases. The maximum amount each user can take
# is four, with a max total ticket count of twenty. The loop repeats until every ticket
# is sold. The program ends after printing the total number of buyers.

def main():

    buyerCount = 0
    tixTotal = 20

    # Loop until total remaining tickets is less than 1.
    while tixTotal > 0:
        # Prompts for amount user would like to buy.
        tixSale = int(input("Enter amount of tickets you'd like you buy: "))

        # Restricts sale amount to four and ensures buyers cannot buy nothing.
        if tixSale > 4 or tixSale <= 0:
            print("Try again.")

        # Ensures code doesn't end with a buyer buying more than technically available.
        elif tixSale > tixTotal:
            print("Requested amount is greater than remaining ticket count. Try again. REM TIX: ", (tixTotal))

        # If all else is good: add a buyer and remove tickets sold from total amount.
        else:
            buyerCount += 1
            tixTotal -= tixSale

    print()
    print("Total buyers: ", buyerCount)

main()





