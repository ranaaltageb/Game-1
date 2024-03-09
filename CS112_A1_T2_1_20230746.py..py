# File: CS112_A1_T2_1_20230746.py.
# Purpose: Two players start from 0 and alternatively add a number from 1 to 10 to the sum.
# the player who reaches 100 wins.
# Author: Rana altageb alnoor
# ID: 20230746


def display_status(player, total):
    print("Player {}: Total Score = {}".format(player, total))


# Main function to run the game
def main():
    total, player = 0, 1

    # Display initial game status
    display_status(player, total)

    # Main game loop
    while True:
        # Ask the current player to choose a number
        num_str = input("Player {}, please choose a number from 1 to 10: ".format(player))

        # Check if the input is empty
        if not num_str:
            print("Invalid input! Please enter a number.")
            continue

        # Convert the input to an integer
        try:
            num = int(num_str)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # Validate the chosen number
        if not 1 <= num <= 10:
            print("Invalid input! Please choose a number from 1 to 10.")
            continue

        # Update total score
        total += num

        # Display updated game status
        display_status(player, total)

        # Check if any player wins the game
        if total >= 100:
            print("Congratulations! Player {} wins the game!".format(player))
            break

        # Switch to the other player's turn
        if player == 1:
            player = 2
        else:
            player = 1


# Check if the file is being run directly
if __name__ == "__main__":
    main()