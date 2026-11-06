import random
try:
    set = ["Rock", "Paper", "Scissors"]

    ran = random.choice(set)

    choice = input("Play rock paper scissors: Choose either 'Rock', 'Paper', or 'Scissors'. Choose now: ").lower()

    if choice == ran:
        print("It was a tie!")
    elif(choice=="Rock" and ran=="Scissors") or (choice=="Paper" and ran=="Rock") or (choice=="Scissors" and ran=="Paper"):
        print("Good job! You won aginst the robot who picked ", ran)
    else:
        print("Unlucky. You lost aginst the robot who picked ", ran)
except:
    print("Either enter 'Rock', 'Paper', or 'Scissors' with the right characters.")
