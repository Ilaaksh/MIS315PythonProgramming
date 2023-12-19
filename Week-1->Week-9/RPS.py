import time
import random

print("Welcome to Rock, Paper, and Scissors\n")
print("Choose one of the following:")
print("Rock [1]\nPaper [2]\nScissors [3]")

playerPoints = 0
compPoints = 0

while playerPoints < 10 and compPoints < 10:
    try:
        playerChoice = int(input("Please make a selection: "))
    except:
        print ("You entered a letter")

    if playerChoice == 1:
        print("You have selected Rock")

    elif playerChoice == 2:
        print("You have selected Paper")

    elif playerChoice == 3:
        print("You have selected Scissors")

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        continue
    compChoice = random.randint(1, 3)

    time.sleep(0.5)

    if compChoice == 1:
        print("Computer selected Rock")

    elif compChoice == 2:
        print("Computer selected Paper")

    elif compChoice == 3:
        print("Computer selected Scissors")

    if playerChoice == compChoice:
        print("It's a TIE")

    elif (playerChoice == 1 and compChoice == 3) or (playerChoice == 2 and compChoice == 1) or (playerChoice == 3 and compChoice == 2):
        print("YOU WIN")
        playerPoints += 1

    else:
        print("COMPUTER WINS")
        compPoints += 1

    print("Your Points:", playerPoints)
    print("Computer Points:", compPoints)

if playerPoints == 10:
    print("Congratulations! You've won the game.")

if compPoints == 10:
    print("Computer wins. Better luck next time.")
