import random
import time

play = True

while play == True:
    play = True

    act = random.randrange(1, 4)
    opt = input("\nPlease type the first letter of your action: ")

    # telling player input
    if opt == "r":
        print("\nYou have chosen rock!")
    elif opt == "s":
        print("\nYou have chosen scissors!")
    elif opt == "p":
        print("\nYou have chosen paper!")
    else:
        print("\nPlease enter a valid input!")
        continue

    time.sleep(1)

    # telling computer choice
    if act == 1:
        print("\nThe computer has chosen rock!")
    elif act == 2:
        print("\nThe computer has chosen scissors!")
    elif act == 3:
        print("\nThe computer has chosen paper!")
    else:
        print(("unexpected error"))
        break

    time.sleep(1)

    # determining the result
    if opt == "r" and act == 1:
        print("\nNothing happened!")
        continue
    elif opt == "r" and act == 2:
        print("\nYou won!")
        time.sleep(1)
        play_again = input("\nWould you like to play again? [y/n] ")
        if play_again == "y":
            play = True
        elif play_again == "n":
            play = False
        else:
            break

    elif opt == "r" and act == 3:
        print("\nYou lost!")

    elif opt == "s" and act == 1:
        print("\nYou lost!")
    elif opt == "s" and act == 3:
        print("\nYou won!")
        time.sleep(1)
        play_again = input("\nWould you like to play again? [y/n] ")
        if play_again == "y":
            play = True
        elif play_again == "n":
            play = False
        else:
            break
    elif opt == "s" and act == 2:
        print("\nNothing happened!")

    elif opt == "p" and act == 1:
        print("\nYou won!")
        time.sleep(1)
        play_again = input("\nWould you like to play again? [y/n] ")
        if play_again == "y":
            play = True
        elif play_again == "n":
            play = False
        else:
            break
    elif opt == "p" and act == 3:
        print("\nNothing happened!")
    elif opt == "p" and act == 2:
        print("\nYou lost!")

print("\nThank you for playing!")
