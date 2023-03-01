import random

COLOURS = ['R', 'G', 'Y', 'B', 'W', 'O']
TRIES = 10
COLOUR_LENGTH = 4


def random_colour():
    randomised = []
    for i in range(COLOUR_LENGTH):
        colour = random.choice(COLOURS)
        randomised.append(colour)
    return randomised


def guess():
    while True:
        user_colours = input("Guess the colour: ").upper().split(" ")

        if len(user_colours) != COLOUR_LENGTH:
            print(f"Error 0: Need {COLOUR_LENGTH} colours")
            continue

        for colours in user_colours:
            if colours not in COLOURS:
                print(f"Error 1: Can only have {COLOURS} colours")
                break
        else:
            break
    return user_colours


def check_colours(guess_code, real_code):
    colour_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for colour in real_code:
        if colour not in colour_counts:
            colour_counts[colour] = 0
        colour_counts[colour] += 1

    for guess_colour, real_colour in zip(guess_code, real_code):
        if guess_colour == real_colour:
            correct_pos += 1
            colour_counts[guess_colour] -= 1

    for guess_colour, real_colour in zip(guess_code, real_code):
        if guess_colour in colour_counts:
            if colour_counts[guess_colour] > 0:
                incorrect_pos += 1
                colour_counts[guess_colour] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to Mastermind, you have {TRIES} tries to guess the code")
    print(f"The valid colours are", *COLOURS)

    randomised = random_colour()
    for attempts in range(0, TRIES):
        guessed = guess()
        correct_pos, incorrect_pos = check_colours(guessed, randomised)
        if correct_pos == COLOUR_LENGTH:
            print("Well Done, The code was", *randomised, f"and it took you {attempts + 1} tries!")
            break
        print(f"Correct Positions: {correct_pos}, Incorrect Positions: {incorrect_pos}")
    else:
        print("You Lose! the code was", *randomised)


if __name__ == "__main__":
    game()
