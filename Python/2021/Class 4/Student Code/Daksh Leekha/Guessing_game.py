import random

secret_no = random.randrange(1, 10)
guess_count = 0
guess_limit = 3


def check_num(guess):
    try:
        int(guess)
    except ValueError:
        print("Please enter a valid number. The number cannot contain a decimal.")


while guess_count < guess_limit:
    guess = input('Guess an integer between 1 and 10: ')
    guess_count += 1

    check_num(guess)

    guess = int(guess)

    if guess == secret_no:
        print('You won!')
        break

    else:
        print('\nTry again!\n')
else:
    print('\nSorry, you failed!')
    print(f'\nThe number was: {secret_no}')
